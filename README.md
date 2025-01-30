# RESTful API para la gestión de datos de una tienda

Esta aplicación permite el manejo digital del _store_ de una tienda. El sistema utiliza una RESTful API creada con **Flask** para manejar los datos, que son gestionados con ayuda de un árbol de búsqueda binario, una lista enlazada y técnicas de serialización. Se asegura la persistencia de datos grabándolos en un JSON.

El proyecto sigue principios de código limpio. Es decir, legibilidad, simplicidad, modularidad, nombrado claro y consistente, entre otros.

## Instalación y ejecución

1. **Clona** este repositorio en tu máquina local
2. Crea un **entorno virtual**. Recomiento el uso de Anaconda

```sh
conda create -n tienda-api python=3.10
conda activate tienda-api
```

3. Instala las **dependencias**. No son muchas, pero son necesarias, `pip install -r requirements.txt`

```
4. Ejecuta la API `python app/app.py`

> La API estará disponible en `http://127.0.0.1:5000/`

---
## Endpoints disponibles
> Se trata de una API de arquitectura **RESTful**, por lo que todas las **operaciones CRUD** (Crear, leer, actualizar y eliminar) están disponibles.

### **Productos (BST)**
| Método | Endpoint           | Descripción                       |
|--------|--------------------|-----------------------------------|
| POST   | `/products`        | Agregar un producto              |
| GET    | `/products/<id>`   | Obtener un producto por ID       |
| PUT    | `/products/<id>`   | Actualizar un producto por ID    |
| DELETE | `/products/<id>`   | Eliminar un producto por ID      |

### **Pedidos (Lista Enlazada)**
| Método | Endpoint       | Descripción                          |
|--------|---------------|--------------------------------------|
| POST   | `/orders`      | Crear un nuevo pedido               |
| GET    | `/orders/<id>` | Obtener un pedido por ID            |
| PUT    | `/orders/<id>` | Actualizar un pedido existente      |
| DELETE | `/orders/<id>` | Eliminar un pedido                  |
| GET    | `/orders`      | Listar todos los pedidos            |

---
## Decisiones de desarollo

### **¿Por qué Flask?**
Elegí Flask para este proyecto debido a su simplicidad y flexibilidad. A diferencia de Django, que es más pesado y estructurado, Flask permite un control total sobre la arquitectura, lo que es ideal para proyectos más pequeños o cuando se busca un enfoque personalizado sin las restricciones de un framework más grande. En comparación con FastAPI, que es más rápido y optimizado para aplicaciones asincrónicas, Flask sigue siendo adecuado para APIs que no requieren un rendimiento ultra alto o concurrencia compleja

### **Uso de un Árbol Binario de Búsqueda (BST) para la gestión de productos**
- Permite búsquedas eficientes en **O(log n)** en promedio.
- Optimiza la gestión de grandes volúmenes de productos.

Si lo deseas entender mejor su funcionamiento, puedes probarlo separadamente:

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

### **Uso de Lista Enlazada para los pedidos**
- Permite fácil adición y eliminación de pedidos sin necesidad de redimensionar estructuras.
- Se adapta bien a sistemas donde los pedidos se gestionan en **orden de llegada**, como es el caso que nos ocupa: una tienda online.

---
## Cómo probar la API
### Usando Postman o Bruno
1. Instalar [Postman](https://www.postman.com/) o [Bruno](https://www.usebruno.com/).
2. Crear una nueva petición con la URL `http://127.0.0.1:5000/products`.
3. Enviar diferentes solicitudes (`POST`, `GET`, `PUT`, `DELETE`).

### Construir y ejecutar el contenedor Docker
```sh
docker build -t tienda-api .
docker run -p 5000:5000 tienda-api
````
