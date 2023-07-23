import tkinter as tk

class Stack:
    
   
def __init__(self):
        self.items = []

    
        self.items = []

   

        self.items = []

def is_empty(self):
        return len(self.items) == 0

    

   


def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        
       
else:
            return None

    def peek(self):
        
       
if not self.is_empty():
            return self.items[-1]
        else:
            
           
return None

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    
        self.items = []

def peek_element(self, element):
        return element in self.items

    

def search(self, item):
        return self.items.index(item) if item in self.items else None

    def check_balance(self, expression):
        stack = []
        brackets = {
        stack = []
')': '(', '}': '{', ']': '['}

        for char in expression:
            if char in '({[':
                stack.append(char)
            
                stack.append(char)

                stack.append(char
elif char in ')}]':
                if not stack or stack[-1] != brackets[char]:
                    return False
                stack.pop()

        
                stack.pop()

       

                stack.pop()


               
return len(stack) == 0

    

def to_list(self):
        return self.items

    

   


def invert_stack(self):
        self.items = self.items[::-
        self.items = self.items[::-
1]

def push_element():
    element = entry_element.get()
    
    element = entry_element

   
if element:
        stack.push(element)
        update_stack()


        stack.push(element)
        update_stack

        stack.push(element)
       

        stack.push(element)

        stack.push
def pop_element():
    stack.pop()
    update_stack()

def peek_element():
    element = stack.peek()
    
    element = stack.peek()
   

    element = stack.peek()

    element =
if element:
        label_result.config(text=
        label_result.config(text=f

        label_result
f"Elemento en el tope de la pila: {element}")
    else:
        label_result.config(text=
        label_result.config
"La pila está vacía.")

def is_empty():
    
   
if stack.is_empty():
        label_result.config(text=
        label_result.config(text

        label_result
"La pila está vacía.")
    
   
else:
        label_result.config(text=
        label_result.config
"La pila no está vacía.")

def size_stack():
    label_result.config(text=
    label_result.config

    label_result

    label

   
f"Tamaño de la pila: {stack.size()}")

def clear_stack():
    stack.clear()
    update_stack()


    stack.clear()
    update

    stack.clear()
   

    stack.clear()
def peek_specific_element():
    element = entry_element.get()
    
    element = entry_element.get

    element = entry
if element:
        if stack.peek_element(element):
            label_result.config(text=
            label_result.config

            label
f"El elemento {element} está en la pila.")
        else:
            label_result.config(text=
            label_result.config
f"El elemento {element} no está en la pila.")

def search_element():
    element = entry_element.get()
    index = stack.search(element)
    
    element = entry_element.get()
    index = stack.search(element)
   

    element = entry_element.get()
    index = stack.search

    element = entry_element.get()
   

    element = entry
if index is not None:
        label_result.config(text=
        label_result
f"El elemento {element} se encuentra en el índice {index}.")
    else:
        label_result.config(text=
        label_result.config(text
f"El elemento {element} no está en la pila.")

def check_balance_expression():
    expression = entry_expression.get()
    
    expression = entry_expression

    expression
if stack.check_balance(expression):
        label_result.config(text=
        label
"La expresión está correctamente balanceada.")
    else:
        label_result.config(text=
        label_result
"La expresión no está correctamente balanceada.")

def invert_stack():
    stack.invert_stack()
    update_stack()


    stack.invert_stack()
    update_stack

    stack.invert_stack()
   

    stack.invert

   
def update_stack():
    stack_list = stack.to_list()
    listbox.delete(
    stack_list = stack.to_list()
    listbox.delete(

    stack_list = stack.to_list()
   

    stack_list = stack.to_list()

    stack_list = stack.to

    stack
0, tk.END)
    for element in stack_list[::-1]:
        listbox.insert(tk.END, element)


        listbox.insert(tk.END

        listbox.insert
# Crear la ventana principal
ventana = tk.Tk()
ventana.title(
ventana = tk.Tk()
vent

ventana = tk.T

vent
"Algoritmo de Pilas")
ventana.geometry("500x500")

# Crear pila
stack = Stack()

# Etiquetas y campos de entrada
label_stack = tk.Label(ventana, text=
label_stack = tk.Label(ventana

label_stack = tk.Label(

label_stack = tk.Label

label
"Pila:")
label_stack.pack()

listbox = tk.Listbox(ventana)
listbox.pack()

label_element = tk.Label(ventana, text=
label_stack.pack()

listbox = tk.Listbox(ventana)
listbox.pack()

label_element = tk.Label(ventana,

label_stack.pack()

listbox = tk.Listbox(ventana)
listbox.pack()

label_element = tk.Label(ventana

label_stack.pack()

listbox = tk.Listbox(ventana)
listbox.pack()

label_element = tk.Label(vent

label_stack.pack()

listbox = tk.Listbox(ventana)
listbox.pack()

label_element

label_stack.pack()

listbox = tk.Listbox(ventana)

label_stack.pack()

listbox = tk.Listbox(vent

label_stack.pack()

listbox = tk

label_stack.pack()


label_stack
"Ingrese el elemento:")
label_element.pack()

entry_element = tk.Entry(ventana)
entry_element.pack()

label_expression = tk.Label(ventana, text=
label_element.pack()

entry_element = tk.Entry(ventana)
entry_element.pack()

label_expression = tk.Label(vent

label_element.pack()

entry_element = tk.Entry(ventana)
entry_element.pack()

label

label_element.pack()

entry_element = tk.Entry(ventana)

label_element.pack()

entry_element = tk.Entry(

label_element.pack()

entry_element =

label_element.pack()

"Ingrese la expresión:")
label_expression.pack()

entry_expression = tk.Entry(ventana)
entry_expression.pack()


label_expression.pack()

entry_expression = tk.Entry(ventana)
entry_expression

label_expression.pack()

entry_expression = tk.Entry(ventana)

label_expression.pack()

entry_expression = tk.Entry(vent

label_expression.pack()

entry_expression = tk

label_expression.pack
# Botones
boton_push = tk.Button(ventana, text=
boton_push = tk.Button(ventana, text

boton_push = tk.Button(vent

boton_push = tk.Button(

boton_push =
"Push", command=push_element)
boton_push.pack()

boton_pop = tk.Button(ventana, text=
boton_push.pack()

boton_pop = tk.Button(ventana,

boton_push.pack()

boton_pop = tk.Button(vent

boton_push.pack()

boton_pop =

boton_push.pack()

bot

boton_push.pack()


boton_push
"Pop", command=pop_element)
boton_pop.pack()

boton_peek = tk.Button(ventana, text=
boton_pop.pack()

boton_peek = tk.Button(ventana, text

boton_pop.pack()

boton_peek = tk.Button(ventana,

boton_pop.pack()

boton_peek = tk.Button(vent

boton_pop.pack()

boton_peek = tk.Button

boton_pop.pack()

boton_

boton_pop.pack()

boton

boton_pop.pack()

bot

boton_pop
"Top", command=peek_element)
boton_peek.pack()

boton_is_empty = tk.Button(ventana, text=
boton_peek.pack()

boton_is_empty = tk.Button(ventana, text

boton_peek.pack()

boton_is_empty = tk.Button(vent

boton_peek.pack()

boton_is_empty = tk.Button

boton_peek.pack()

boton_is

boton_peek.pack

boton_peek

boton
"Esta vacía", command=is_empty)
boton_is_empty.pack()

boton_size = tk.Button(ventana, text=
boton_is_empty.pack()

boton_size = tk.Button(vent

boton_is_empty.pack()

boton_size = tk.Button(

boton_is_empty.pack()

boton_size

boton_is_empty.pack()


boton
"Tamaño", command=size_stack)
boton_size.pack()

boton_clear = tk.Button(ventana, text=
boton_size.pack()

boton_clear = tk.Button(ventana

boton_size.pack()

boton_clear = tk.Button

boton_size.pack()

boton_clear

boton_size.pack()

bot

boton_size.pack()


bot
"Limpiar", command=clear_stack)
boton_clear.pack()

boton_peek_element = tk.Button(ventana, text=
boton_clear.pack()

boton_peek_element = tk.Button(ventana, text

boton_clear.pack()

boton_peek_element = tk.Button(ventana

boton_clear.pack()

boton_peek_element = tk.Button

boton_clear.pack()

boton_peek_element =

boton_clear.pack()

boton_

boton_clear.pack()


boton_clear

bot
"Peek", command=peek_specific_element)
boton_peek_element.pack()

boton_search = tk.Button(ventana, text=
boton_peek_element.pack()

boton_search = tk.Button(ventana,

boton_peek_element.pack()

boton_search = tk.Button(ventana

boton_peek_element.pack()

boton_search = tk.Button(vent

boton_peek_element.pack()

boton_search = tk.Button(

boton_peek_element.pack()

boton_search = tk.Button

boton_peek_element.pack()

boton_search =

boton_peek_element.pack()

boton

boton_peek_element

boton_peek

bot
"Buscar", command=search_element)
boton_search.pack()

boton_check_balance = tk.Button(ventana, text=
boton_search.pack()

boton_check_balance = tk.Button(ventana, text

boton_search.pack()

boton_check_balance = tk.Button(ventana,

boton_search.pack()

boton_check_balance = tk.Button(vent

boton_search.pack()

boton_check_balance = tk.Button

boton_search.pack()

boton_check_balance = tk

boton_search.pack()

boton

boton_search.pack()

bot

boton_search

boton
"Balance", command=check_balance_expression)
boton_check_balance.pack()

boton_invert = tk.Button(ventana, text=
boton_check_balance.pack()

boton_invert = tk.Button(ventana, text

boton_check_balance.pack()

boton_invert = tk.Button(ventana

boton_check_balance.pack()

boton_invert = tk.Button(

boton_check_balance.pack()

boton_invert =

boton_check_balance.pack()

boton_in

boton_check_balance.pack()


boton_check_balance

boton_check

bot
"Invertir pila", command=invert_stack)
boton_invert.pack()


boton_invert.pack

boton_in

boton

bot
# Etiqueta para mostrar el resultado
label_result = tk.Label(ventana, text=
label_result = tk.Label(ventana, text

label_result = tk.Label(ventana,

label_result = tk.Label(vent

label_result = tk.Label(

label_result = tk

label_result

label
"")
label_result.pack()


label_result.pack

label_result

label
# Iniciar el bucle de eventos de la ventana
ventana.mainloop()
