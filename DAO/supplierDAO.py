from flask import jsonify
import psycopg2
from Config.DbConfig import pg_config

class SupplierDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host = %s" % (
        pg_config['dbname'],
        pg_config['user'],
        pg_config['passwd'],
        pg_config['host']
       )
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

    def insert(self, pfirst_name, plast_name ,scompany_name ,pphone_number):
        # Create query to insert a supplier into the DB
        cursor = self.conn.cursor()
        query = "insert into person(pfirst_name, plast_name, pphone_number) values (%s, %s, %s) returning pid;"
        cursor.execute(query, (pfirst_name, plast_name,pphone_number,))
        pid1 = cursor.fetchone()[0]
        cursor1 = self.conn.cursor()
        query1 = "insert into supplier(scompany_name,pid) values (%s,%s) returning sid;"
        cursor1.execute(query1, (scompany_name,pid1,))
        sid = cursor1.fetchone()[0]
        self.conn.commit()
        return sid

