from flask_restful import Api
from flask import Flask
from resources.products import ProductResource
from resources.orders import OrdersResource, OrderListResource

app = Flask(__name__)
api = Api(app)

api.add_resource(ProductResource, "/products", "/products/<int:id>")
api.add_resource(OrdersResource, "/orders", "/orders/<int:id>")
api.add_resource(OrderListResource, "/orders")

def create_app():
    return app
