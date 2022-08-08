from pymongo import MongoClient
import pymongo


def get_database(password):
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://jcybul:"+password+"@cluster0.mstxt1s.mongodb.net/?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client  = ""
    try:
     client = MongoClient(CONNECTION_STRING)
    except:
        return "Error"

    # Create the database for our example (we will use the same database throughout the tutorial
    return client
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    dbname = get_database()
    print(dbname)