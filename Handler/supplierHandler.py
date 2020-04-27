from flask import jsonify
from DAO.supplierDAO import SupplierDAO


class SupplierHandler:
    def build_supplier_dict(self, row):
        result = {}
        result['Supplier ID'] = row[0]
        result['First Name'] = row[1]
        result['Last Name'] = row[2]
        result['Phone'] = row[3]
        result['Person ID'] = row[4]
        result['Company Name'] = row[5]
        return result

    def build_resource_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['ptype'] = row[1]
        result['pquantity'] = row[2]
        result['pprice'] = row[3]
        result['platitude'] = row[4]
        result['plongitude'] = row[5]
        return result

    def getAllSuppliers(self):
        # Creates the list of all suppliers calling the DAO which creates the query,
        # this returns a list. The list is then jsonified to be used as a response.
        dao = SupplierDAO()
        suppliers_list = dao.getAllSuppliers()
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getSupplierById(self, sid):
        # Creates the list of the supplier with the given ID calling the DAO which creates the query,
        # this returns a list. The list is then jsonified to be used as a response.
        dao = SupplierDAO()
        suppliers_list = dao.getSupplierById(sid)
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getResourcesBySupplierId(self, sid):
        # Creates the list of the resources of the specified supplier with the given ID calling the
        # DAO which creates the query, this returns a list. The list is then jsonified to be used as a response.
        dao = SupplierDAO()
        resources_list = dao.getResourcesBySupplierId(sid)
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def searchSuppliers(self, args):
        return "Search by supplier with a specified parameter"

    def insertSupplier(self, form):
        dao = SupplierDAO()
        sid = dao.insert('sname', 'scity', 'sphone')
        return sid
