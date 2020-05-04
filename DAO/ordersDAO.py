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
        query = "with table1 as (Select * from water union Select * from babyfood union Select * from clothing union Select * from batteries union Select * from cannedfood union Select * from dryfood union Select * from fuel union Select * from heavyequipment union Select * from ice union Select * from medicaldevices union Select * from medications union Select * from powergenerator union Select * from tools)select * from Orders natural inner join Consumer natural inner join Person natural inner join Resources natural inner join table1;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrderByID(self, oid):
        # Build a query to select an order by its id
        cursor = self.conn.cursor()
        query = "with table1 as (Select * from water union Select * from babyfood union Select * from clothing union Select * from batteries union Select * from cannedfood union Select * from dryfood union Select * from fuel union Select * from heavyequipment union Select * from ice union Select * from medicaldevices union Select * from medications union Select * from powergenerator union Select * from tools)select * from Orders natural inner join Consumer natural inner join Person natural inner join Resources natural inner join table1 where oid = %s" % (
            oid)
        cursor.execute(query)
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

    def getOrderByKeyword(self, keyword):
        cursor = self.conn.cursor()
        query = "with table1 as (Select * from water union Select * from babyfood union Select * from clothing union Select * from batteries union Select * from cannedfood union Select * from dryfood union Select * from fuel union Select * from heavyequipment union Select * from ice union Select * from medicaldevices union Select * from medications union Select * from powergenerator union Select * from tools)select * from Orders natural inner join Consumer natural inner join Person natural inner join Resources natural inner join table1 where type ~  '%s'" % (keyword)
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrderByType(self, type):
        cursor = self.conn.cursor()
        query = "Select * from Orders natural inner join Consumer natural inner join Person natural inner join Resources natural inner join %s;" % (type)
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


