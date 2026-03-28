import tkinter as tk
from tkinter import messagebox

class AppTkinter:
    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio

        self.root.title("Lista de Tareas")

        # Entrada de texto
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        # Evento ENTER
        self.entry.bind("<Return>", self.agregar_tarea_evento)

        # Lista de tareas
        self.lista = tk.Listbox(root, width=50)
        self.lista.pack(pady=10)

        # Evento doble clic
        self.lista.bind("<Double-1>", self.marcar_completada_evento)

        # Botones
        tk.Button(root, text="Añadir Tarea", command=self.agregar_tarea).pack(pady=5)
        tk.Button(root, text="Marcar Completada", command=self.marcar_completada).pack(pady=5)
        tk.Button(root, text="Eliminar", command=self.eliminar_tarea).pack(pady=5)

        self.actualizar_lista()

    # -------- EVENTOS --------

    def agregar_tarea_evento(self, event):
        self.agregar_tarea()

    def marcar_completada_evento(self, event):
        self.marcar_completada()

    # -------- FUNCIONES --------

    def agregar_tarea(self):
        texto = self.entry.get()

        if not self.servicio.agregar_tarea(texto):
            messagebox.showwarning("Error", "Ingrese una tarea válida")
            return

        self.entry.delete(0, tk.END)
        self.actualizar_lista()

    def marcar_completada(self):
        seleccion = self.lista.curselection()

        if not seleccion:
            messagebox.showwarning("Error", "Seleccione una tarea")
            return

        index = seleccion[0]
        tarea = self.servicio.obtener_tareas()[index]

        self.servicio.completar_tarea(tarea.id)
        self.actualizar_lista()

    def eliminar_tarea(self):
        seleccion = self.lista.curselection()

        if not seleccion:
            messagebox.showwarning("Error", "Seleccione una tarea")
            return

        index = seleccion[0]
        tarea = self.servicio.obtener_tareas()[index]

        self.servicio.eliminar_tarea(tarea.id)
        self.actualizar_lista()

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)

        for tarea in self.servicio.obtener_tareas():
            texto = tarea.descripcion

            if tarea.completada:
                texto = "[Hecho] " + texto

            self.lista.insert(tk.END, texto)