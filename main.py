'''The main app module takes care to setup the routes for the REST API and 
calling the proper handler objects to process the request.
'''
from flask import Flask, jsonify, request

from Handler.administratorHandler import AdministratorHandler
from Handler.consumerHandler import ConsumerHandler
from Handler.ordersHandler import OrdersHandler
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
@app.route('/DSRL/suppliers', methods=['GET', 'POST'])
def getAllSuppliers():
    if request.method == 'GET':
        if request.args:
            return SupplierHandler().searchSuppliers(request.args)
        else:
            return SupplierHandler().getAllSuppliers()
    elif request.method == 'POST':
        return SupplierHandler().insertSupplier(request.form)
    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/DSRL/suppliers/<int:sid>', methods=['GET'])
def getSupplierById(sid):
    if request.method == 'GET':
        return SupplierHandler().getSupplierById(sid)
    else:
        return jsonify(Error="Method not allowed"), 405


# Get resources that supplier with id {id} provides
@app.route('/DSRL/suppliers/<int:sid>/resources', methods=['GET'])
def getResourcesBySupplierId(sid):
    if request.method == 'GET':
        return SupplierHandler().getResourcesBySupplierId(sid)
    else:
        return jsonify(Error="Method not allowed"), 405

# TODO
# Get request
# Get reservation ?

#################################################### Consumers ######################################
# Post order in Order table


@app.route('/DSRL/consumer', methods=['GET', 'POST'])
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


@app.route('/DSRL/consumer/<int:cid>', methods=['GET'])
def getConsumerById(cid):
    if request.method == 'GET':
        return ConsumerHandler().getConsumerById(cid)
    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/DSRL/consumer/<int:cid>/orders', methods=['GET'])
def getOrdersByConsumerId(cid):
    if request.method == 'GET':
        return ConsumerHandler().getOrdersByConsumerId(cid)
    else:
        return jsonify(Error="Method not allowed"), 405


################################# Admin ####################################################

@app.route('/DSRL/administrators', methods=['GET', 'POST'])
def getAllAdministratorsrs():
    if request.method == 'GET':
        if request.args:
            return AdministratorHandler().getAllAdministrators(request.args)
        else:
            return AdministratorHandler().getAllAdministrators()
    elif request.method == 'POST':
        return AdministratorHandler().insertAdministrator(request.form)
    else:
        return jsonify(Error="Method not allowed"), 405

@app.route('/DSRL/administrators/<int:sid>', methods=['GET'])
def getAdministratorById(sid):
    if request.method == 'GET':
        return AdministratorHandler().getAdministratorById(sid)
    else:
        return jsonify(Error="Method not allowed"), 405


##################  Resources  #########################################
@app.route('/DSRL/resources', methods=['GET'])
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


@app.route('/DSRL/resources/<int:rid>', methods=['GET'])
def getResourceById(rid):
    if request.method == 'GET':
        return ResourceHandler().getResourceById(rid)
    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/DSRL/resources/suppliers/<int:sid>', methods=['GET']) 
def getResourceBySupplierId(sid):
    if request.method == 'GET':
        return ResourceHandler().getResourceBySupplierId(sid)
    else:
        return jsonify(Error="Method not allowed"), 405


############################### Orders  ##########################################
@app.route('/DSRL/orders', methods=['GET'])
def getAllOrders():
    if request.method == 'GET':
        if request.args:
            return OrdersHandler().searchOrders(request.args)
        else:
            return OrdersHandler().getAllOrders()
    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/DSRL/orders/<int:oid>', methods=['GET'])
def getOrderById(oid):
    if request.method == 'GET':
        return OrdersHandler().getOrderById(oid)
    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/DSRL/orders/consumer/<int:cid>', methods=['GET'])
def getOrderByConsumerId(cid):
    if request.method == 'GET':
        return ConsumerHandler().getOrdersByConsumerId(cid)
    else:
        return jsonify(Error="Method not allowed"), 405




if __name__ == '__main__':
    app.run()
