

class SupplierDAO:

    def getAllSuppliers(self):
        # Build query selecting all suppliers
        return "A list of all suppliers is returned"

    def getSupplierById(self, sid):
        # Build query to select a supplier by its ID
        return "A supplier with a given ID is returned"

    def getResourcesBySupplierId(self, sid):
        # Create query to select all info resources that a supplier with a given ID has
        return "A list of resources the supplier with given ID has is returned"

    def insert(self, sname, scity, sphone):
        # Create query to insert a supplier into the DB
        return "Returns the id of the supplier inserted into the DB"