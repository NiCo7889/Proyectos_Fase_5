import helpers
import database as db
from tkinter import * # se pone el * porque se importa todo lo que hay dentro de tkinter (todas las clases de tkinter)
from tkinter import ttk # se importa ttk para poder usar las clases de tkinter que tienen un estilo mas moderno
from tkinter.messagebox import askokcancel, WARNING # se importa askokcancel para poder usar la funcion que me permite preguntar si estoy seguro de borrar un cliente y WARNING para poder usar la funcion que me permite mostrar un mensaje de advertencia


class CenterWidgetMixin: # creo la clase CenterWidgetMixin que me permite centrar la ventana 
    def center(self):
        self.update()
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int(ws/2 - w/2)
        y = int(hs/2 - h/2)
        self.geometry(f"{w}x{h}+{x}+{y}")


class CreateClientWindow(Toplevel, CenterWidgetMixin): # creo la clase CreateClientWindow que hereda de Toplevel y CenterWidgetMixin que me permite crear una ventana para crear un cliente
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Crear cliente")
        self.build()
        self.center()
        self.transient(parent)
        self.grab_set()

    def build(self):
        frame = Frame(self)
        frame.pack(padx=20, pady=10)

        Label(frame, text="CD (2 ints y 1 upper char)").grid(row=0, column=0)
        Label(frame, text="Producto (de 2 a 30 chars)").grid(row=0, column=1)
        Label(frame, text="categoria (de 2 a 30 chars)").grid(row=0, column=2)

        CD = Entry(frame)
        CD.grid(row=1, column=0)
        CD.bind("<KeyRelease>", lambda event: self.validate(event, 0))
        Producto = Entry(frame)
        Producto.grid(row=1, column=1)
        Producto.bind("<KeyRelease>", lambda event: self.validate(event, 1))
        categoria = Entry(frame)
        categoria.grid(row=1, column=2)
        categoria.bind("<KeyRelease>", lambda event: self.validate(event, 2))

        frame = Frame(self)
        frame.pack(pady=10)

        crear = Button(frame, text="Crear", command=self.create_client)
        crear.configure(state=DISABLED)
        crear.grid(row=0, column=0)
        Button(frame, text="Cancelar", command=self.close).grid(row=0, column=1)

        self.validaciones = [0, 0, 0]
        self.crear = crear
        self.CD = CD
        self.Producto = Producto
        self.categoria = categoria

    def create_client(self):
        self.master.treeview.insert(
            parent='', index='end', iid=self.CD.get(),
            values=(self.CD.get(), self.Producto.get(), self.categoria.get()))
        db.Inventario.crear(self.CD.get(), self.Producto.get(), self.categoria.get())
        self.close()

    def close(self):
        self.destroy()
        self.update()

    def validate(self, event, index):
        valor = event.widget.get()
        valido = helpers.CD_valido(valor, db.Inventario.lista) if index == 0 \
            else (valor.isalpha() and len(valor) >= 2 and len(valor) <= 30)
        event.widget.configure({"bg": "Green" if valido else "Red"})
        # Cambiar el estado del botón en base a las validaciones
        self.validaciones[index] = valido
        self.crear.config(state=NORMAL if self.validaciones == [1, 1, 1] else DISABLED)


class EditClientWindow(Toplevel, CenterWidgetMixin): # creo la clase EditClientWindow que hereda de Toplevel y CenterWidgetMixin que me permite crear una ventana para editar un cliente 
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Actualizar cliente")
        self.build()
        self.center()
        self.transient(parent)
        self.grab_set()

    def build(self):
        frame = Frame(self)
        frame.pack(padx=20, pady=10)

        Label(frame, text="CD (no editable)").grid(row=0, column=0)
        Label(frame, text="Producto (de 2 a 30 chars)").grid(row=0, column=1)
        Label(frame, text="categoria (de 2 a 30 chars)").grid(row=0, column=2)

        CD = Entry(frame)
        CD.grid(row=1, column=0)
        Producto = Entry(frame)
        Producto.grid(row=1, column=1)
        Producto.bind("<KeyRelease>", lambda event: self.validate(event, 0))
        categoria = Entry(frame)
        categoria.grid(row=1, column=2)
        categoria.bind("<KeyRelease>", lambda event: self.validate(event, 1))

        cliente = self.master.treeview.focus()
        campos = self.master.treeview.item(cliente, 'values')
        CD.insert(0, campos[0])
        CD.config(state=DISABLED)
        Producto.insert(0, campos[1])
        categoria.insert(0, campos[2])

        frame = Frame(self)
        frame.pack(pady=10)

        actualizar = Button(frame, text="Actualizar", command=self.edit_client)
        actualizar.grid(row=0, column=0)
        Button(frame, text="Cancelar", command=self.close).grid(row=0, column=1)

        self.validaciones = [1, 1]
        self.actualizar = actualizar
        self.CD = CD
        self.Producto = Producto
        self.categoria = categoria

    def edit_client(self):
        cliente = self.master.treeview.focus()
        self.master.treeview.item(cliente, values=(
            self.CD.get(), self.Producto.get(), self.categoria.get()))
        db.Clientes.modificar(self.CD.get(), self.Producto.get(), self.categoria.get())
        self.close()

    def close(self):
        self.destroy()
        self.update()

    def validate(self, event, index):
        valor = event.widget.get()
        valido = (valor.isalpha() and len(valor) >= 2 and len(valor) <= 30)
        event.widget.configure({"bg": "Green" if valido else "Red"})
        # Cambiar el estado del botón en base a las validaciones
        self.validaciones[index] = valido
        self.actualizar.config(state=NORMAL if self.validaciones == [1, 1] else DISABLED)


class MainWindow(Tk, CenterWidgetMixin): # creo la clase MainWindow que hereda de Tk y CenterWidgetMixin que me permite crear una ventana principal
    def __init__(self):
        super().__init__()
        self.title("Gestor de clientes")
        self.build()
        self.center()

    def build(self):
        frame = Frame(self)
        frame.pack()

        treeview = ttk.Treeview(frame)
        treeview['columns'] = ('CD', 'Producto', 'categoria')

        treeview.column("#0", width=0, stretch=NO)
        treeview.column("CD", anchor=CENTER)
        treeview.column("Nombre", anchor=CENTER)
        treeview.column("categoria", anchor=CENTER)

        treeview.heading("CD", text="DNI", anchor=CENTER)
        treeview.heading("Producto", text="Producto", anchor=CENTER)
        treeview.heading("categoria", text="categoria", anchor=CENTER)

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        treeview['yscrollcommand'] = scrollbar.set

        for cliente in db.Inventario.lista:
            treeview.insert(
                parent='', index='end', iid=cliente.CD,
                values=(cliente.CD, cliente.Producto, cliente.categoria))

        treeview.pack()

        frame = Frame(self)
        frame.pack(pady=20)

        Button(frame, text="Crear", command=self.create).grid(row=0, column=0)
        Button(frame, text="Modificar", command=self.edit).grid(row=0, column=1)
        Button(frame, text="Borrar", command=self.delete).grid(row=0, column=2)

        self.treeview = treeview

    def delete(self):
        cliente = self.treeview.focus()
        if cliente:
            campos = self.treeview.item(cliente, "values")
            confirmar = askokcancel(
                title="Confirmar borrado",
                message=f"¿Borrar {campos[1]} {campos[2]}?",
                icon=WARNING)
            if confirmar:
                self.treeview.delete(cliente)
                db.Inventario.borrar(campos[0])

    def create(self):
        CreateClientWindow(self)

    def edit(self):
        if self.treeview.focus():
            EditClientWindow(self)


if __name__ == "__main__": # ejecuto el programa
    app = MainWindow()
    app.mainloop()