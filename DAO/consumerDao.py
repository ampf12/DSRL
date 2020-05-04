import psycopg2
from flask import jsonify
from Config.DbConfig import pg_config


class ConsumerDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host = ec2-52-202-146-43.compute-1.amazonaws.com" % (
            pg_config['dbname'],
            pg_config['user'],
            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllConsumers(self):
        # Build query selecting all consumers
        cursor = self.conn.cursor()
        query = "select * from Consumer natural inner join Person;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getConsumerById(self, cid):
        # Build query to select a consumer by its ID
        cursor = self.conn.cursor()
        query = "select * from Consumer natural inner join Person where Consumer.cid = %s;" % cid
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrdersByConsumerId(self, cid):
        # Create query to select the orders plaaced by a consumer with given id
        cursor = self.conn.cursor()
        query = "with table1 as (Select * from water union Select * from babyfood union Select * from clothing union Select * from batteries union Select * from cannedfood union Select * from dryfood union Select * from fuel union Select * from heavyequipment union Select * from ice union Select * from medicaldevices union Select * from medications union Select * from powergenerator union Select * from tools)select * from Orders natural inner join Consumer natural inner join Person natural inner join Resources natural inner join table1 where not pmethod = 'NONE' and  Consumer.cid = %s" %(cid)
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    ###############################################################################

    def insertConsumer(self, sname, scity, sphone):
        return jsonify("Returns the id of the consumer inserted into the DB")

    def insertRequest(self, rid, rtype, rquantity, cid):
        # Create query to insert a request for a resource into the DB
        return jsonify("Returns the id of the request inserted into the DB")

    def insertReservation(self, rid, cid):
        return jsonify("Returns the id of the reservation of resources inserted into the DB")
