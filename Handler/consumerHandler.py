from flask import jsonify
from DAO.consumerDao import ConsumerDAO

class ConsumerHandler:
    def build_consumer_dict(self, row):
        result = {}
        result['cid'] = row[0]
        result['cfirst_name'] = row[1]
        result['clast_name'] = row[2]
        result['cphone'] = row[3]
        result['caddress'] = row[4]
        result['cage'] = row[5]
        return result

    def build_resourceRequest_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rtype'] = row[1]
        result['rquantity'] = row[2]
        result['cid'] = row[3]
        return result

    def build_resourceReservation_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['cid'] = row[1]
        return result

    def getAllConsumers(self):
        # Creates the list of all consumers calling the DAO which creates the query,
        # this returns a list. The list is then jsonified to be used as a response.
        dao = ConsumerDAO()
        # TODO Implemented in later phases
        return dao.getAllConsumers()

    def getConsumerById(self, sid):
        # Creates the list of the consumer with the given ID calling the DAO which creates the query,
        # this returns a list. The list is then jsonified to be used as a response.

        dao = ConsumerDAO()
        # TODO Implemented in later phases
        return dao.getConsumerById(sid)

    def getResourcesByConsumerId(self, sid):
        # Creates the list of the resources the consumer needs calling the DAO which creates the query,
        # this returns a list. The list is then jsonified to be used as a response.

        dao = ConsumerDAO()
        # TODO Implemented in later phases
        return dao.getResourcesByConsumerId(sid)

    def searchConsumers(self, args):
        return "Search by consumer with a specified parameter"

    def insertConsumer(self, form):
        dao = ConsumerDAO()
        sid = dao.insertConsumer('sname', 'scity', 'sphone')
        return sid

    @classmethod
    def makeRequestForResources(self, form):
        dao = ConsumerDAO()
        rid = dao.insertRequest('rid', 'rtype', 'rquantity','cid')
        return rid

    @classmethod
    def makeReservationForResources(self, form):
        dao = ConsumerDAO()
        rid = dao.insertReservation('rid','cid')
        return rid