from flask import Flask
from flask_restful import Api
from resources import ProductResource, OrdersResource

def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(ProductResource, "/products", "/products/<int:id>")
    api.add_resource(OrdersResource, "/orders", "/orders/<int:id>")

    return app
