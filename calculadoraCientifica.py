# Es necesario instalar la librería de ttkthemes y matplotlib con pip install ttkthemes matplotlib

import tkinter as UPP
from tkinter import ttk 
from ttkthemes import ThemedTk
import matplotlib.pyplot as plt
import pandas as pd
import random
from turtle import RawTurtle, TurtleScreen

# Crear ventana
ventana = ThemedTk(theme="arc")
ventana.title("Proyecto calculadora científica")
ventana.geometry("800x600")


# Definir variables y funciones para la calculadora de áreas
LabelResultado = None
poligono = UPP.IntVar()

def Reset_calc():
    global LabelResultado
    print("reset")
    Clear_calc()
    RadioBotonCirculo = ttk.Radiobutton(tab1, text="Calcular área de un círculo", variable= poligono, value= 0,  command=calcular_area)
    RadioBotonTriangulo = ttk.Radiobutton(tab1, text="Calcular área de un triángulo",variable= poligono, value= 1, command=calcular_area)
    RadioBotonCuadrado = ttk.Radiobutton(tab1, text="Calcular área de un cuadrado", variable= poligono, value= 2,  command=calcular_area)
    RadioBotonRectangulo = ttk.Radiobutton(tab1, text="Calcular área de un rectángulo", variable= poligono, value= 3, command=calcular_area)
    RadioBotonPoligono = ttk.Radiobutton(tab1, text="Calcular área de un polígono regular", variable= poligono, value= 4, command=calcular_area)
    RadioBotonCirculo.grid(row=0,column=0, padx=4, pady=2, sticky= "w")
    RadioBotonTriangulo.grid(row=1,column=0, padx=4, pady=2, sticky="w")
    RadioBotonCuadrado.grid(row=2,column=0, padx=4, pady=2, sticky="w")
    RadioBotonRectangulo.grid(row=3,column=0, padx=4, pady=2, sticky="w")
    RadioBotonPoligono.grid(row=4,column=0, padx=4, pady=2, sticky="w")
    LabelResultado = None

def Clear_calc():
    print("clear")
    for widget in tab1.winfo_children():
        widget.destroy()

    
def Manipular_Resultado():
    global LabelResultado
    AreaFormateada = '{:.2f}'.format(AreaResultado).rstrip('0').rstrip('.')
    if LabelResultado is None:
        LabelResultado = ttk.Label(tab1, text=f"El área de tu {poligonoNombre} es {AreaFormateada}", font=("arial",12))
        LabelResultado.grid(column=2, row= 1, sticky="w", padx=50, pady=15)
        print("Se crea la etiqueta")
    else:
        LabelResultado.config(text=f"El área de tu {poligonoNombre} es {AreaFormateada}")
        print("Se modifica la etiqueta")
        
def Area_Circulo():
    global EntradaValor1
    global AreaResultado
    AreaResultado = 3.1416 * float(EntradaValor1.get())**2
    Manipular_Resultado()

    
def Area_Triangulo():
    print("Area Triangulo")
    global EntradaValor1
    global EntradaValor2
    global AreaResultado
    AreaResultado = float(EntradaValor1.get()) * float(EntradaValor2.get())*0.5
    
    Manipular_Resultado()
    
def Area_Cuadrado():
    print("Area Cuadrado")
    global EntradaValor1
    global AreaResultado
    AreaResultado=float(EntradaValor1.get())**2
    Manipular_Resultado()
    
        
def Area_Rectangulo():
    print("Area Rectangulo")

    global EntradaValor1
    global EntradaValor2
    global AreaResultado
    AreaResultado = float(EntradaValor1.get())* float(EntradaValor2.get())
    Manipular_Resultado()
    
def Area_Poligono():
    print("Area polígono")
    
    global EntradaValor1
    global EntradaValor2
    global AreaResultado
    AreaResultado = float(EntradaValor1.get()) * float(EntradaValor2.get())*0.5
    
    Manipular_Resultado()
                
        
    
def calcular_area():
    global EntradaValor1
    global EntradaValor2
    global EtiquetaIntroduce
    global EtiquetaIntroduce2
    global BotonCalcular
    global poligonoNombre
    
    if poligono.get() == 0:
        poligonoNombre = "circulo"
        print("Circulo")
        Clear_calc()
        EtiquetaSeleccion = ttk.Label(tab1, text="Haz seleccionado el círculo")         
        EtiquetaIntroduce = ttk.Label(tab1, text="Introduce el valor del radio")        
        EntradaValor1 = ttk.Entry(tab1)
        BotonCalcular = ttk.Button(tab1, text="Calcular área", command=Area_Circulo)
        
        EtiquetaSeleccion.grid(padx=50, column=1, row= 0, sticky="w", pady=15)
        EtiquetaIntroduce.grid(padx=50, column=1, row= 1, sticky="w", pady=15)
        EntradaValor1.grid(padx=50, column=1, row=2, sticky="w", pady=15)        
        BotonCalcular.grid(padx=50, column=1, row= 3, sticky="w", pady=15)
        ttk.Button(tab1, text="Regresar", command=Reset_calc).grid(padx=50, column=1, row=10, sticky="w", pady=15)
        
    elif poligono.get() == 1:
        print("triangulo")
        
        poligonoNombre = "triángulo"
        
        Clear_calc()
        
        EtiquetaSeleccion = ttk.Label(tab1, text="Haz seleccionado el triángulo")
        EtiquetaSeleccion.grid(padx=50, column=1, row= 0, sticky="w", pady=15)
                
        EtiquetaIntroduce = ttk.Label(tab1, text="Introduce el valor de la base")
        EtiquetaIntroduce.grid(padx=50, column=1, row= 1, sticky="w", pady=15)
        
        EntradaValor1 = ttk.Entry(tab1)
        EntradaValor1.grid(padx=50, column=1, row=2, sticky="w", pady=15)
        
        EtiquetaIntroduce2 = ttk.Label(tab1, text="Introduce el valor de la altura")
        EtiquetaIntroduce2.grid(padx=50,column=1, row= 3, sticky="w", pady=15)
        

        EntradaValor2 = ttk.Entry(tab1)
        EntradaValor2.grid(padx=50, column=1, row=4, sticky="w", pady=15)
        
        BotonCalcular=ttk.Button(tab1, text="Calcular área", command=Area_Triangulo)
        BotonCalcular.grid(padx=50, column=1, row= 5, sticky="w", pady=15)
        ttk.Button(tab1, text="Regresar", command=Reset_calc).grid(padx=50, column=1, row=10, sticky="w", pady=15)
        
    elif poligono.get() == 2:
        print("cuadrado")
        
        poligonoNombre = "cuadrado"
        
        Clear_calc()
        
        EtiquetaSeleccion = ttk.Label(tab1, text="Haz seleccionado el cuadrado")
        EtiquetaSeleccion.grid(padx=50, column=1, row= 0, sticky="w", pady=15)
                
        EtiquetaIntroduce = ttk.Label(tab1, text="Introduce el valor de un lado")
        EtiquetaIntroduce.grid(padx=50, column=1, row= 1, sticky="w", pady=15)
        
        EntradaValor1 = ttk.Entry(tab1)
        EntradaValor1.grid(padx=50, column=1, row=2, sticky="w", pady=15)
        
        ttk.Button(tab1, text="Calcular área", command=Area_Cuadrado).grid(padx=50, column=1, row= 3, sticky="w", pady=15)
        ttk.Button(tab1, text="Regresar", command=Reset_calc).grid(padx=50, column=1, row=10, sticky="w", pady=15)
        
    elif poligono.get() == 3:
        print("rectángulo")
        
        poligonoNombre = "rectángulo"
         
        Clear_calc()
        
        EtiquetaSeleccion = ttk.Label(tab1, text="Haz seleccionado el rectángulo")
        EtiquetaSeleccion.grid(padx=50, column=1, row= 0, sticky="w", pady=15)
                
        EtiquetaIntroduce = ttk.Label(tab1, text="Introduce el valor de la base")
        EtiquetaIntroduce.grid(padx=50, column=1, row= 1, sticky="w", pady=15)
        
        EntradaValor1 = ttk.Entry(tab1)
        EntradaValor1.grid(padx=50, column=1, row=2, sticky="w", pady=15)
        
        EtiquetaIntroduce2 = ttk.Label(tab1, text="Introduce el valor de la altura")
        EtiquetaIntroduce2.grid(padx=50, column=1, row= 3, sticky="w", pady=15)

        EntradaValor2 = ttk.Entry(tab1)
        EntradaValor2.grid(padx=50, column=1, row=4, sticky="w", pady=15)
        
        
        ttk.Button(tab1, text="Calcular área", command=Area_Rectangulo).grid(padx=50, column=1, row= 5, sticky="w", pady=15)
        ttk.Button(tab1, text="Regresar", command=Reset_calc).grid(column=1, row=10, sticky="w", padx=50, pady=15)        
        
    elif poligono.get() == 4:
        
        print("Poligono")
        
        poligonoNombre = "polígono regular"
        
        Clear_calc()
        EtiquetaSeleccion = ttk.Label(tab1, text="Haz seleccionado el polígono regular")
        EtiquetaSeleccion.grid(padx=50, column=1, row= 0, sticky="w", pady=15)
                
        EtiquetaIntroduce = ttk.Label(tab1, text="Introduce el valor del perímetro")
        EtiquetaIntroduce.grid(padx=50, column=1, row= 1, sticky="w", pady=15)
        
        EntradaValor1 = ttk.Entry(tab1)
        EntradaValor1.grid(padx=50, column=1, row=2, sticky="w", pady=15)
        
        EtiquetaIntroduce2 = ttk.Label(tab1, text="Introduce el valor del apotema")
        EtiquetaIntroduce2.grid(padx=50, column=1, row= 3, sticky="w", pady=15)
        

        EntradaValor2 = ttk.Entry(tab1)
        EntradaValor2.grid(padx=50, column=1, row=4, sticky="w", pady=15)
        
        ttk.Button(tab1, text="Calcular área", command=Area_Poligono).grid(padx=50, column=1, row= 5, sticky="w", pady=15)
        ttk.Button(tab1, text="Regresar", command=Reset_calc).grid(padx=50, column=1, row=10, sticky="w", pady=15)
        
    else:
        print("error")

# Definir variables y funciones para la calculadora simple
resultado = ""
nuevoTexto = ""
operando1 = ""
operando2 = ""
TextoLabel = ""
operacion=""

def ejecutar_CE():
    TextoLabel = ""
    operando1 = ""
    operando2 = ""
    nuevoTexto=TextoLabel
    TextoOP.config(text=nuevoTexto)
    print("Ejecutar_CE")
    
def ejecutar_C():
    TextoOP.config(text="")
    print("Ejecutar_C")
    
def ejecutar_bkspc():
    TextoLabel = TextoOP.cget("text")
    nuevoTexto = TextoLabel[:-1]
    TextoOP.config(text=nuevoTexto)
    print("Ejecutar_bkspc")

def op_division():
    global operacion, operando1
    operacion = "/"
    operando1 = TextoOP.cget("text")
    TextoOP.config(text="")
    print("op_division")
    
def op_multi():
    global operacion, operando1
    operacion = "*"
    operando1 = TextoOP.cget("text")
    TextoOP.config(text="")
    print("op_multi")
    
def op_resta():
    global operacion, operando1
    operacion = "-"
    operando1 = TextoOP.cget("text")
    TextoOP.config(text="") 
    print("op_resta")
    
def op_suma():
    global operacion, operando1
    operacion = "+"
    operando1 = TextoOP.cget("text")
    TextoOP.config(text="")   
    print("op_suma")
    
def op_realizar():
    operando2 = TextoOP.cget("text")
    if operacion == "/":
        nuevoTexto = float(operando1) / float(operando2)
        
    elif operacion == "*":
        nuevoTexto = float(operando1) * float(operando2)
        
    elif operacion == "+":
        nuevoTexto = float(operando1) + float(operando2)
        
    elif operacion == "-":
        nuevoTexto = float(operando1) - float(operando2)
        
    if nuevoTexto.is_integer():
        nuevoTexto=int(nuevoTexto)
        
    TextoOP.config(text=str(nuevoTexto))
    print(TextoOP.cget("text"))
    
def set7():
    TextoLabel = TextoOP.cget("text")
    nuevoTexto = TextoLabel + "7"
    TextoOP.config(text=nuevoTexto)
    print("set7")

def set8():
    TextoLabel = TextoOP.cget("text")
    nuevoTexto = TextoLabel + "8"
    TextoOP.config(text=nuevoTexto)
    print("set8")
    
def set9():
    TextoLabel = TextoOP.cget("text")
    nuevoTexto = TextoLabel + "9"
    TextoOP.config(text=nuevoTexto)
    print("set9")
    
def set4():
    TextoLabel = TextoOP.cget("text")
    nuevoTexto = TextoLabel + "4"
    TextoOP.config(text=nuevoTexto)
    print("set4")
    
def set5():
    TextoLabel = TextoOP.cget("text")
    nuevoTexto = TextoLabel + "5"
    TextoOP.config(text=nuevoTexto)
    print("set5")
    
def set6():
    TextoLabel = TextoOP.cget("text")
    nuevoTexto = TextoLabel + "6"
    TextoOP.config(text=nuevoTexto)
    print("set6")
    
def set1():
    TextoLabel = TextoOP.cget("text")
    nuevoTexto = TextoLabel + "1"
    TextoOP.config(text=nuevoTexto)
    print("set1")
    
def set2():
    TextoLabel = TextoOP.cget("text")
    nuevoTexto = TextoLabel + "2"
    TextoOP.config(text=nuevoTexto)
    print("set2")
    
def set3():
    TextoLabel = TextoOP.cget("text")
    nuevoTexto = TextoLabel + "3"
    TextoOP.config(text=nuevoTexto)
    print("set3")

def setDot():
    if "." not in TextoOP.cget("text"):
        TextoLabel = TextoOP.cget("text")
        nuevoTexto = TextoLabel + "."
        TextoOP.config(text=nuevoTexto)
        print("Set.")
    print("No se puede agregar otro punto")

def set0():
    TextoLabel = TextoOP.cget("text")
    nuevoTexto = TextoLabel + "0"
    TextoOP.config(text=nuevoTexto)
    print("set0")
    
# Definir variables y funciones para el Gauge y spinbox
aguja_id = ""
ValorGauge = 0

def Cambiar_Aguja():
    global ValorGauge
    print("Cambiar_Aguja")
    ValorGauge = (float(SpinboxGauge.get())-10)*179/60
    gauge.itemconfig(aguja_id, start=179 - ValorGauge)

# Definir función y variables para graficar datos
def grafica():
#categorias
    cate1 = ingre_cat1.get()
    cate2 = ingre_cat2.get()
    cate3 = ingre_cat3.get()
    cate4 = ingre_cat4.get()
#frecuencia 
    frecu1 = ingre_fre1.get()
    frecu2 = ingre_fre2.get()
    frecu3 = ingre_fre3.get()
    frecu4 = ingre_fre4.get()
#Título
    titulo = ingre_titulo.get()

#categorias (datos globales)
    categorias = [cate1, cate2, cate3, cate4]
    frecuencia = pd.to_numeric([frecu1, frecu2, frecu3, frecu4], errors="coerce")

#Gráfica de barras
    plt.title(titulo)
    plt.bar(categorias, frecuencia, width=0.5)
    plt.xlabel('Categorías')
    plt.ylabel('Frecuencia')
    plt.show()
        
# Definir la notebook con la que vamos a trabajar
    
notebook= ttk.Notebook(ventana)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tab4 = ttk.Frame(notebook)
tab5 = ttk.Frame(notebook)

notebook.add(tab1, text="Calculadora de áreas")
notebook.add(tab2, text="Calculadora simple")
notebook.add(tab3, text= "Gauge y spinbox")
notebook.add(tab4, text= "Graficadora de datos")
notebook.add(tab5, text= "Presentación del equipo")
notebook.pack(expand=True, fill="both")

# Agregar widgets de la calculadora de áreas
RadioBotonCirculo = ttk.Radiobutton(tab1, text="Calcular área de un círculo", variable= poligono, value= 0,  command=calcular_area)
RadioBotonTriangulo = ttk.Radiobutton(tab1, text="Calcular área de un triángulo",variable= poligono, value= 1, command=calcular_area)
RadioBotonCuadrado = ttk.Radiobutton(tab1, text="Calcular área de un cuadrado", variable= poligono, value= 2,  command=calcular_area)
RadioBotonRectangulo = ttk.Radiobutton(tab1, text="Calcular área de un rectángulo", variable= poligono, value= 3, command=calcular_area)
RadioBotonPoligono = ttk.Radiobutton(tab1, text="Calcular área de un polígono regular", variable= poligono, value= 4, command=calcular_area)


# Agregar widgets a la pestaña de calculadora simple

TextoOP = ttk.Label(tab2, relief="sunken", borderwidth="4", anchor="e", font=("arial", 12))
boton1 = ttk.Button(tab2, text="CE", command= ejecutar_CE)
boton2 = ttk.Button(tab2, text="C", command= ejecutar_C)
boton3 = ttk.Button(tab2, text="<─", command= ejecutar_bkspc)
boton4 = ttk.Button(tab2, text="÷", command= op_division)

boton5 = ttk.Button(tab2, text="7", command= set7)
boton6 = ttk.Button(tab2, text="8", command= set8)
boton7 = ttk.Button(tab2, text="9", command= set9)
boton8 = ttk.Button(tab2, text="×", command= op_multi)

boton9 = ttk.Button(tab2, text="4", command= set4)
boton10 = ttk.Button(tab2, text="5", command= set5)
boton11 = ttk.Button(tab2, text="6", command= set6)
boton12 = ttk.Button(tab2, text="─", command= op_resta)

boton13 = ttk.Button(tab2, text="1", command= set1)
boton14 = ttk.Button(tab2, text="2", command= set2)
boton15 = ttk.Button(tab2, text="3", command= set3)
boton16 = ttk.Button(tab2, text="+", command= op_suma)

boton17 = ttk.Button(tab2, text="·", command= setDot)
boton18 = ttk.Button(tab2, text="0", command= set0)
boton19 = ttk.Button(tab2, text="<┘", command= op_realizar)


# Arreglo de radiobotones para la calculadora de áreas
RadioBotonCirculo.grid(row=0,column=0, padx=4, pady=2, sticky= "w")
RadioBotonTriangulo.grid(row=1,column=0, padx=4, pady=2, sticky="w")
RadioBotonCuadrado.grid(row=2,column=0, padx=4, pady=2, sticky="w")
RadioBotonRectangulo.grid(row=3,column=0, padx=4, pady=2, sticky="w")
RadioBotonPoligono.grid(row=4,column=0, padx=4, pady=2, sticky="w")


# Arreglo de botones para la calculadora simple

TextoOP.grid(column=0, row=0, columnspan=4, padx=3, pady=3, sticky="nswe")
boton1.grid(row=1, column=0, padx=2, pady=2, sticky="nswe")
boton2.grid(row=1, column=1, padx=2, pady=2, sticky="nswe")
boton3.grid(row=1, column=2, padx=2, pady=2, sticky="nswe")
boton4.grid(row=1, column=3, padx=2, pady=2, sticky="nswe")

boton5.grid(row=2, column=0, padx=2, pady=2, sticky="nswe")
boton6.grid(row=2, column=1, padx=2, pady=2, sticky="nswe")
boton7.grid(row=2, column=2, padx=2, pady=2, sticky="nswe")
boton8.grid(row=2, column=3, padx=2, pady=2, sticky="nswe")

boton9.grid(row=3, column=0, padx=2, pady=2, sticky="nswe")
boton10.grid(row=3, column=1, padx=2, pady=2, sticky="nswe")
boton11.grid(row=3, column=2, padx=2, pady=2, sticky="nswe")
boton12.grid(row=3, column=3, padx=2, pady=2, sticky="nswe")

boton13.grid(row=4, column=0, padx=2, pady=2, sticky="nswe")
boton14.grid(row=4, column=1, padx=2, pady=2, sticky="nswe")
boton15.grid(row=4, column=2, padx=2, pady=2, sticky="nswe")
boton16.grid(row=4, column=3, padx=2, pady=2, sticky="nswe")

boton17.grid(row=5, column=0, padx=2, pady=2, sticky="nswe")
boton18.grid(row=5, column=1, padx=2, pady=2, sticky="nswe")
boton19.grid(row=5, column=2, columnspan=2, padx=2, pady=2, sticky="nswe")

# Agregar el canvas del gauge
gauge = UPP.Canvas(tab3, width=500, height=400)

PosGauge = 70, 50, 350, 350
ValorGauge=0
gauge.create_arc(PosGauge, start=0, extent=180, fill="white",  width=3)

gauge.create_arc(PosGauge, start=0, extent=50, fill="red", width=3)
gauge.create_arc(PosGauge, start=130, extent=50, fill="yellow" ,  width=3)
gauge.create_arc(72, 52, 348, 348, start=50, extent=80, fill="green", outline="green",  width=2)

gauge.create_arc(PosGauge, start= 165, extent=1, width=3)
gauge.create_arc(PosGauge, start= 135, extent=1, width=3)
gauge.create_arc(PosGauge, start= 105, extent=1, width=3)
gauge.create_arc(PosGauge, start= 75, extent=1, width=3)
gauge.create_arc(PosGauge, start= 45, extent=1, width=3)
gauge.create_arc(PosGauge, start= 15, extent=1, width=3)

gauge.create_arc(90, 70, 330, 330, start= 1, extent=178, width=3, fill="white", outline="white")

gauge.create_arc(PosGauge, start= 150, extent=1, width=3)
gauge.create_arc(PosGauge, start= 120, extent=1, width=3)
gauge.create_arc(PosGauge, start= 90, extent=1, width=3)
gauge.create_arc(PosGauge, start= 60, extent=1, width=3)
gauge.create_arc(PosGauge, start= 30, extent=1, width=3)

gauge.create_arc(110, 90, 310, 310, start= 1, extent=178, width=3, fill="white", outline="white")


aguja_id = gauge.create_arc(PosGauge, start= 179, extent=1, width=1, outline="red", fill="red")


SpinboxGauge= ttk.Spinbox(tab3, from_=10, to=70, increment=0.5, width=5, state="readonly", command=Cambiar_Aguja )

# Etiquetas de texto

gauge.create_text(210, 20, font="Arial 20 italic bold", text="Presión")

gauge.create_text(100, 190, font="Arial 12 bold", text="10")
gauge.create_text(140, 150, font="Arial 12 bold", text="20")
gauge.create_text(165, 120, font="Arial 12 bold", text="30")
gauge.create_text(210, 100, font="Arial 12 bold", text="40")
gauge.create_text(255, 120, font="Arial 12 bold", text="50")
gauge.create_text(280, 150, font="Arial 12 bold", text="60")
gauge.create_text(320, 190, font="Arial 12 bold", text="70")


# Insertar el canvas del gauge

gauge.pack(padx=3, pady=3)
SpinboxGauge.pack(padx=5, pady= 5)

#Formulario para graficar Datos

frame1 = ttk.Frame(tab4)
frame1.grid(column=0, row=0)

Cate = ttk.Label(frame1, text="Coloque el nombre de las categorías")
Cate.grid(columnspan=2, row=0, padx=0, pady=2)

ttk.Label (frame1, text="Categoría 1", width=10).grid (column=0, row=3, padx=0, pady=10)
ingre_cat1 = ttk.Entry (frame1, width=20)
ingre_cat1.grid (column =1, row=3)

cat2 = ttk.Label (frame1, text="Categoría 2", width=10).grid (column=0, row=4, padx=0, pady=10)
ingre_cat2 = ttk.Entry (frame1, width=20)
ingre_cat2.grid (column =1, row=4)

ttk.Label (frame1, text="Categoría 3", width=10).grid (column=0, row=5, padx=0, pady=10)
ingre_cat3 = ttk.Entry (frame1, width=20)
ingre_cat3.grid (column =1, row=5)

ttk.Label (frame1, text="Categoría 4", width=10).grid (column=0, row=6, padx=0, pady=10)
ingre_cat4 = ttk.Entry (frame1, width=20)
ingre_cat4.grid (column =1, row=6)


frame2 = ttk.Frame (tab4)
frame2.grid (column=1, row=0)

frecu= ttk.Label (frame2, text= "Coloque la frecuencia de la categoría")
frecu.grid (columnspan=2, row=0, padx=0, pady=2)

frec1 = ttk.Label (frame2, text="Frecuencia 1", width=10).grid (column=0, row=3, padx=0, pady=10)
ingre_fre1 = ttk.Entry (frame2, width=20)
ingre_fre1.grid (column =1, row=3)
frec2 = ttk.Label (frame2, text="Frecuencia 2", width=10).grid (column=0, row=4, padx=0, pady=10)
ingre_fre2 = ttk.Entry (frame2, width=20)
ingre_fre2.grid (column =1, row=4)
frec3 = ttk.Label (frame2, text="Frecuencia 3", width=10).grid (column=0, row=5, padx=0, pady=10)
ingre_fre3 = ttk.Entry (frame2, width=20)
ingre_fre3.grid (column =1, row=5)
frec4 = ttk.Label (frame2, text="Frecuencia 4", width=10).grid (column=0, row=6, padx=0, pady=10)
ingre_fre4 = ttk.Entry (frame2, width=20)
ingre_fre4.grid (column =1, row=6)

frame3= ttk.Frame (tab4)
frame3.grid (column=2, row=0)

TITULO = ttk.Label (frame3, text= "Ingrese el título de la gráfica")
TITULO.grid (columnspan=2, row=0, padx=0, pady=2)

ingre_titulo = ttk.Entry (frame3, width= 20)
ingre_titulo.grid (column=1, row=2)

#botón para la gráfica
guardar= ttk.Button (tab4, 
                    width=20,
                    text="Crear Gráfica de Barras",
                    command=grafica)
guardar.grid (columnspan=3, row=13, pady=10)


# Insertar nombres e imagenes
Imagen1= UPP.PhotoImage(file="./Willshapers_glyph.png")
Imagen1 = Imagen1.subsample(4)
ttk.Label(tab5, text="Jorge Adrián Montes Pimentel", font=("arial",15 ,"bold")).grid(column=0, row=0, columnspan=2, sticky="nswe", padx=5)
ttk.Label(tab5, text="231403103 No. de lista 12", font=("arial",15 ,"bold")).grid(column=0, row=1, columnspan=2, sticky="nswe", padx=5)

ttk.Label(tab5, image=Imagen1).grid(column=2, row=0, rowspan=2, sticky="nswe") 
   
barrita= ttk.Progressbar(tab5, length=300, mode="indeterminate")
barrita.grid(column=0, row=2, columnspan=2, sticky="nswe")
ttk.Button(tab5, text="Iniciar", command=barrita.start).grid(column=0, row=3, sticky="nswe", pady=20, padx=5)
ttk.Button(tab5, text="Detener", command=barrita.stop).grid(column=1, row=3, sticky="nswe",pady=20, padx=5)

Imagen2= UPP.PhotoImage(file="./Paula.png")
Imagen2 = Imagen2.subsample(4)
ttk.Label(tab5, text="Paula Martínez Cuatlayotl ", font=("arial",15 ,"bold")).grid(column=3, row=0, padx=5)
ttk.Label(tab5, text="231403094 No. de lista 11", font=("arial",15 ,"bold")).grid(column=3, row=1, padx=5)


ttk.Label(tab5, image=Imagen2).grid(column=4, row=0, rowspan=2, sticky="nswe", padx=5)  
  
canvas = UPP.Canvas(tab5)
canvas.grid(column=3, row=3, padx=5, sticky="nswe", rowspan=4, columnspan=2) #fill= expanción tanto horizontal como vertica

#turtle 
screen = TurtleScreen(canvas) # herramienta independiente para el dibujo
turtle = RawTurtle(screen) # dibuja dentro de la canva creada 
turtle.speed(5) # tiempo/velocidad del dibujo

# Función para dibujar la estrella
def dibujar_estrella():
    turtle.clear()  # Limpiar cualquier dibujo anterior
    for _ in range(5): #estrella de 5 picos
        turtle.forward(100) #dirección hacia adelante dependiendo la dirección en la que la tortuga se mueve y los 100 es la distancia que tiene en px
        turtle.right(144) #cuando la tortuga gira a la derecha dependiendo en no. de grados que en este caso son los 144°
        
# Crear botón para dibujar la estrella
button_estrella = ttk.Button(tab5, 
                            text="Dibujar Estrella", 
                            command=dibujar_estrella)
button_estrella.grid(column=3, row=2, padx=5)


Imagen3= UPP.PhotoImage(file="./Tortuga.png")
Imagen3 = Imagen3.subsample(3)
ttk.Label(tab5, text="Erick Reyes Aguilar", font=("arial",15 ,"bold")).grid(column=0, row=4, columnspan=2, sticky="nswe", padx=5)
ttk.Label(tab5, text="231401005 No de Lista 20", font=("arial",15 ,"bold")).grid(column=0, row=5, columnspan=2, sticky="nswe", padx=5)

ttk.Label(tab5, image=Imagen3).grid(column=2,row=4, rowspan=2, sticky="nswe", padx=5)    

# Función para generar un color aleatorio
def generar_color():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    etiquetaColor.config(text=f"Color: {color}", background=color)

ttk.Label(text="Generador de Color Raro")

# Crear el botón
botonColor = ttk.Button(tab5, text="Generar color", command=generar_color)
botonColor.grid(column=0, columnspan=2, row=6, padx=5)

# Crear la etiqueta que mostrará el color
etiquetaColor = ttk.Label(tab5, text="Presiona el botón para un color raro", font=("Arial", 12))
etiquetaColor.grid(column=0, columnspan=2, row=7, padx=5)

ventana.mainloop()