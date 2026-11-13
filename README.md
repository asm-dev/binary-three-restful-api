# RESTful API for managing a store's data

This application enables digital management of a shop's _store_. The system uses a RESTful API built with **Flask** to handle the data, which is managed with the help of a binary search tree, a linked list and serialization techniques. Data persistence is ensured by saving it to a JSON file.

The project follows clean code principles. That is: readability, simplicity, modularity, clear and consistent naming, among others.

&nbsp;

## Installation and execution

1. **Clone** this repository to your local machine
2. Create a **virtual environment**. I recommend using Anaconda

```
conda create -n tienda-api python=3.10
conda activate tienda-api
```

3. Install the **dependencies**. There aren't many, but they are necessary, `pip install -r requirements.txt`
4. Run the API with `python -m app.app` or `python app/app.py`. The API will be available at `http://127.0.0.1:5000/`

Alternatively, you can create a **Docker** container to run the application:

```
docker build -t tienda-online-app .
docker run -d -p 5000:5000 --name online-shop-container tienda-online-app
````

&nbsp;

## Available endpoints
> This is a **RESTful** architecture API, so all **CRUD operations** (Create, Read, Update and Delete) are available.

#### Products (BST)
| Method | Endpoint           | Description                       |
|--------|--------------------|-----------------------------------|
| POST   | `/products`        | Add a product                    |
| GET    | `/products/<id>`   | Get a product by ID              |
| PUT    | `/products/<id>`   | Update a product by ID           |
| DELETE | `/products/<id>`   | Delete a product by ID           |

#### Orders (Linked List)
| Method | Endpoint       | Description                          |
|--------|---------------|--------------------------------------|
| POST   | `/orders`      | Create a new order                  |
| GET    | `/orders/<id>` | Get an order by ID                  |
| PUT    | `/orders/<id>` | Update an existing order            |
| DELETE | `/orders/<id>` | Delete an order                     |
| GET    | `/orders`      | List all orders                     |


&nbsp;

## Development decisions

### **Why Flask?**
I chose Flask for this project because of its simplicity and flexibility. Unlike Django, which is heavier and more structured, Flask allows full control over the architecture, which is ideal for smaller projects or when a customized approach is wanted without the restrictions of a larger framework. Compared with FastAPI, which is faster and optimized for asynchronous applications, Flask remains suitable for APIs that do not require ultra-high performance or complex concurrency

### **Using a Binary Search Tree (BST) for product management**
- Allows efficient searches in **O(log n)** on average.
- Optimizes the management of large volumes of products.

If you want to better understand how it works, you can try it on its own:

```
bst = BinarySearchTree()

bst.insert(10, "Producto A")
bst.insert(30, "Producto A")
bst.insert(2, "Producto A")
bst.insert(14, "Producto A")

bst.print_tree()

print("Buscar clave 10:", bst.search(10))
print("Buscar clave 100:", bst.search(100))
print("Buscar clave 2:", bst.search(2))
````

### **Using a Linked List for orders**
- Makes it very easy and fast to add and remove orders since there is no need to resize structures.
- *Linked lists* fit well in systems where orders are handled in **order of arrival**, as in the case at hand: an online store.

&nbsp;

## Usage tests

Besides testing the API with tests (`pytest test/api_endpoints_spec.py`), I have run several usage tests using Postman and Bruno.

Test | Screenshot
:------:|:-------:
*We add an order* | ![image](https://github.com/user-attachments/assets/f2ae755b-4796-4353-96e6-e2a375e2f8ab)
*We delete a product* | ![image](https://github.com/user-attachments/assets/e55e30d5-a24e-4916-a93e-77da4324f904)
*We show all orders* | ![image](https://github.com/user-attachments/assets/ade35ced-2115-43dd-a573-c764e6898aa8)


