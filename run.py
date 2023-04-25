import ui # importo ui para poder usar la clase MainWindow que me permite iniciar la aplicacion
import sys # importo sys para poder usar la funcion argv que me permite leer los argumentos que le paso por consola
import menu # importo menu para poder usar la funcion iniciar que me permite iniciar el menu de la aplicacion 

if __name__ == "__main__": # creo la condicion para que solo se ejecute el codigo si se ejecuta el archivo run.py
    if len(sys.argv) > 1 and sys.argv[1] == "-t": # creo la condicion para que si le paso el argumento -t por consola se ejecute el menu de la aplicacion
        menu.iniciar() # ejecuto la funcion iniciar que me permite iniciar el menu de la aplicacion
    else: # creo la condicion para que si no le paso el argumento -t por consola se ejecute la aplicacion
        app = ui.MainWindow() # creo la app para instanciar la clase MainWindow
        app.mainloop() # ejecuto la funcion mainloop que me permite iniciar la aplicacion