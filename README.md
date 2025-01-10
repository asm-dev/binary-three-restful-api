# RESTful API

Esta aplicación permite el manejo digital del store de una tienda. El sistema utiliza una RESTful API para manejar los datos, que son gestionados con ayuda de un árbol de búsqueda binario, una lista enlazada y técnicas de serialización. Se asegura la persistencia de datos grabándolos en un JSON.

Para probar el BST:

```
bst.insert(10, "Producto A")
bst.insert(30, "Producto A")
bst.insert(2, "Producto A")
bst.insert(14, "Producto A")

bst.print_tree()

print("Buscar clave 10:", bst.search(10))
print("Buscar clave 100:", bst.search(100))
print("Buscar clave 2:", bst.search(2))
```
