from flask import jsonify
import psycopg2
from Config.DbConfig import pg_config

class SupplierDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host = ec2-52-202-146-43.compute-1.amazonaws.com" % (
        pg_config['dbname'],
        pg_config['user'],
        pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllSuppliers(self):
        # Build query selecting all suppliers
        # return jsonify("A list of all suppliers is returned")
        cursor = self.conn.cursor()
        query = "select * from Person natural inner join Supplier;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierById(self, sid):
        # Build query to select a supplier by its ID
        cursor = self.conn.cursor()
        query = "select * from Person natural inner join Supplier where Supplier.sid = %s;" % (sid)
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierId(self, sid):
        # Create query to select all info resources that a supplier with a given ID has
        cursor = self.conn.cursor()
        query = "with table1 as (Select * from water union Select * from babyfood union Select * from clothing union Select * from batteries union Select * from cannedfood union Select * from dryfood union Select * from fuel union Select * from heavyequipment union Select * from ice union Select * from medicaldevices union Select * from medications union Select * from powergenerator union Select * from tools)select * from table1 natural inner join Resources natural inner join Supplies where Supplies.sid = %sorder by type;" % (sid)
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, sname, scity, sphone):
        # Create query to insert a supplier into the DB
        return jsonify("Returns the id of the supplier inserted into the DB")