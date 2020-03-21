from DAO.resourceDAO import resourceDAO

class resourceHandler:

    def build_resource_dic(self, row):
        result = {}
        result['rid'] = row[0]
        result['rtype'] = row[1]
        result['rquantity'] = row[2]

        return result

    def getAllResources(self):

        # Creates the list of all resources calling the DAO which creates the query,
        # this returns a list. This list is then jsonified to be used as a response.

        dao = resourceDAO()

        #TODO Implemented in later phase

        return dao.getAllResources()


    def getResourceByID(self,rid):

        #Returns the resource based on the rid provided

        dao = resourceDAO()

        #TODO Implemented in later phase

        return dao.getResourceByID(rid)

    def getResourceBySupplierID(self,sid):

        #Returns the resource based on the sid provided

        dao = resourceDAO()

        #TODO Implemented in later phase

        return dao.getResourceBySupplierId(sid)

    def searchResource(self, args):
        return "Search by resource with a specified parameter"

    def insertResource(self, form):
        dao = ResourceDAO()
        sid = dao.insert('rtype')
        return rid