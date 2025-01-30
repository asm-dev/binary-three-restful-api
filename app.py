from flask import Flask
from flask_restful import Api
from products import ProductResource, load_products
from orders import OrdersResource, OrderListResource, load_orders

app = Flask(__name__)
api = Api(app)

api.add_resource(ProductResource, "/products", "/products/<int:id>")
api.add_resource(OrdersResource, "/orders", "/orders/<int:id>")
api.add_resource(OrderListResource, "/orders")

load_products()
load_orders()

if __name__ == "__main__":
    app.run(debug=True)
