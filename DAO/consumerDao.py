from flask import jsonify


class ConsumerDAO:

    def getAllConsumers(self):
        # Build query selecting all consumers
        return jsonify("A list of all consumers is returned")

    def getConsumerById(self, sid):
        # Build query to select a consumer by its ID
        return jsonify("A consumer with a given ID is returned")

    def getResourcesByConsumerId(self, sid):
        # Create query to select all info resources that a supplier with a given ID has
        return jsonify("A list of resources needed by a consumer with the given ID is returned")

    def insertConsumer(self, sname, scity, sphone):
        # Create query to insert a supplier into the DB
        return jsonify("Returns the id of the consumer inserted into the DB")

    def insertRequest(self, rid, rtype, rquantity,cid):
        # Create query to insert a request for a resource into the DB
        return jsonify("Returns the id of the request inserted into the DB")