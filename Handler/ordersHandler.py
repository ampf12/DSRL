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

    def build_order_attribute_dict(self,rid,cid,pmethod,oid):
        result = {}
        result['Consumer ID'] = cid
        result['Order ID'] = oid
        result['Payment Method'] = pmethod
        result['Resource ID'] = rid
        return result
    def build_reservation_attribute_dict(self,rid,cid,oid):
        result = {}
        result['Consumer ID'] = cid
        result['Order ID'] = oid
        result['Resource ID'] = rid
        return result

    def build_reservation_dict(self, row):
        result = {}
        result['Person ID'] = row[1]
        result['Consumer ID'] = row[2]
        result['Reservation ID'] = row[3]
        #result['Payment Method'] = row[4]
        # result['Resource ID'] = row[0]
        result['First Name'] = row[5]
        result['Last Name'] = row[6]
        result['Phone Number'] = row[7]
        result['Quantity'] = row[8]
        #result['Price'] = row[9]
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
        dao = OrdersDAO()
        orders_list = dao.getOrderByID(oid)
        result_list = []
        for row in orders_list:
            result = self.build_orders_dict(row)
            result_list.append(result)
        return jsonify(Orders=result_list)


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


########################## REQUESTS #######################################
    def getAllReservations(self):
        dao = OrdersDAO()
        orders_list = dao.getAllReservations()
        result_list = []
        for row in orders_list:
            result = self.build_reservation_dict(row)
            result_list.append(result)
        return jsonify(Reservations=result_list)

    def getReservationById(self, oid):
        dao = OrdersDAO()
        orders_list = dao.getReservationByID(oid)
        result_list = []
        for row in orders_list:
            result = self.build_reservation_dict(row)
            result_list.append(result)
        return jsonify(Reservation=result_list)


    def getReservationsByKeyword(self, rqtype):
        dao = OrdersDAO()
        orders_list = dao.getReservationByKeyword(rqtype)
        result_list = []
        for row in orders_list:
            result = self.build_reservation_dict(row)
            result_list.append(result)
        return jsonify(Reservation=result_list)

    def getReservationsByType(self, type):
        dao = OrdersDAO()
        orders_list = dao.getReservationByType(type)
        result_list = []
        for row in orders_list:
            result = self.build_reservation_dict(row)
            result_list.append(result)
        return jsonify(Reservations=result_list)

    def getReservationsByConsumerId(self, cid):
        dao = OrdersDAO()
        orders_list = dao.getReservationsByConsumerId(cid)
        result_list = []
        for row in orders_list:
            result = self.build_reservation_dict(row)
            result_list.append(result)
        return jsonify(Reservations=result_list)


    #############################################################
    def searchOrders(self, args):
        return "Search by orders with a specified parameter"

    def insertOrderJson(self, json):
        rid = json['rid']
        cid = json['cid']
        pmethod = json['pmethod']
        if rid and cid and pmethod:
            dao = OrdersDAO()
            oid = dao.insert(cid,rid,pmethod)
            result = self.build_order_attribute_dict(rid,cid,pmethod,oid)
            return jsonify(Order=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def insertReservationJson(self, json):
        rid = json['rid']
        cid = json['cid']
        if rid and cid:
            dao = OrdersDAO()
            oid = dao.insertReservation(cid,rid)
            result = self.build_reservation_attribute_dict(rid,cid,oid)
            return jsonify(Order=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400






