from flask import request
from flask_restful import Resource
from binary_search_tree import BinarySearchTree
from storage import save_json, load_json
import messages

bst = BinarySearchTree()

class ProductResource(Resource):
    def post(self):
        data = request.get_json()
        if "id" not in data or "name" not in data:
            return messages.ERROR_MISSING_DATA
        bst.insert(data["id"], data)
        save_json("products.json", bst.to_list())
        return messages.SUCCESS_PRODUCT_ADDED

    def get(self, id):
        product = bst.search(id)
        return (product, 200) if product else messages.ERROR_PRODUCT_NOT_FOUND

    def put(self, id):
        data = request.get_json()
        if bst.search(id) is None:
            return messages.ERROR_PRODUCT_NOT_FOUND
        bst.delete(id)
        bst.insert(id, data)
        save_json("products.json", bst.to_list())
        return messages.SUCCESS_PRODUCT_UPDATED

    def delete(self, id):
        if bst.search(id) is None:
            return messages.ERROR_PRODUCT_NOT_FOUND
        bst.delete(id)
        save_json("products.json", bst.to_list())
        return messages.SUCCESS_PRODUCT_DELETED

def load_products():
    products = load_json("products.json")
    for p in products:
        bst.insert(p["id"], p)
