from flask import jsonify
import psycopg2
from Config.DbConfig import pg_config


class ResourceDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host = ec2-52-202-146-43.compute-1.amazonaws.com" % (
        pg_config['dbname'],
        pg_config['user'],
        pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllResources(self):
        # Build query for selecting all resources
        # return jsonify("A list of all resources is returned")
        cursor = self.conn.cursor()
        query = "with table1 as (Select * from water union Select * from babyfood union Select * from clothing union Select * from batteries union Select * from cannedfood union Select * from dryfood union Select * from fuel union Select * from heavyequipment union Select * from ice union Select * from medicaldevices union Select * from medications union Select * from powergenerator union Select * from tools)select * from table1 natural inner join Resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllSpecificResources(self, rtype):
        # Build query for selecting all resources
        # return jsonify("A list of all resources is returned")
        cursor = self.conn.cursor()
        query = "select * from Resources natural inner join %s order by type;" %(rtype)
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByID(self, rid):
        # Build a query to select a resource by its id
        # return jsonify("A resource with a given ID is returned")
        cursor = self.conn.cursor()
        query = "with table1 as (Select * from water union Select * from babyfood union Select * from clothing union Select * from batteries union Select * from cannedfood union Select * from dryfood union Select * from fuel union Select * from heavyequipment union Select * from ice union Select * from medicaldevices union Select * from medications union Select * from powergenerator union Select * from tools)select * from table1 natural inner join Resources where rid=%s;" %(rid)
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSpecificResourceByID(self, rid,rtype):
        # Build a query to select a resource by its id
        # return jsonify("A resource with a given ID is returned")
        cursor = self.conn.cursor()
        query = "select * from Resources natural inner join %s where tid = %s;" % (rtype,rid)
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceBySupplierId(self, sid):
        # Create query to select all info resources that a supplier with a given ID has
        # return jsonify("A list of resources for the supplier with given ID is returned")
        cursor = self.conn.cursor()
        query = "select * from Resources natural inner join Supplier where Supplier.sid = %s;" % (sid)
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    def getResourceByKeyword(self,Keyword):
        # Build query for selecting all resources
        # return jsonify("A list of all resources is returned")
        cursor = self.conn.cursor()
        query = "with table1 as (Select * from water union Select * from babyfood union Select * from clothing union Select * from batteries union Select * from cannedfood union Select * from dryfood union Select * from fuel union Select * from heavyequipment union Select * from ice union Select * from medicaldevices union Select * from medications union Select * from powergenerator union Select * from tools)select * from table1 natural inner join Resources where type ~ '%s';" % (Keyword)
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result