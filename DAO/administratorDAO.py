from flask import jsonify

class AdministratorDAO:

    def getAllSuppliers(self):
        #Build query selecting all suppliers
        return jsonify("A list of all suppliers is returned")

    def getAllConsumers(self):
        #Build query selecting all consumers
        return jsonify("A list of all consumers is returned")

    def getSupplierByID(self, sid):
        #Build a query to select a supplier by its id
        return jsonify("A supplier with a given ID is returned")

    def getConsumerByID(self,cid):
        #Build a query to select a supplier by its id
        return jsonify("A consumer with a given ID is returned")