import tkinter as tk

class Formulario:
    def __init__(self):
        self.ventana_formulario = tk.Tk()
        self.ventana_formulario.title("Formulario")
        

        self.label_nombre = tk.Label(self.ventana_formulario, text="Escribe el nombre: ")
        self.entry_nombre = tk.Entry(self.ventana_formulario)
        self.boton_enviar = tk.Button(self.ventana_formulario, text="Guardar Cliente", command=self.tomar_datos)
        self.boton_limpiar = tk.Button(self.ventana_formulario, text="Limpiar", command=self.evento_borrar)
        
        self.label_nombre.grid(row=0, column=0)
        self.entry_nombre.grid(row=1, column=0)
        self.boton_enviar.grid(row=0, column=1)
        self.boton_limpiar.grid(row=1, column=1)

        self.ventana_formulario.mainloop()

    def tomar_datos(self):
        nombre = self.entry_nombre.get()
        print(f"Nombre guardado: {nombre}")
        self.entry_nombre.delete(0, 'end')  

    def evento_borrar(self):
        self.entry_nombre.delete(0, 'end')

# Código principal
if __name__ == "__main__":
    obj_formulario = Formulario()
