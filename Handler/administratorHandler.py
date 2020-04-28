from flask import jsonify

from DAO.administratorDAO import AdministratorDAO

class AdministratorHandler:

    def build_administrator_dict(self, row):
        result = {}
        result['Administrator ID'] = row[4]
        result['First Name'] = row[1]
        result['Last Name'] = row[2]
        result['Phone Number'] = row[3]
        result['Person ID'] = row[0]

        return result

    def getAllAdministrators(self):

        # Creates the list of all suppliers calling the DAO which creates the queary,
        # this returns a list. This list is then jsonified to be used as a response.

        dao = AdministratorDAO()
        administrators_list = dao.getAllAdministrators()
        result_list = []
        for row in administrators_list:
            result = self.build_administrator_dict(row)
            result_list.append(result)
        return jsonify(Administrators=result_list)

    def getAdministratorById(self, sid):
        # Creates the list of the supplier with the given ID calling the DAO which creates the query,
        # this returns a list. The list is then jsonified to be used as a response.
        dao = AdministratorDAO()
        administrators_list = dao.getAdministratorById(sid)
        result_list = []
        for row in administrators_list:
            result = self.build_administrator_dict(row)
            result_list.append(result)
        return jsonify(Administrator=result_list)

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

    def searchSuppliers(self, args):
        return "Search by supplier with a specified parameter"

    def insertSupplier(self, form):
        dao = AdministratorDAO()
        sid = dao.insert('sname', 'scity', 'sphone')
        return sid

    def insertAdministrator(self, form):
        dao = AdministratorDAO()
        sid = dao.insert('sname', 'scity', 'sphone')
        return sid

    def searchConsumers(self, args):
        return "Search by consumer with a specified parameter"

    def insertConsumer(self, form):
        dao = AdministratorDAO()
        sid = dao.insertConsumer('sname', 'scity', 'sphone')
        return sid
