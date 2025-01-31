from app.routes import create_app
from resources import load_products, load_orders

app = create_app()

load_products()
load_orders()

if __name__ == "__main__":
    app.run(debug=True)
