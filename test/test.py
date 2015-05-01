#!/usr/bin/python

import pymongo

def connect():
        try:
                global conn
                conn=pymongo.MongoClient('localhost', 7001)
                print "INFO connect: Connected successfully!"
        except pymongo.errors.ConnectionFailure, e:
                print "ERROR connect: Could not connect to MongoDB: %s" % e
				
def createdb():
        global conn
        global db
        db = conn.mydb
		
def listdb():
        global conn
        print "INFO listdb: " + str(conn.database_names())
		
def createcollection():
        global conn
        global db
        global collection
        collection = db.my_collection
		
def listcollection():
        global conn
        global db
        print "INFO listcollection: " + str(db.collection_names())
		
def createdocument():
        global conn
        global db
        global collection
        try:
            doc = {"name":"Ali Okan","surname":"Yuksel","twitter":"@aliokanyuksel"}
            collection.insert_one(doc)
            print "INFO createdocument: " + str(doc)
        except Exception as e:
			print "ERROR createdocument: " + str(e)
			
def main():
        connect()
        createdb()
        listdb()
        createcollection()
        listcollection()
        createdocument()
		
if __name__ == "__main__":
        main()
