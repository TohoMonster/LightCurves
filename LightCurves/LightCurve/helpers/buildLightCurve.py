__author__ = 'john'

import math
from astropy import constants as const
import astrophysics
import datetime
import time
import pymongo
from pymongo import MongoClient

# 2.2 mps max
# 1.5 mps min
# 1.8 mps average

# 55e90987c26755a4ea513a4f star id for 101

class buildLightCurve:

    SHOTS = 48 # 24 hours of shots every 1/2 hour
    YEAR = 365 # days in a year
    YEARS = 10 # observation time
    DURATION = YEARS * YEAR * SHOTS
    CIRCLE = 360
    SUN_RADIUS = 695508000 #const.R_sun
    SECONDS = 30 * 60 # seconds in a half hour
    AU = 1.49597871e+11

    def __init__(self):
        pass

    def lightCurve(self, starData):
        #print starData
        star = starData['Star']
        print ' star id: ' + str(starData['_id'])
        physics = astrophysics.AstroPhysics()
        STAR_RADIUS = self.SUN_RADIUS * physics.getRadiusFromLuminosity(star['luminosity'])
        SOLAR_DIAMETER = STAR_RADIUS * 2
        SOLAR_WIDTH = SOLAR_DIAMETER / self.AU
        SOLAR_X = 0
        SOLAR_0 = 0
        curve = 1
        stamp = time.time()
        allPlanets = starData['Planets']
        pLen = len(allPlanets)
        cx = 0
        cy = 0
        r = 0
        yearInDays = 0
        curveData = []

        for i in range(0, self.DURATION):
            curve = 1.0
            stamp = stamp + self.SECONDS

            for p in range(0, pLen):
                planet = starData['Planets'][p]
                yearInDays = planet['lengthOfYear'] * self.YEAR
                r = planet['distanceFromPrimaryStar']
                SOLAR_X = self._calcSolarX(SOLAR_WIDTH, r * self.AU)
                cx = self._calcX(i, yearInDays, r)
                cy = self._calcY(i, yearInDays, r)

                if cx >= SOLAR_0 and cx <= SOLAR_X and cy < 0:
                    ratio = (planet['equatorialRadius'] / STAR_RADIUS)
                    dip = math.pow(ratio, 2)
                    curve = curve - dip

                curveData.append({'star_id': starData['_id'], 'timestamp': stamp, 'brightness': curve})

        self._saveCurve(curveData)

    def _saveCurve(self, data):
        client = MongoClient('ubuntu.local', 27017)
        print ' connected'
        db = client['starCatalog']
        curveCollection = db.get_collection('lightcurveschemas_2')
        curveCollection.insert_many(data)
        client.close()
        print ' closed'

    def _calcX(self, i, days, radius):
        amp = radius / 100.0
        deg = (i / days) * self.CIRCLE
        rad = self._getRadianFromDegrees(deg, radius)
        ret = math.sin(rad) / amp
        return ret

    def _calcY(self, i, days, radius):
        amp = radius / 100.0
        deg = (i / days) * self.CIRCLE
        rad = self._getRadianFromDegrees(deg, radius)
        ret = math.cos(rad) / amp
        return ret

    def _calcSolarX(self, width, au):
        amp = 1.0/100.0
        ret = (width * 2) / amp
        return ret

    def _getRadianFromDegrees(self, degree, radius):
        rad = 2 * math.pi * radius
        return rad * (degree / self.CIRCLE)

