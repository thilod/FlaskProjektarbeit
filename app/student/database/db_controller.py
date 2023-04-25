import pymongo


class database_controller():

    def __init__(self, database, table):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.client[database]
        self.mycol = self.mydb[table]

    def create_database(self, database):
        self.mydb = self.client[database]

    def create_table(self, table):
        self.mycol = self.mydb[table]

    def insert(self, data):
        mydict = data

        x = self.mycol.insert_one(mydict)
        print(x.inserted_id)

    def update(self, query, new_values):
        new_values = {"$set": new_values}
        self.mycol.update_one(query, new_values)

    def delete(self, query):
        self.mycol.delete_one(query)

    def get(self, query=""):
        result = []
        if query == "":
            for x in self.mycol.find():
                # print(x)
                result.append(x)
        else:
            for x in self.mycol.find(query):
                # print(x)
                result.append(x)
        return result

    def count(self):
        number = self.mycol.count_documents({})
        return number


# Erzeugt eine MongoDB Datenbank mit dem Table 'test'
db = database_controller("software_praktikum_db", "test")
# Testdatensatz
data = {'test_id': 'djfj8ksa7l85h7gkjl78h7gl87dj', 'test': 'test'}
# Einfügen des Testdatensatzes in den Table 'test'
db.insert(data)
