import tkinter as tk

class AppTkinter:
    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio
        self.root.title("Lista de Tareas")

        # Entrada de texto
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        # Lista de tareas
        self.lista = tk.Listbox(root, width=50)
        self.lista.pack()

        # Botones
        tk.Button(root, text="Agregar", command=self.agregar_tarea).pack(pady=5)
        tk.Button(root, text="Completar", command=self.completar_tarea).pack(pady=5)
        tk.Button(root, text="Eliminar", command=self.eliminar_tarea).pack(pady=5)

        # 🔥 Atajos de teclado (REQUERIDO)
        self.root.bind("<Return>", lambda e: self.agregar_tarea())
        self.root.bind("<c>", lambda e: self.completar_tarea())
        self.root.bind("<Delete>", lambda e: self.eliminar_tarea())
        self.root.bind("<Escape>", lambda e: self.root.quit())

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)
        for tarea in self.servicio.obtener_tareas():
            estado = "✔️" if tarea.completada else "❌"
            self.lista.insert(tk.END, f"{estado} {tarea.descripcion}")

    def agregar_tarea(self):
        texto = self.entry.get()
        self.servicio.agregar_tarea(texto)
        self.entry.delete(0, tk.END)
        self.actualizar_lista()

    def completar_tarea(self):
        try:
            indice = self.lista.curselection()[0]
            self.servicio.completar_tarea(indice)
            self.actualizar_lista()
        except:
            pass

    def eliminar_tarea(self):
        try:
            indice = self.lista.curselection()[0]
            self.servicio.eliminar_tarea(indice)
            self.actualizar_lista()
        except:
            pass