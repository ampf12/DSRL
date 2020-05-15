from flask import jsonify
from DAO.consumerDao import ConsumerDAO


class ConsumerHandler:
    def build_consumer_dict(self, row):
        result = {}
        result['Person ID'] = row[0]
        result['Consumer ID'] = row[1]
        result['First Name'] = row[2]
        result['Last Name'] = row[3]
        result['Phone Number'] = row[4]
        return result
    def build_consumer_attribute_dict(self, sname, slast_name, sphone_number, cid):
        result = {}
        #result['Person ID'] = row[0]
        result['Consumer ID'] = cid
        result['First Name'] = sname
        result['Last Name'] = slast_name
        result['Phone Number'] = sphone_number
        return result

    def build_orders_dict(self, row):
        result = {}
        result['Person ID'] = row[1]
        result['Consumer ID'] = row[2]
        result['Order ID'] = row[3]
        result['Payment Method'] = row[4]
        #result['Resource ID'] = row[0]
        result['First Name'] = row[5]
        result['Last Name'] = row[6]
        result['Phone Number'] = row[7]
        result['Quantity'] = row[8]
        result['Price'] = row[9]
        #result['Latitude'] = row[10]
        #result['Longitude'] = row[11]
        result['Type'] = row[13]

        return result

    def getAllConsumers(self):
        # Creates the list of all consumers calling the DAO which creates the query,
        # this returns a list. The list is then jsonified to be used as a response.
        dao = ConsumerDAO()
        consumers_list = dao.getAllConsumers()
        result_list = []
        for row in consumers_list:
            result = self.build_consumer_dict(row)
            result_list.append(result)
        return jsonify(Consumer=result_list)

    def getConsumerById(self, cid):
        # Creates the list of the consumer with the given ID calling the DAO which creates the query,
        # this returns a list. The list is then jsonified to be used as a response.
        dao = ConsumerDAO()
        consumers_list = dao.getConsumerById(cid)
        result_list = []
        for row in consumers_list:
            result = self.build_consumer_dict(row)
            result_list.append(result)
        return jsonify(Consumer=result_list)

    def getOrdersByConsumerId(self, cid):
        # Creates the list of the resources the consumer needs calling the DAO which creates the query,
        # this returns a list. The list is then jsonified to be used as a response.
        dao = ConsumerDAO()
        orders_list = dao.getOrdersByConsumerId(cid)
        result_list = []
        for row in orders_list:
            result = self.build_orders_dict(row)
            result_list.append(result)
        return jsonify(Orders=result_list)

###################################################################

    def searchConsumers(self, args):
        return "Search by consumer with a specified parameter"

    def insertConsumerJson(self, json):
        sname = json['sname']
        slast_name = json['slast_name']
        sphone_number = json['sphone_number']
        if sname and slast_name and sphone_number:
            dao = ConsumerDAO()
            cid = dao.insert(sname, slast_name, sphone_number)
            result = self.build_consumer_attribute_dict(sname, slast_name, sphone_number, cid)
            return jsonify(Consumer=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    @classmethod
    def makeRequestForResources(self, form):
        dao = ConsumerDAO()
        rid = dao.insertRequest('rid', 'rtype', 'rquantity','cid')
        return rid

    @classmethod
    def makeReservationForResources(self, form):
        dao = ConsumerDAO()
        rid = dao.insertReservation('rid','cid')
        return rid