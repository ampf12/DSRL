from flask import jsonify
from DAO.supplierDAO import SupplierDAO


class SupplierHandler:
    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['sfirst_name'] = row[1]
        result['slast_name'] = row[2]
        result['sphone'] = row[3]
        result['saddress'] = row[4]
        result['sage'] = row[5]
        result['scompany_name'] = row[6]
        return result

    def build_resource_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['ptype'] = row[1]
        result['pquantity'] = row[2]
        # result['pprice'] = row[3]
        return result

    def getAllSuppliers(self):
        # Creates the list of all suppliers calling the DAO which creates the query,
        # this returns a list. The list is then jsonified to be used as a response.

        dao = SupplierDAO()
        # TODO Implemented in later phases
        return dao.getAllSuppliers()

    def getSupplierById(self, sid):
        # Creates the list of the supplier with the given ID calling the DAO which creates the query,
        # this returns a list. The list is then jsonified to be used as a response.

        dao = SupplierDAO()
        # TODO Implemented in later phases
        return dao.getSupplierById(sid)

    def getResourcesBySupplierId(self, sid):
        # Creates the list of the resources of the specified supplier with the given ID calling the
        # DAO which creates the query, this returns a list. The list is then jsonified to be used as a response.

        dao = SupplierDAO()
        # TODO Implemented in later phases
        return dao.getResourcesBySupplierId(sid)

    def searchSuppliers(self, args):
        return "Search by supplier with a specified parameter"

    def insertSupplier(self, form):
        dao = SupplierDAO()
        sid = dao.insert('sname', 'scity', 'sphone')
        return sid
