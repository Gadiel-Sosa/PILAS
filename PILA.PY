class Pila:
    def __init__(self):
        self.items = []


    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "La pila está vacía"


    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "La pila está vacía"


    def mostrar(self):
        return self.items



pila = Pila()


pila.push(1)  
pila.push(2)  
pila.push(3)  
print("Elementos en la pila:", pila.mostrar())  
print("Tope de la pila:", pila.peek())           

print("Desapilando:", pila.pop())                 
print("Elementos en la pila después de desapilar:", pila.mostrar())  

print("Desapilando:", pila.pop())                 
print("Desapilando:", pila.pop())                 
print("Desapilando:", pila.pop())                 