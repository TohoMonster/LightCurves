__author__ = 'john'

pip install --user -e git+https://github.com/hplgit/scitools.git#egg=scitools

import scipy as sp
import numpy as np
import matplotlib as plot
import ConfigParser as config

#from astropy import analytic_functions as af

import pymongo
from pymongo import MongoClient
import mongotest

import helpers.astrophysics as phys
import helpers.buildLightCurve as curve
import time

def main():
    print 'in main'
    pc = phys.AstroPhysics().getParsecFromParalex(768.87 / 1000)
    print pc
    print pc * 3.26
    aMag = phys.AstroPhysics().getAbsoluteMagitudeFromParsec(11.09, pc)
    print aMag

def mongoTest():
    test = mongotest.MongoTest().testing()

def buildCurves():
    cnt = 0
    client = MongoClient(host = 'ubuntu.local', port = 27017)
    db = client['starCatalog']
    collection = db.get_collection('planetsystems')
    allPlanets = collection.find(no_cursor_timeout = True)

    for planet in allPlanets:
        start = time.time()
        cnt = cnt + 1
        print 'allPlanets # ' + str(cnt)
        data = curve.buildLightCurve().lightCurve(planet)
#        print('saving')
#        curveCollection = db.get_collection('lightcurveschemas')
#        curveCollection.insert_many(data)

        end = time.time()
        total = end - start
        print ('total time: ' + str(total))
    client.close()
    print 'Finished!'

if __name__ == "__main__":
    print 'starting'
    #buildCurves()
    #mongoTest()