from flask import jsonify
from DAO.resourceDAO import ResourceDAO


class ResourceHandler:

    def build_resource_dic(self, row):
        result = {}
        result['Resource ID'] = row[0]
        result['Type'] = row[2]
        result['Quantity'] = row[1]
        result['Price'] = row[3]
        return result

    def getAllResources(self):
        # Creates the list of all resources calling the DAO which creates the query,
        # this returns a list. This list is then jsonified to be used as a response.
        dao = ResourceDAO()
        resources_list = dao.getAllResources()
        result_list = []
        for row in resources_list:
            result = self.build_resource_dic(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getResourceById(self,rid):
        # Returns the resource based on the rid provided
        dao = ResourceDAO()
        resources_list = dao.getResourceByID(rid)
        result_list = []
        for row in resources_list:
            result = self.build_resource_dic(row)
            result_list.append(result)
        return jsonify(Resource=result_list)

    def getResourceBySupplierId(self, sid):
        # Returns the resource based on the sid provided
        dao = ResourceDAO()
        resources_list = dao.getResourceBySupplierId(sid)
        result_list = []
        for row in resources_list:
            result = self.build_resource_dic(row)
            result_list.append(result)
        return jsonify(Resource=result_list)

    def searchResource(self, args):
        return "Search by resource with a specified parameter"

    def insertResource(self, form):
        dao = ResourceDAO()
        rid = dao.insert('rtype')
        return "Insertion of Resource (?)"