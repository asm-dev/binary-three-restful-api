class Node:
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_new_node(self, id, data):
        new_node = Node(id, data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find(self, id):
        current = self.head
        while current:
            if current.id == id:
                return current.data
            current = current.next
        return None

    def delete(self, id):
        if self.head is None:
            return
        if self.head.id == id:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.id == id:
                current.next = current.next.next
                return
            current = current.next

    def list_all(self):
        orderList = []
        current = self.head
        while current:
            orderList.append({"id": current.id, "data": current.data})
            current = current.next
        return orderList
