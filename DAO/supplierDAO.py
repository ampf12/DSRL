from flask import jsonify


class SupplierDAO:

    def getAllSuppliers(self):
        # Build query selecting all suppliers
        return jsonify("A list of all suppliers is returned")

    def getSupplierById(self, sid):
        # Build query to select a supplier by its ID
        return jsonify("A supplier with a given ID is returned")

    def getResourcesBySupplierId(self, sid):
        # Create query to select all info resources that a supplier with a given ID has
        return jsonify("A list of resources for the supplier with given ID is returned")

    def insert(self, sname, scity, sphone):
        # Create query to insert a supplier into the DB
        return jsonify("Returns the id of the supplier inserted into the DB")