import requests

BASE_URL = "http://127.0.0.1:5000"

def test_create_product():
    response = requests.post(f"{BASE_URL}/products", json={"id": 1, "name": "Laptop", "price": 1200})
    assert response.status_code == 201
    assert response.json()["mensaje"] == "Producto agregado"

def test_get_product():
    response = requests.get(f"{BASE_URL}/products/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Laptop"

def test_update_product():
    response = requests.put(f"{BASE_URL}/products/1", json={"id": 1, "name": "Laptop Pro", "price": 1500})
    assert response.status_code == 200
    assert response.json()["mensaje"] == "Producto actualizado"

def test_delete_product():
    response = requests.delete(f"{BASE_URL}/products/1")
    assert response.status_code == 200
    assert response.json()["mensaje"] == "Producto eliminado"

def test_create_order():
    response = requests.post(f"{BASE_URL}/orders", json={
        "id": 101,
        "products": [
            {"id": 1, "name": "Laptop", "price": 1200},
            {"id": 2, "name": "Mouse", "price": 50}
        ]
    })
    assert response.status_code == 201
    assert response.json()["mensaje"] == "Pedido agregado"

def test_get_order():
    response = requests.get(f"{BASE_URL}/orders/101")
    assert response.status_code == 200
    assert "products" in response.json()

def test_update_order():
    response = requests.put(f"{BASE_URL}/orders/101", json={
        "id": 101,
        "products": [
            {"id": 1, "name": "Laptop Pro", "price": 1500},
            {"id": 2, "name": "Mouse", "price": 50}
        ]
    })
    assert response.status_code == 200
    assert response.json()["mensaje"] == "Pedido actualizado"

def test_delete_order():
    response = requests.delete(f"{BASE_URL}/orders/101")
    assert response.status_code == 200
    assert response.json()["mensaje"] == "Pedido eliminado"

def test_list_orders():
    response = requests.get(f"{BASE_URL}/orders")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
