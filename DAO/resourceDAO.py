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
        query = "select * from Resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByID(self, rid):
        # Build a query to select a resource by its id
        # return jsonify("A resource with a given ID is returned")
        cursor = self.conn.cursor()
        query = "select * from Resources where Resources.rid = %s;" % (rid)
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
