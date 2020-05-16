from flask import jsonify

from DAO.requestDAO import RequestDAO


class RequestHandler:

    def build_request_dict(self, row):
        result = {}
        #result['Resource ID'] = row[0]
        #result['Person ID'] = row[1]
        result['Consumer ID'] = row[2]
        result['Request ID'] = row[3]
        result['First Name'] = row[4]
        result['Last Name'] = row[5]
        result['Phone Number'] = row[6]
        result['Quantity'] = row[7]
        #result['Price'] = row[8]
        #result['Latitude'] = row[9]
        #result['Longitude'] = row[10]
        #result['Type ID'] = row[11]
        result['Resource'] = row[12]
        return result

    def build_request_attribute_dict(self, cid, rid):
        result = {}
        #result['Request ID'] = rqid
        result['Consumer ID'] = cid
        result['Resource ID'] = rid
        return result

    def getAllRequests(self):
        # Creates the list of all orders calling the DAO which creates the query,
        # this returns a list. This list is then jsonified to be used as a response.
        dao = RequestDAO()
        orders_list = dao.getAllRequests()
        result_list = []
        for row in orders_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Reqsssssuests=result_list)

    def getRequestById(self, rid):
        dao = RequestDAO()
        requests_list = dao.getRequestByID(rid)
        result_list = []
        for row in requests_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)

    def getRequestByKeyword(self, keyword):
        dao = RequestDAO()
        requests_list = dao.getRequestByKeyword(keyword)
        result_list = []
        for row in requests_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)

    def getRequestByType(self, type):
        dao = RequestDAO()
        requests_list = dao.getRequestByType(type)
        result_list = []
        for row in requests_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)

    def getRequestByConsumerId(self, cid):
        # Creates the list of the resources the consumer needs calling the DAO which creates the query,
        # this returns a list. The list is then jsonified to be used as a response.
        dao = RequestDAO()
        requests_list = dao.getRequestByConsumerID(cid)
        result_list = []
        for row in requests_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)


    #############################################################
    def searchRequests(self, args):
        return "Search by requests with a specified parameter"

    def insertRequests(self, json):
        #rqid = json['rqid']
        cid = json['cid']
        rid = json['rid']
        if cid and rid:
            dao = RequestDAO()
            dao.insertRequests(cid, rid)
            result = self.build_request_attribute_dict(cid, rid)
            return jsonify(Requests=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400
