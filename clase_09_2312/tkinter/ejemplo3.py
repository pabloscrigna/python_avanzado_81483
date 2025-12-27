import tkinter as tk


def saludar():
    print("Presionaron el boton")


# creamos la ventana
root = tk.Tk()

root.title("Mi primer programa")
root.geometry("400x200")

boton = tk.Button(root, text="Saludar", command=saludar)
boton.pack(padx=50, pady=50)

#Ejecutar la aplicacion
root.mainloop()