import tkinter as tk
from tkinter import filedialog, messagebox,Button
from tkinter.scrolledtext import ScrolledText
#from Analizador import intruccion, getErrores,operar_


class interfaz():

    def __init__(self, root):

        self.root = root
        self.root.title("Aplicación Númerica con Análisis Léxico")
        self.root.geometry("%dx%d+%d+%d" % (900,500,350,100))
        self.root.resizable(0,0)

        self.barra_numeros = tk.Text(root, width=2, padx = 4, takefocus = 0, border = 3, background = 'lightblue', state ='disabled')
        self.barra_numeros.pack(side = tk.LEFT, fill = tk.Y)

        self.campo_texto = ScrolledText(self.root, wrap = tk.WORD)
        self.campo_texto.pack(expand = True, fill = 'both')
        
        self.campo_texto.bind('<Key>', self.actualizando_barra_numeros)
        self.campo_texto.bind('<MouseWheel>', self.actualizando_barra_numeros)

        self.current_line = 1

        self.menu_bar = tk.Menu(root)
        
        self.root.config(menu = self.menu_bar)

        self.menu_archivo = tk.Menu(self.menu_bar, tearoff=0)
        
        self.menu_bar.add_cascade(label="Archivo", menu=self.menu_archivo)
        self.menu_archivo.add_command(label = "Abrir Archivo", command = self.CargarArchivo)
        self.menu_archivo.add_command(label = "Guardar", command = self.guardar)
        self.menu_archivo.add_command(label = "Guardar Como", command = self.guardar_como)
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label = "Salir", command = self.root.quit)
        self.menu_bar.add_command(label = "Analizar")
        self.menu_bar.add_command(label = "Errores")


    def CargarArchivo(self):
        global archivo_actual
        archivo = filedialog.askopenfilename()
        if archivo:
            archivo_actual = archivo
            with open(archivo, 'r') as info_archivo:
                contenido = info_archivo.read()
                self.campo_texto.delete(1.0, tk.END)
                self.campo_texto.insert(tk.END, contenido)
            self.actualizando_barra_numeros()
        self.data = self.campo_texto.get(1.0, tk.END)
        
    def actualizando_barra_numeros(self, event = None):
        contador_linea = self.campo_texto.get('1.0', tk.END).count('\n')
        if contador_linea != self.current_line:
            self.barra_numeros.config(state = tk.NORMAL)
            self.barra_numeros.delete(1.0, tk.END)
            for line in range(1, contador_linea + 1):
                self.barra_numeros.insert(tk.END, f"{line}\n")
            self.barra_numeros.config(state = tk.DISABLED)
            self.current_line = contador_linea

   
    
    def guardar_como(self):
        file_path = filedialog.asksaveasfilename(defaultextension = ".json")
        if file_path:
            content = self.campo_texto.get(1.0, tk.END)
            with open(file_path, 'w') as file:
                file.write(content)
            messagebox.showinfo("Guardado", "Archivo guardado exitosamente.")
   

    def guardar(self):
        global archivo_actual
        contenido = self.campo_texto.get("1.0", "end-1c")  
        with open(archivo_actual, "w") as archivo:
            archivo.write(contenido)  
        messagebox.showinfo("Guardado", "Archivo guardado exitosamente.")
   
            

    

if __name__ == "__main__":
    root = tk.Tk()
    app = interfaz(root)
    root.mainloop()