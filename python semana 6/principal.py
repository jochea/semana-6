import tkinter as tk

class Vehiculo:
    def __init__(self, placa, marca, color, tipo, hora_ingreso):
        self.vehiculo_info = {
            "placa": placa,
            "marca": marca,
            "color": color,
            "tipo": tipo,
            "hora_ingreso": hora_ingreso}

    def obtener_info(self):
        return self.vehiculo_info
    
class Formulario:
    def __init__(self):
        self.ventana_formulario = tk.Tk()
        self.ventana_formulario.title("Registro de Vehículos")
        
        self.registro_vehiculos = []

        self.label_placa = tk.Label(self.ventana_formulario, text="Placa: ")
        self.entry_placa = tk.Entry(self.ventana_formulario)
        self.label_marca = tk.Label(self.ventana_formulario, text="Marca: ")
        self.entry_marca = tk.Entry(self.ventana_formulario)
        self.label_color = tk.Label(self.ventana_formulario, text="Color: ")
        self.entry_color = tk.Entry(self.ventana_formulario)
        self.label_tipo = tk.Label(self.ventana_formulario, text="Tipo (Residente/Visitante): ")
        self.entry_tipo = tk.Entry(self.ventana_formulario)

        self.boton_guardar = tk.Button(self.ventana_formulario, text="Guardar", command=self.guardar_vehiculo)
        self.boton_limpiar = tk.Button(self.ventana_formulario, text="Limpiar", command=self.limpiar_campos)
        self.boton_mostrar = tk.Button(self.ventana_formulario, text="Mostrar Registro", command=self.mostrar_registro)

        self.label_error = tk.Label(self.ventana_formulario, text="", fg="red")

        self.label_placa.grid(row=0, column=0)
        self.entry_placa.grid(row=0, column=1)
        self.label_marca.grid(row=1, column=0)
        self.entry_marca.grid(row=1, column=1)
        self.label_color.grid(row=2, column=0)
        self.entry_color.grid(row=2, column=1)
        self.label_tipo.grid(row=3, column=0)
        self.entry_tipo.grid(row=3, column=1)

        self.boton_guardar.grid(row=4, column=0)
        self.boton_limpiar.grid(row=4, column=1)
        self.boton_mostrar.grid(row=5, column=0, columnspan=2)

        self.label_error.grid(row=6, column=0, columnspan=2)

        self.ventana_formulario.mainloop()

    def limpiar_campos(self):
        self.entry_placa.delete(0, 'end')
        self.entry_marca.delete(0, 'end')
        self.entry_color.delete(0, 'end')
        self.entry_tipo.delete(0, 'end')
        self.label_error.config(text="")


    def evento_borrar(self):
        self.entry_nombre.delete(0, 'end')

# Código principal
if __name__ == "__main__":
    obj_formulario = Formulario()
