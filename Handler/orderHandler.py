from DAO.orderDAO import OrderDAO


class OrderHandler:

    def build_order_dic(self, row):
        result = {}
        result['oid'] = row[0]
        result['otype'] = row[1]
        result['sid'] = row[2]
        result['rid'] = row[2]

        return result

    def getAllOrders(self):

        # Creates the list of all orders calling the DAO which creates the query,
        # this returns a list. This list is then jsonified to be used as a response.

        dao = OrderDAO()

        #TODO Implemented in later phase
        return dao.getAllOrders()


    def getOrderById(self, oid):

        #Returns the supplier based on the sid provided

        dao = OrderDAO()

        #TODO Implemented in later phase
        return dao.getOrderByID(oid)

    def getOrderByResourceId(self,rid):

        #Returns the order based on the rid provided

        dao = OrderDAO()

        #TODO Implemented in later phase
        return dao.getOrderByResourceId(rid)

    def getOrderBySupplierId(self,sid):

        #Returns the order based on the sid provided

        dao = OrderDAO()

        #TODO Implemented in later phase
        return dao.getOrderBySupplierId(sid)

    # What?
    def searchOrder(self, args):
        return "Search by order with a specified parameter"

    def insertOrder(self, form):
        dao = OrderDAO()
        sid = dao.insert('rtype')
        return "Order inserted, return id"






