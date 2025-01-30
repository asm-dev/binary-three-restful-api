from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from binary_search_tree import BinarySearchTree
from linked_list import LinkedList
import json

app = Flask(__name__)
api = Api(app)

bst = BinarySearchTree()
orderList = LinkedList()

# ====== API endpoints ======

class ProductResource(Resource):
    def post(self):
        data = request.get_json()        
        if "id" not in data or "name" not in data:
            return {"error": "Faltan datos"}, 400
        bst.insert(data["id"], data)
        save_products()
        return {"mensaje": "Producto agregado"}, 201

    def get(self, id):
        product = bst.search(id)
        if product:
            return product, 200
        return {"error": "Producto no encontrado"}, 404

    def put(self, id):
        data = request.get_json()
        if bst.search(id) is None:
            return {"error": "Producto no encontrado"}, 404
        bst.delete(id)
        bst.insert(id, data)
        save_products()
        return {"mensaje": "Producto actualizado"}, 200

    def delete(self, id):
        if bst.search(id) is None:
            return {"error": "Producto no encontrado"}, 404
        bst.delete(id)
        save_products()
        return {"mensaje": "Producto eliminado"}, 200

class OrdersResource(Resource):
    def post(self):
        data = request.get_json()
        if "id" not in data or "products" not in data:
            return {"error": "Faltan datos"}, 400
        orderList.add_new_node(data["id"], data)
        save_orders()
        return {"mensaje": "Pedido agregado"}, 201

    def get(self, id):
        order = orderList.find(id)
        if order:
            return order, 200
        return {"error": "Pedido no encontrado"}, 404

    def put(self, id):
        data = request.get_json()
        if orderList.find(id) is None:
            return {"error": "Pedido no encontrado"}, 404
        orderList.delete(id)
        orderList.add_new_node(id, data)
        save_orders()
        return {"mensaje": "Pedido actualizado"}, 200

    def delete(self, id):
        if orderList.find(id) is None:
            return {"error": "Pedido no encontrado"}, 404
        orderList.delete(id)
        save_orders()
        return {"mensaje": "Pedido eliminado"}, 200

class OrderListResource(Resource):
    def get(self):
        return orderList.list_all(), 200

# ====== JSON serialisation and deserialisation ======

def save_products():
    with open("products.json", "w") as f:
        products = []
        
        def inorder_traverse_tree(nodo):
            if nodo:
                inorder_traverse_tree(nodo.left)
                products.append(nodo.value)
                inorder_traverse_tree(nodo.right)

        inorder_traverse_tree(bst.root)
        json.dump(products, f, indent=4)

def load_products():
    try:
        with open("products.json", "r") as f:
            products = json.load(f)
            for p in products:
                bst.insert(p["id"], p)
    except FileNotFoundError:
        pass

def save_orders():
    with open("orders.json", "w") as f:
        json.dump(orderList.list_all(), f)

def load_orders():
    try:
        with open("orders.json", "r") as f:
            orders_json = json.load(f)
            for p in orders_json:
                orderList.add_new_node(p["id"], p)
    except FileNotFoundError:
        pass

# ====== API routes ======

api.add_resource(ProductResource, "/products", "/products/<int:id>")
api.add_resource(OrdersResource, "/orders", "/orders/<int:id>")
api.add_resource(OrderListResource, "/orders")

# Load data on init
load_products()
load_orders()

if __name__ == "__main__":
    app.run(debug=True)