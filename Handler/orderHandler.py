from DAO.orderDAO import orderDAO

class orderHandler:

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

        dao = orderDAO()

        #TODO Implemented in later phase

        return dao.getAllOrders()


    def getOrderByID(self, oid):

        #Returns the supplier based on the sid provided

        dao = orderDAO()

        #TODO Implemented in later phase

        return dao.getOrderByID(oid)

    def getOrderByResourceID(self,rid):

        #Returns the order based on the rid provided

        dao = orderDAO()

        #TODO Implemented in later phase

        return dao.getOrderByResourceId(rid)

    def getOrderBySupplierID(self,sid):

        #Returns the order based on the sid provided

        dao = orderDAO()

        #TODO Implemented in later phase

        return dao.getOrderBySupplierId(sid)

    def searchOrder(self, args):
        return "Search by order with a specified parameter"

    def insertOrder(self, form):
        dao = OrderDAO()
        sid = dao.insert('rtype')
        return oid






