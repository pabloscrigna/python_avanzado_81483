import tkinter as tk

# creamos la ventana
root = tk.Tk()

root.title("Mi primer programa")
root.geometry("400x200")

label = tk.Label(root, text="Hola mundo!!!", font=("Arial", 16))
label.pack()

#Ejecutar la aplicacion
root.mainloop()