from flask import request
from flask_restful import Resource
from models.linked_list import LinkedList
from utils.storage import save_json, load_json
import utils.messages as messages

orderList = LinkedList()

class OrdersResource(Resource):
    def post(self):
        data = request.get_json()
        if "id" not in data or "products" not in data:
            return messages.ERROR_MISSING_DATA
        orderList.add_new_node(data["id"], data)
        save_json("orders.json", orderList.list_all())
        return messages.SUCCESS_ORDER_ADDED

    def get(self, id):
        order = orderList.find(id)
        return (order, 200) if order else messages.ERROR_ORDER_NOT_FOUND

    def put(self, id):
        data = request.get_json()
        if orderList.find(id) is None:
            return messages.ERROR_ORDER_NOT_FOUND
        orderList.delete(id)
        orderList.add_new_node(id, data)
        save_json("orders.json", orderList.list_all())
        return messages.SUCCESS_ORDER_UPDATED

    def delete(self, id):
        if orderList.find(id) is None:
            return messages.ERROR_ORDER_NOT_FOUND
        orderList.delete(id)
        save_json("orders.json", orderList.list_all())
        return messages.SUCCESS_ORDER_DELETED

class OrderListResource(Resource):
    def get(self):
        return orderList.list_all(), 200

def load_orders():
    orders = load_json("orders.json")
    for p in orders:
        orderList.add_new_node(p["id"], p)
