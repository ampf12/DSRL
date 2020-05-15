import psycopg2
from flask import jsonify

from Config.DbConfig import pg_config


class AdministratorDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host = %s" % (
            pg_config['dbname'],
            pg_config['user'],
            pg_config['passwd'],
            pg_config['host']
        )
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

    def insert(self, pfirst_name, plast_name, pphone_number):
        # Create query to insert a supplier into the DB
        cursor = self.conn.cursor()
        query = "insert into person(pfirst_name, plast_name, pphone_number) values (%s, %s, %s) returning pid;"
        cursor.execute(query, (pfirst_name, plast_name, pphone_number,))
        pid = cursor.fetchone()[0]
        cursor1 = self.conn.cursor()
        query1 = "insert into administrator(pid) values (%s) returning aid;"
        cursor1.execute(query1, ( pid,))
        aid = cursor1.fetchone()[0]
        self.conn.commit()
        return aid