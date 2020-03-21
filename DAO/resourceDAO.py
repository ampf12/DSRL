from flask import jsonify

class resourceDAO:

    def getAllResources(self):
        #Build query selecting all resources
        return jsonify("A list of all resources is returned")

    def getResourceByID(self, rid):
        #Build a query to select a resource by its id
        return jsonify("A resource with a given ID is returned")

    def getResourceBySupplierId(self, sid):
        # Create query to select all info resources that a supplier with a given ID has
        return jsonify("A list of resources for the supplier with given ID is returned")