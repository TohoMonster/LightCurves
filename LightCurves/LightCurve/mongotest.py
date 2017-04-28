__author__ = 'john'

import pymongo
from pymongo import MongoClient

class MongoTest:

    def testing(self):
        client = MongoClient('ubuntu.local', 27017)
        print 'connected'
        name = client.database_names()
        print name
        db = client['starCatalog']
        collections = db.collection_names()
        print collections
        print 'mongo connects'
        #collection = db.get_collection('lightcurveschemas')
        collection = db.get_collection('planetsystems')
        cnt = collection.count()
        print 'planet count ' + str(cnt)
        #one = collection.find()
        #p = one['Planets'][5]
        #for k in p:
        #    print k + '\t' + str(p[k])
        #allPlanets = collection.find()
        #print 'i have all planets'

        #for p in allPlanets:
        #    print p
        client.close()

    def __init__(self):
        print 'testing mongo'


