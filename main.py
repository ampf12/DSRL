'''The main app module takes care to setup the routes for the REST API and 
calling the proper handler objects to process the request.
'''
from flask import Flask, jsonify, request

from Handler.administratorHandler import AdministratorHandler
from Handler.consumerHandler import ConsumerHandler
from Handler.orderHandler import OrderHandler
from Handler.resourceHandler import ResourceHandler
from Handler.supplierHandler import SupplierHandler

# Import Cross-Origin Resource Sharing to enable
# services on other ports on this machine or on other
# machines to access this app
from flask_cors import CORS, cross_origin

app = Flask(__name__)

# Apply CORS to this app
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World! This is the Disaster Resource Locator app.'


############################### Supplier ###############################################
# info of
# Place/get resource on Resource table
# Get resource of supplier with {id}

# Post new supplier or Get supplier info by  (all, id, name/company)
@app.route('/DSLR/suppliers', methods=['GET', 'POST'])
def getAllSuppliers():
    if request.method == 'GET':
        if request.args:
            return SupplierHandler().searchSuppliers(request.args)  # TODO jsonify
        else:
            return SupplierHandler().getAllSuppliers()
    elif request.method == 'POST':
        return SupplierHandler().insertSupplier(request.form)
    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/DSLR/suppliers/<int:sid>', methods=['GET'])
def getSupplierById(sid):
    if request.method == 'GET':
        return SupplierHandler().getSupplierById(sid)
    else:
        return jsonify(Error="Method not allowed"), 405


# Get resources that supplier with id {id} provides
@app.route('/DSLR/suppliers/<int:sid>/resources')
def getResourcesBySuplierId(sid):
    return SupplierHandler().getResourcesBySupplierId(sid)

# TODO
# Get request
# Get reservation ?


#################################################### Consumers ######################################
# info of
# Post order in Order table
@app.route('/DSLR/consumers', methods=['GET', 'POST'])
def getAllConsumers():
    if request.method == 'GET':
        if request.args:
            return ConsumerHandler().searchConsumers(request.args)
        else:
            return ConsumerHandler().getAllConsumers()
    elif request.method == 'POST':
        return ConsumerHandler().insertConsumer(request.form)
    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/DSLR/consumers/<int:sid>', methods=['GET'])
def getConsumerById(sid):
    if request.method == 'GET':
        return ConsumerHandler().getConsumerById(sid)
    else:
        return jsonify(Error="Method not allowed"), 405

    # Get resources that consumer with id {id} provides


@app.route('/DSLR/consumers/<int:sid>/resources')
def getResourcesByConsumerId(sid):
    return ConsumerHandler().getResourcesByConsumerId(sid)


#
@app.route('/DSLR/consumers/request', methods=['POST'])
def makeRequestForResource():
    if request.method == "POST":
        return ConsumerHandler.makeRequestForResources(request.form)
    else:
        return jsonify(Error="Method not allowed")


@app.route('/DSLR/consumers/reservation', methods=['POST'])
def makeReservationForResource():
    if request.method == "POST":
        return ConsumerHandler.makeReservationForResources(request.form)
    else:
        return jsonify(Error="Method not allowed")


################################# Admin ####################################################

@app.route('/DSLR/admin/suppliers', methods=['GET', 'POST'])
def adminGetAllSuppliers():
    return getAllSuppliers()


@app.route('/DSLR/admin/consumers', methods=['GET', 'POST'])
def adminGetAllConsumers():
    return getAllConsumers()


@app.route('/DSLR/admin/suppliers/<int:sid>', methods=['GET'])
def adminGetSupplierById(sid):
    return getSupplierById(sid)


@app.route('/DSLR/admin/consumers/<int:cid>', methods=['GET'])
def adminGetConsumerById(cid):
    return getConsumerById(cid)


##################  Resources  #########################################
@app.route('/DSLR/resources', methods=['GET'])
def getAllResources():
    if request.method == 'GET':
        if request.args:
            return ResourceHandler().searchResource(request.args)
        else:
            return ResourceHandler().getAllResources()
    elif request.method == 'POST':
        return ResourceHandler().insertResource(request.form)
    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/DSLR/resources/<int:rid>', methods=['GET']) #TODO post(?)
def getResourceById(rid):
    if request.method == 'GET':
        return ResourceHandler().getResourceById(rid)
    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/DSLR/resources/suppliers/<int:sid>', methods=['GET']) #TODO post(?)
def getResourceBySupplierId(sid):
    if request.method == 'GET':
        return ResourceHandler().getResourceBySupplierId(sid)
    else:
        return jsonify(Error="Method not allowed"), 405


############################### Orders  ##########################################
@app.route('/DSLR/orders', methods=['GET'])
def getAllOrders():
    if request.method == 'GET':
        if request.args:
            return OrderHandler().searchOrder(request.args)
        else:
            return OrderHandler().getAllOrders()
    elif request.method == 'POST':
        return OrderHandler().insertOrder(request.form)
    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/DSLR/orders/<int:oid>', methods=['GET'])
def getOrderById(oid):
    if request.method == 'GET':
        return OrderHandler().getOrderById(oid)
    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/DSLR/orders/resources/<int:rid>', methods=['GET'])
def getOrderByResourceId(rid):
    if request.method == 'GET':
        return OrderHandler().getOrderByResourceId(rid)
    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/DSLR/orders/suppliers/<int:sid>', methods=['GET'])
def getOrderBySupplierId(sid):
    if request.method == 'GET':
        return OrderHandler().getOrderBySupplierId(sid)
    else:
        return jsonify(Error="Method not allowed"), 405


if __name__ == '__main__':
    app.run()
