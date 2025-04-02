import tkinter as tk
from datetime import datetime

class Vehiculo:
    def __init__(self, placa, marca, color, tipo, hora_ingreso):
        self.vehiculo_info = {
            "placa": placa,
            "marca": marca,
            "color": color,
            "tipo": tipo,
            "hora_ingreso": hora_ingreso
        }

    def obtener_info(self):
        return self.vehiculo_info

class Formulario:
    def __init__(self):
        self.ventana_formulario = tk.Tk()
        self.ventana_formulario.title("Registro de Vehículos")
        
        self.registro_vehiculos = []

        # Labels y entradas
        self.label_placa = tk.Label(self.ventana_formulario, text="Placa:")
        self.entry_placa = tk.Entry(self.ventana_formulario)
        self.label_marca = tk.Label(self.ventana_formulario, text="Marca:")
        self.entry_marca = tk.Entry(self.ventana_formulario)
        self.label_color = tk.Label(self.ventana_formulario, text="Color:")
        self.entry_color = tk.Entry(self.ventana_formulario)
        self.label_tipo = tk.Label(self.ventana_formulario, text="Tipo (Residente/Visitante):")
        self.entry_tipo = tk.Entry(self.ventana_formulario)

        # Botones
        self.boton_guardar = tk.Button(self.ventana_formulario, text="Guardar", command=lambda: self.guardar_vehiculo())
        self.boton_limpiar = tk.Button(self.ventana_formulario, text="Limpiar", command=self.limpiar_campos)
        self.boton_mostrar = tk.Button(self.ventana_formulario, text="Mostrar Registro", command=self.mostrar_registro)

        # Etiquetas de error y salida
        self.label_error = tk.Label(self.ventana_formulario, text="", fg="red")
        self.label_salida = tk.Label(self.ventana_formulario, text="", fg="blue", justify="left")

        # Layout
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
        self.label_salida.grid(row=7, column=0, columnspan=2)

        self.ventana_formulario.mainloop()

    def limpiar_campos(self):
        self.entry_placa.delete(0, 'end')
        self.entry_marca.delete(0, 'end')
        self.entry_color.delete(0, 'end')
        self.entry_tipo.delete(0, 'end')
        self.label_error.config(text="")
        self.label_salida.config(text="")

    def guardar_vehiculo(self):
        placa = self.entry_placa.get().strip()
        marca = self.entry_marca.get().strip()
        color = self.entry_color.get().strip()
        tipo = self.entry_tipo.get().strip()
        hora_ingreso = datetime.now().strftime("%H:%M:%S")

        # Validación
        if not placa or not marca or not color or not tipo:
            self.label_error.config(text="¡Todos los campos son obligatorios!")
            return

        vehiculo = Vehiculo(placa, marca, color, tipo, hora_ingreso)
        self.registro_vehiculos.append(vehiculo.obtener_info())

        self.label_error.config(text="Vehículo registrado exitosamente", fg="green")
        self.limpiar_campos()

    def mostrar_registro(self):
        if not self.registro_vehiculos:
            self.label_salida.config(text="No hay vehículos registrados.")
            return

        salida_texto = ""
        for i, vehiculo in enumerate(self.registro_vehiculos, start=1):
            info = f"{i}. {vehiculo['placa']} - {vehiculo['marca']} - {vehiculo['color']} - {vehiculo['tipo']} - {vehiculo['hora_ingreso']}\n"
            salida_texto += info
            print(info)  # Muestra en consola

        self.label_salida.config(text=salida_texto)

# Código principal
if __name__ == "__main__":
    obj_formulario = Formulario()
