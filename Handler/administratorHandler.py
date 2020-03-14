from DAO.administratorDAO import AdministratorDAO

class AdministratorHandler:

    def build_administrator_dic(self, row):
        result = {}
        result['aid'] = row[0]
        result['afirst_name'] = row[1]
        result['alast_name'] = row[2]

        return result

    def getAllSuppliers(self):

        # Creates the list of all suppliers calling the DAO which creates the queary,
        # this returns a list. This list is then jsonified to be used as a response.

        dao = AdministratorDAO()

        #TODO Implemented in later phase

        return dao.getAllSuppliers()

    def getAllConsumers(self):

        #Creates the list of all consumers calling the DAO which creates the queary,
        #this returns a list. This list is then jsonified to be used as a response.

        dao = AdministratorDAO()

        #TODO Implemented in later phase

        return dao.getAllConsumers()

    def getSupplierByID(self,sid):

        #Returns the supplier based on the sid provided

        dao = AdministratorDAO()

        #TODO Implemented in later phase

        return dao.getSupplierByID(sid)

    def getConsumerbyID(self,cid):

        #Returns a consumer based on the cid provided

        dao = AdministratorDAO()

        #TODO Implemented in later phase

        return dao.getConsumerByID(cid)








