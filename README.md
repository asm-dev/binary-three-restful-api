# RESTful API para la gestión de datos de una tienda

Esta aplicación permite el manejo digital del _store_ de una tienda. El sistema utiliza una RESTful API creada con **Flask** para manejar los datos, que son gestionados con ayuda de un árbol de búsqueda binario, una lista enlazada y técnicas de serialización. Se asegura la persistencia de datos grabándolos en un JSON.

El proyecto sigue principios de código limpio. Es decir, legibilidad, simplicidad, modularidad, nombrado claro y consistente, entre otros.

&nbsp;

## Instalación y ejecución

1. **Clona** este repositorio en tu máquina local
2. Crea un **entorno virtual**. Recomiento el uso de Anaconda

```
conda create -n tienda-api python=3.10
conda activate tienda-api
```

3. Instala las **dependencias**. No son muchas, pero son necesarias, `pip install -r requirements.txt`
4. Ejecuta la API con `python -m app.app` o `python app/app.py`. La API estará disponible en `http://127.0.0.1:5000/`

Alternativamente, puedes crear un contenedor **Docker** para ejecutar la aplicación:

```
docker build -t tienda-online-app .
docker run -d -p 5000:5000 --name online-shop-container tienda-online-app
````

&nbsp;

## Endpoints disponibles
> Se trata de una API de arquitectura **RESTful**, por lo que todas las **operaciones CRUD** (Crear, leer, actualizar y eliminar) están disponibles.

#### Productos (BST)
| Método | Endpoint           | Descripción                       |
|--------|--------------------|-----------------------------------|
| POST   | `/products`        | Agregar un producto              |
| GET    | `/products/<id>`   | Obtener un producto por ID       |
| PUT    | `/products/<id>`   | Actualizar un producto por ID    |
| DELETE | `/products/<id>`   | Eliminar un producto por ID      |

#### Pedidos (Lista Enlazada)
| Método | Endpoint       | Descripción                          |
|--------|---------------|--------------------------------------|
| POST   | `/orders`      | Crear un nuevo pedido               |
| GET    | `/orders/<id>` | Obtener un pedido por ID            |
| PUT    | `/orders/<id>` | Actualizar un pedido existente      |
| DELETE | `/orders/<id>` | Eliminar un pedido                  |
| GET    | `/orders`      | Listar todos los pedidos            |


&nbsp;

## Decisiones de desarollo

### **¿Por qué Flask?**
Elegí Flask para este proyecto debido a su simplicidad y flexibilidad. A diferencia de Django, que es más pesado y estructurado, Flask permite un control total sobre la arquitectura, lo que es ideal para proyectos más pequeños o cuando se busca un enfoque personalizado sin las restricciones de un framework más grande. En comparación con FastAPI, que es más rápido y optimizado para aplicaciones asincrónicas, Flask sigue siendo adecuado para APIs que no requieren un rendimiento ultra alto o concurrencia compleja

### **Uso de un Árbol Binario de Búsqueda (BST) para la gestión de productos**
- Permite búsquedas eficientes en **O(log n)** en promedio.
- Optimiza la gestión de grandes volúmenes de productos.

Si deseas entender mejor su funcionamiento, puedes probarlo separadamente:

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
- Permite agregar y eliminar pedidos con mucha facilidad y rapidez ya que no hay necesidad de redimensionar estructuras.
- Las *linked list* se adaptan bien a sistemas donde los pedidos se gestionan en **orden de llegada**, como es el caso que nos ocupa: una tienda online.

&nbsp;

## Pruebas de uso

Además de probar la API con tests (`pytest test/api_endpoints_spec.py`) he realizado varias pruebas de uso utilizando Postman/Bruno

Prueba | Captura
:------:|:-------:
*Agregamos un pedido* |
*Eliminamos un producto* |
*Mostramos todos los pedidos* |

