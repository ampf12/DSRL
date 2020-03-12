'''The main app module takes care to setup the routes for the REST API and 
calling the proper handler objects to process the request.
'''
from flask import Flask, jsonify, request
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


# Supplier
    # info of
    # Place/get resource on Resource table
    # Get resource of supplier with {id}

# Post new supplier or Get supplier info by  (all, id, name/company)
@app.route('/DSLR/suppliers', methods=['GET', 'POST'])
def getAllSuppliers():
    if request.method == 'GET':
        if request.args:
            return SupplierHandler().searchSuppliers(request.args)
        else:
            return SupplierHandler().getAllSuppliers()
    elif request.method == 'POST':
        return SupplierHandler().insertSupplier(request.form)
    else:
        return jsonify(Error = "Method not allowed"), 405


@app.route('/DSLR/suppliers/<int:sid>', methods=['GET'])
def getSupplierById(sid):
    if request.method == 'GET':
        return SupplierHandler().getSupplierById(sid)
    else:
        return jsonify(Error = "Method not allowed"), 405

# Get resources that supplier with id {id} provides
@app.route('/DSLR/suppliers/<int:sid>/resources')
def getResourcesBySuplierId(sid):
    return SupplierHandler().getResourcesBySupplierId(sid)

# Consumer
    # info of
    # Post order in Order table

# Admin
    # TODO




if __name__ == '__main__':
    app.run()
