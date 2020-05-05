import psycopg2
from Config.DbConfig import pg_config


class RequestDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host = ec2-52-202-146-43.compute-1.amazonaws.com" % (
            pg_config['dbname'],
            pg_config['user'],
            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllRequests(self):
        # Build query selecting all orders
        cursor = self.conn.cursor()
        query = "with table1 as (Select * from water union Select * from babyfood union Select * from clothing union Select * from batteries union Select * from cannedfood union Select * from dryfood union Select * from fuel union Select * from heavyequipment union Select * from ice union Select * from medicaldevices union Select * from medications union Select * from powergenerator union Select * from tools)select * from Request natural inner join Consumer natural inner join Person natural inner join Resources natural inner join table1 ;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByID(self, rqid):
        cursor = self.conn.cursor()
        query = "with table1 as (Select * from water union Select * from babyfood union Select * from clothing union Select * from batteries union Select * from cannedfood union Select * from dryfood union Select * from fuel union Select * from heavyequipment union Select * from ice union Select * from medicaldevices union Select * from medications union Select * from powergenerator union Select * from tools)select * from Request natural inner join Consumer natural inner join Person natural inner join Resources natural inner join table1 where rqid =%s ;" % (
            rqid)
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByKeyword(self, keyword):
        cursor = self.conn.cursor()
        query = "with table1 as (Select * from water union Select * from babyfood union Select * from clothing union Select * from batteries union Select * from cannedfood union Select * from dryfood union Select * from fuel union Select * from heavyequipment union Select * from ice union Select * from medicaldevices union Select * from medications union Select * from powergenerator union Select * from tools)select * from Request natural inner join Consumer natural inner join Person natural inner join Resources natural inner join table1 where type ~  '%s' order by type" % (keyword)
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByType(self, type):
        cursor = self.conn.cursor()
        query = "Select * from Request natural inner join Consumer natural inner join Person natural inner join Resources natural inner join %s " % (type)
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestByConsumerID(self, cid):
        # build query to return requests given a consumer id
        cursor = self.conn.cursor()
        query = "with table1 as (Select * from water union Select * from babyfood union Select * from clothing union Select * from batteries union Select * from cannedfood union Select * from dryfood union Select * from fuel union Select * from heavyequipment union Select * from ice union Select * from medicaldevices union Select * from medications union Select * from powergenerator union Select * from tools)select * from Request natural inner join Consumer natural inner join Person natural inner join Resources natural inner join table1 where cid =%s ;" % (
            cid)
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
