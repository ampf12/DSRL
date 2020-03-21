from flask import jsonify

class orderDAO:

    def getAllOrders(self):
        #Build query selecting all orders
        return jsonify("A list of all orders is returned")

    def getOrderByID(self, oid):
        #Build a query to select an order by its id
        return jsonify("An order with a given ID is returned")

    def getOrderByResourceId(self, rid):
        # Create query to select all info of orders that a resource with a given ID has
        return jsonify("A list of orders for the resource with given ID is returned")

    def getOrderBySupplierId(self, sid):
        # Create query to select all info of orders that a supplier with a given ID has
        return jsonify("A list of orders for the supplier with given ID is returned")