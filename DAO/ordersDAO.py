import psycopg2
from Config.DbConfig import pg_config


class OrdersDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host = ec2-52-202-146-43.compute-1.amazonaws.com" % (
        pg_config['dbname'],
        pg_config['user'],
        pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllOrders(self):
        # Build query selecting all orders
        cursor = self.conn.cursor()
        query = "select * from Orders;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrderByID(self, oid):
        # Build a query to select an order by its id
        cursor = self.conn.cursor()
        query = "select * from Orders where oid = %s;" % (oid)
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # def getOrderByConsumerId(self, cid):
    #     # Build query to return orders given a consumer id
    #     cursor = self.conn.cursor()
    #     query ="select * from Orders natural inner join Consumer natural inner join Person where Consumer.cid = %s;" % cid
    #     cursor.execute(query)
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result

    def getOrderByType(self, otype):
        # Build query returning orders with given type
        cursor = self.conn.cursor()
        query = "select * from Orders where otype = %s;" % otype
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

