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

    def build_orders_dict(self, row):
        result = {}
        result['Person ID'] = row[0]
        result['Consumer ID'] = row[1]
        result['Order ID'] = row[2]
        result['Type'] = row[3]
        result['Quantity'] = row[4]
        result['First Name'] = row[5]
        result['Last Name'] = row[6]
        result['Phone Number'] = row[7]
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

    def insertConsumer(self, form):
        dao = ConsumerDAO()
        sid = dao.insertConsumer('sname', 'scity', 'sphone')
        return sid

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