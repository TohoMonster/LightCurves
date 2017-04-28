__author__ = 'john'

from astropy import units as u
from astropy import constants as const
import math

class AstroPhysics:

    sun_absolute_magnitude = 4.77

    def __init__(self):
        pass

    def getParsecFromParalex(self, plx):
        return 1 / plx

    def getAbsoluteMagnitudeFromParalex(self, vMag, plx):
        pc = self.getParsecFromParalex(plx);
        return self.getAbsoluteMagitudeFromParsec(vMag, pc)

    def getAbsoluteMagitudeFromParsec(self, vMag, parsec):
        # m + 5 - (5 * log10 D)
        ad = vMag + 5
        pc = 5 * math.log(parsec, 10)
        aMag = ad - pc
        #aMag = (5 * (math.log((parsec / 10), 10)) - vMag) * -1
        return aMag

    def getLuminosityFromAbsoluteMagnitude(self, aMag):
        lum =  math.log(abs, 10) / self.sun_absolute_magnitude
        return lum

    def getLuminosityFromVisulaMagitude(self, vMag, plx):
        aMag = self.getAbsoluteMagnitudeFromParalex(vMag, plx)
        lum = self.getLuminosityFromAbsoluteMagnitude(aMag)
        return lum

    def getMassFromLuminosity(self, lum):
        return math.pow(lum, 0.286)

    def getMassFromVisualMagnitude(self, vMag, plx):
        lum = self.getAbsoluteMagnitudeFromParalex(vMag, plx)
        return self.getMassFromLuminosity(lum)

    def getLuminosityFromMass(self, mass):
        p = 3.9
        if 7 <= mass and mass < 25:
            p = 3.0
        if mass >= 25:
            p = 2.7

        return math.pow(mass, p)

    def getRadiusFromLuminosity(self, lum):
        return math.sqrt(lum)

    def getTempratureFromLuminosity(self, lum):
        return math.pow(lum, 1/4)