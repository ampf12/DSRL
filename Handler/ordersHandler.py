from flask import jsonify

from DAO.ordersDAO import OrdersDAO


class OrdersHandler:

    def build_orders_dict(self, row):
        result = {}
        result['Person ID'] = row[1]
        result['Consumer ID'] = row[2]
        result['Order ID'] = row[3]
        result['Payment Method'] = row[4]
        # result['Resource ID'] = row[0]
        result['First Name'] = row[5]
        result['Last Name'] = row[6]
        result['Phone Number'] = row[7]
        result['Quantity'] = row[8]
        result['Price'] = row[9]
        # result['Latitude'] = row[10]
        # result['Longitude'] = row[11]
        result['Type'] = row[13]
        return result

    def build_consumer_dict(self, row):
        result = {}
        result['Consumer ID'] = row[0]
        result['First Name'] = row[1]
        result['Last Name'] = row[2]
        result['Phone Number'] = row[3]
        return result

    def getAllOrders(self):
        # Creates the list of all orders calling the DAO which creates the query,
        # this returns a list. This list is then jsonified to be used as a response.
        dao = OrdersDAO()
        orders_list = dao.getAllOrders()
        result_list = []
        for row in orders_list:
            result = self.build_orders_dict(row)
            result_list.append(result)
        return jsonify(Orders=result_list)

    def getOrderById(self, oid):
        # Returns the supplier based on the sid provided
        dao = OrdersDAO()
        orders_list = dao.getOrderByID(oid)
        result_list = []
        for row in orders_list:
            result = self.build_orders_dict(row)
            result_list.append(result)
        return jsonify(Orders=result_list)

    # def getOrdersByConsumerId(self, cid):
    #     dao = OrdersDAO()
    #     orders_list = dao.getOrderByConsumerId(cid)
    #     result_list = []
    #     for row in orders_list:
    #         result = self.build_consumer_dict(row)
    #         result_list.append(result)
    #     return jsonify(Orders=result_list)

    def getOrdersByKeyword(self, otype):
        dao = OrdersDAO()
        orders_list = dao.getOrderByKeyword(otype)
        result_list = []
        for row in orders_list:
            result = self.build_orders_dict(row)
            result_list.append(result)
        return jsonify(Orders=result_list)

    def getOrdersByType(self, type):
        dao = OrdersDAO()
        orders_list = dao.getOrderByType(type)
        result_list = []
        for row in orders_list:
            result = self.build_orders_dict(row)
            result_list.append(result)
        return jsonify(Orders=result_list)

    #############################################################
    def searchOrders(self, args):
        return "Search by orders with a specified parameter"

    def insertOrders(self, form):
        dao = OrdersDAO()
        sid = dao.insert('rtype')
        return "Orders inserted, return id"






