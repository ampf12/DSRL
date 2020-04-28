import psycopg2
from flask import jsonify

from Config.DbConfig import pg_config


class AdministratorDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host = ec2-52-202-146-43.compute-1.amazonaws.com" % (
            pg_config['dbname'],
            pg_config['user'],
            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllAdministrators(self):
        #Build query selecting all suppliers
        cursor = self.conn.cursor()
        query = "select * from Person natural inner join Administrator;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorById(self, sid):
        # Build query to select a supplier by its ID
        cursor = self.conn.cursor()
        query = "select * from Person natural inner join Administrator where Administrator.aid = %s;" % (sid)
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllConsumers(self):
        #Build query selecting all consumers
        return jsonify("A list of all consumers is returned")

    def getSupplierByID(self, sid):
        #Build a query to select a supplier by its id
        return jsonify("A supplier with a given ID is returned")

    def getConsumerByID(self,cid):
        #Build a query to select a supplier by its id
        return jsonify("A consumer with a given ID is returned")