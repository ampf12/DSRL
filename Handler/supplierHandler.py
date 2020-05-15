

from flask import jsonify
from DAO.supplierDAO import SupplierDAO


class SupplierHandler:
    def build_supplier_dict(self, row):
        result = {}
        result['Supplier ID'] = row[4]
        result['First Name'] = row[1]
        result['Last Name'] = row[2]
        result['Phone'] = row[3]
        result['Person ID'] = row[0]
        result['Company Name'] = row[5]
        return result

    def build_supplier_attribute_dict(self, sname, slast_name,sphone_number,scompany_name,sid):
        result = {}
        result['Supplier ID'] = sid
        result['First Name'] = sname
        result['Last Name'] = slast_name
        result['Phone'] = sphone_number
       # result['Person ID'] = row[0]
        result['Company Name'] = scompany_name
        return result

    def build_resource_dict(self, row):
        result = {}
        result['Resource ID'] = row[0]
        result['Type ID'] = row[1]
        result['Resource'] = row[2]
        result['Quantity'] = row[3]
        result['Price'] = row[4]
        result['Latitude'] = row[5]
        result['Longitude'] = row[6]
        result['Google Map Location'] = 'https://www.google.com/maps/search/%s,%s' % (row[5], row[6])
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

    def insertSupplierJson(self, json):
        sname = json['sname']
        slast_name = json['slast_name']
        scompany_name = json['scompany_name']
        sphone_number = json['sphone_number']
        if sname and slast_name and scompany_name and sphone_number:
            dao = SupplierDAO()
            sid = dao.insert(sname, slast_name ,scompany_name ,sphone_number)
            result = self.build_supplier_attribute_dict(sname, slast_name,sphone_number,scompany_name,sid)
            return jsonify(Supplier=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400


