from DAO.resourceDAO import ResourceDAO


class ResourceHandler:

    def build_resource_dic(self, row):
        result = {}
        result['rid'] = row[0]
        result['rtype'] = row[1]
        result['rquantity'] = row[2]

        return result

    def getAllResources(self):

        # Creates the list of all resources calling the DAO which creates the query,
        # this returns a list. This list is then jsonified to be used as a response.

        dao = ResourceDAO()

        #TODO Implemented in later phase
        return dao.getAllResources()


    def getResourceById(self,rid):

        #Returns the resource based on the rid provided

        dao = ResourceDAO()

        #TODO Implemented in later phase
        return dao.getResourceByID(rid)

    def getResourceBySupplierId(self,sid):

        #Returns the resource based on the sid provided

        dao = ResourceDAO()

        #TODO Implemented in later phase
        return dao.getResourceBySupplierId(sid)

    def searchResource(self, args):
        return "Search by resource with a specified parameter"

    def insertResource(self, form):
        dao = ResourceDAO()
        rid = dao.insert('rtype')
        return "Insertion of Resource (?)"