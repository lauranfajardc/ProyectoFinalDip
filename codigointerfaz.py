import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from os import path
from skimage import io, exposure, img_as_ubyte
import numpy as np
import matplotlib.pyplot as plt
import pylab
import cv2
import tkinter.filedialog as filedialog
import urllib.request
from io import BytesIO
import base64
from IPython.display import HTML
import urllib.parse

pylab.rcParams['figure.figsize'] = (3.0, 3.0)

class TumoresCerebralesApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tumores Cerebrales")
        self.master.geometry("500x500")
        self.current_page = 1
        # Crear widgets para la página 1
        self.labeli = tk.Label(self.master, text="Detección de ",font=("Arial Bold", 40))
        self.labeli.pack(pady=10)
        self.labele = tk.Label(self.master, text="Tumores Cerebrales",font=("Arial Bold", 40))
        self.labele.pack(pady=10)
        
        self.imageni = Image.open("C:\\Users\\ASUS\\Downloads\\iniciar.jpg")
        self.imagen_i = self.imageni.resize((300, 200))
        self.imagen_botoni = ImageTk.PhotoImage(self.imagen_i)
        self.label_imageni = tk.Label(self.master, image=self.imagen_botoni)
        self.label_imageni.pack()
        
        self.btn_iniciar = tk.Button(self.master, text="Iniciar", command=self.ir_pagina1)
        self.btn_iniciar.pack(pady=10)
        
        # Primera página
        self.pagina1 = tk.Frame(self.master)
        self.imagei = Image.open('C:\\Users\\ASUS\\Downloads\\brain.jpg')
        self.image_i = self.imagei.resize((400, 300))
        self.image_botoni = ImageTk.PhotoImage(self.image_i)
        self.label_imagei = tk.Label(self.pagina1, image=self.image_botoni)
        self.label_imagei.pack()
        self.btn_salir = tk.Button(self.pagina1, text="Salir", command=self.master.quit)
        self.btn_salir.pack(side=tk.RIGHT, padx=10)
        self.btn_pagina2 = tk.Button(self.pagina1, text="Procesamiento", command=self.ir_pagina2)
        self.btn_pagina2.pack(side=tk.RIGHT, padx=10)
        self.btn_pagina4 = tk.Button(self.pagina1, text="Archivo", command=self.ir_pagina5)
        self.btn_pagina4.pack(side=tk.RIGHT, padx=10)

        # Opcion de imagen
        self.pagina2 = tk.Frame(self.master)
        self.titulo2 = tk.Label(self.pagina2, text="Subir una imagen")
        self.btn_volver1 = tk.Button(self.pagina2, text="Volver", command=self.ir_pagina1)
        self.btn_volver1.pack(side=tk.LEFT, padx=10)
        self.btn_subir = tk.Button(self.pagina2, text="Subir imagen", command=self.subir_imagen)
        self.btn_subir.pack(side=tk.LEFT, padx=10)
        self.btn_salir2 = tk.Button(self.pagina2, text="Salir", command=self.master.quit)
        self.btn_salir2.pack(side=tk.RIGHT, padx=10)
        self.btn_pagina3 = tk.Button(self.pagina2, text="Base de datos", command=self.ir_pagina3)
        self.btn_pagina3.pack(side=tk.LEFT, padx=10)

        # Base de datos
        self.pagina3 = tk.Frame(self.master)
        self.titulo3 = tk.Label(self.pagina3, text="Base de Datos")
        
        self.imagen1 = Image.open("C:\\Users\\ASUS\\Downloads\\Brain_Tumor_Detection-20230428T205405Z-001\\Brain_Tumor_Detection\\yes\\y145.jpg")
        self.imagen_redimensionada1 = self.imagen1.resize((100, 100))
        self.imagen_boton1 = ImageTk.PhotoImage(self.imagen_redimensionada1)
        self.boton = tk.Button(self.pagina3, image=self.imagen_boton1, command=self.ir_pagina4)
        self.boton.pack()
        self.imagen2 = Image.open("C:\\Users\\ASUS\\Documents\\BaseDatosRM\\no1035.jpg")
        self.imagen_redimensionada2 = self.imagen2.resize((100, 100))
        self.imagen_boton2= ImageTk.PhotoImage(self.imagen_redimensionada2)
        self.boton = tk.Button(self.pagina3, image=self.imagen_boton2, command=self.ir_pagina4)
        self.boton.pack()
        self.imagen3 = Image.open("C:\\Users\\ASUS\\Documents\\BaseDatosRM\\no1115.jpg")
        self.imagen_redimensionada3 = self.imagen3.resize((100, 100))
        self.imagen_boton3 = ImageTk.PhotoImage(self.imagen_redimensionada3)
        self.boton = tk.Button(self.pagina3, image=self.imagen_boton3, command=self.ir_pagina4)
        self.boton.pack()
        self.imagen = Image.open("C:\\Users\\ASUS\\Documents\\BaseDatosRM\\y15.jpg")
        self.imagen_redimensionada = self.imagen.resize((100, 100))
        self.imagen_boton = ImageTk.PhotoImage(self.imagen_redimensionada)
        self.boton = tk.Button(self.pagina3, image=self.imagen_boton, command=self.ir_pagina4)
        self.boton.pack()
        self.imagen5 = Image.open("C:\\Users\\ASUS\\Documents\\BaseDatosRM\\y1051.jpg")
        self.imagen_redimensionada5 = self.imagen5.resize((100, 100))
        self.imagen_boton5 = ImageTk.PhotoImage(self.imagen_redimensionada5)
        self.boton = tk.Button(self.pagina3, image=self.imagen_boton5, command=self.ir_pagina4)
        self.boton.pack(side="right")
        self.imagen6 = Image.open("C:\\Users\\ASUS\\Documents\\BaseDatosRM\\y1159.jpg")
        self.imagen_redimensionada6 = self.imagen6.resize((100, 100))
        self.imagen_boton6 = ImageTk.PhotoImage(self.imagen_redimensionada6)
        self.boton = tk.Button(self.pagina3, image=self.imagen_boton6, command=self.ir_pagina4)
        self.boton.pack(side="right")
        self.imagen7 = Image.open("C:\\Users\\ASUS\\Documents\\BaseDatosRM\\y1276.jpg")
        self.imagen_redimensionada7 = self.imagen7.resize((100, 100))
        self.imagen_boton7 = ImageTk.PhotoImage(self.imagen_redimensionada7)
        self.boton = tk.Button(self.pagina3, image=self.imagen_boton7, command=self.ir_pagina4)
        self.boton.pack(side="right")
        self.boton_pagina2 = tk.Button(self.pagina3, text="Volver", command=self.ir_pagina2)
        self.boton_pagina2.pack(side="left")
        self.boton_salir = tk.Button(self.pagina3, text="Salir", command=self.master.quit)
        self.boton_salir.pack(side="right")

         #Operaciones
        self.pagina4 = tk.Frame(self.master)
        self.label4 = tk.Label(self.pagina4, text="Operaciones",font=("Arial Bold", 12))
        self.label4.pack(pady=10)
        
        self.boton_base = tk.Button(self.pagina4, text="Mejorar la calidad de la imagen",command=self.ir_pagina7)
        self.boton_base.pack(pady=10)
        
        self.boton_base = tk.Button(self.pagina4, text="Umbralización",command=self.ir_pagina8)
        self.boton_base.pack(pady=10)
        
        self.boton_base = tk.Button(self.pagina4, text="Segmentación",command=self.ir_pagina11)
        self.boton_base.pack(pady=10)
        
        self.boton_volver = tk.Button(self.pagina4, text="Volver", command=self.ir_pagina2)
        self.boton_volver.pack(side=tk.RIGHT, padx=10)
        
        self.boton_salir2 = tk.Button(self.pagina4, text="Salir", command=self.master.quit)
        self.boton_salir2.pack(side=tk.LEFT, padx=10)       
    
        
        #Mejorar la calidad de la imagen
        self.pagina7 = tk.Frame(self.master)
        self.label_titulo7 = tk.Label(self.pagina7, text="Mejorar la calidad de la imagen")
        self.label_titulo7.pack()
        self.boton_base = tk.Button(self.pagina7, text="Nitidez",command=self.ir_pagina10)
        self.boton_base.pack(pady=10)
        self.boton_base = tk.Button(self.pagina7, text="Ecualización del histograma",command=self.ir_pagina9)
        self.boton_base.pack(pady=10)
        self.boton_pagina4_6 = tk.Button(self.pagina7, text="Volver", command=self.ir_pagina4)
        self.boton_pagina4_6.pack(side="left")
        self.boton_salir7 = tk.Button(self.pagina7, text="Salir", command=self.master.quit)
        self.boton_salir7.pack(side="right")
               
        #Archivo
        self.pagina5 = tk.Frame(self.master)
        self.imagenes_umbralizadas_pagina5 = []
        
        self.label_titulo5 = tk.Label(self.pagina5, text="Archivo")
        self.label_titulo5.pack()
        self.boton_pagina1_5 = tk.Button(self.pagina5, text="Volver", command=self.ir_pagina1)
        self.boton_pagina1_5.pack(side="left")
        self.boton_salir5 = tk.Button(self.pagina5, text="Salir", command=self.master.quit)
        self.boton_salir5.pack(side="right")
        
        #umbralización
        self.pagina8 = tk.Frame(self.master)
        self.label_titulo8 = tk.Label(self.pagina8, text="Interfaz de umbralización de imágenes")
        self.label_imagen = tk.Label(self.pagina8)
        self.label_imagen_umbralizada = tk.Label(self.pagina8)
        self.label_imagen.pack(side="left")
        self.label_imagen_umbralizada.pack(side="right")
        self.lbl1 = tk.Label(self.pagina8, text="Imagen umbralizada: ", font=("Arial Bold", 12))
        self.lbl1.pack(side="bottom")
        self.boton_pagina1_8 = tk.Button(self.pagina8, text="Volver", command=self.ir_pagina4)
        self.boton_pagina1_8.pack()
        self.btn_pagina8 = tk.Button(self.pagina8, text="Archivo", command=self.ir_pagina5)
        self.btn_pagina8.pack()
        self.btn_p = tk.Button(self.pagina8, text="Umbralizar", command=self.umbralizar_imagen)
        self.btn_p.pack()
        
        # Ecualizacion del histograma
        self.pagina9 = tk.Frame(self.master)
        self.label_titulo9 = tk.Label(self.pagina9, text="Ecualizacion del histograma")
        self.label_imagen = tk.Label(self.pagina9)
        self.label_imagen_ecualizada = tk.Label(self.pagina9)
        self.label_imagen.pack(side="left")
        self.label_imagen_ecualizada.pack(side="right")
        self.lbl1 = tk.Label(self.pagina9, text="Imagen Ecualizada: ", font=("Arial Bold", 12))
        self.lbl1.pack(side="bottom")
        self.boton_pagina1_8 = tk.Button(self.pagina9, text="Volver", command=self.ir_pagina4)
        self.boton_pagina1_8.pack()
        self.btn_pagina8 = tk.Button(self.pagina9, text="Archivo", command=self.ir_pagina5)
        self.btn_pagina8.pack()
        self.btn_p1 = tk.Button(self.pagina9, text="Ecualizar", command=self.mostrar_imagen_ecualizada)
        self.btn_p1.pack()
        
        # Nitidez
        self.pagina10 = tk.Frame(self.master)
        self.label_titulo10 = tk.Label(self.pagina10, text="Nitidez")
        self.label_imagen_nitida = tk.Label(self.pagina10)
        self.label_imagen_nitida.pack(side="right")
        self.lbl1 = tk.Label(self.pagina10, text="Imagen Con Nitidez: ", font=("Arial Bold", 12))
        self.lbl1.pack(side="bottom")
        self.boton_pagina10 = tk.Button(self.pagina10, text="Volver", command=self.ir_pagina4)
        self.boton_pagina10.pack()
        self.btn_pagina10 = tk.Button(self.pagina10, text="Archivo", command=self.ir_pagina5)
        self.btn_pagina10.pack()
        self.btn_p = tk.Button(self.pagina10, text="Nitidez",command=self.mostrar_imagen_nitidez)
        self.btn_p.pack()
       
        # Segmentación
        self.pagina11 = tk.Frame(self.master)
        self.label_titulo11 = tk.Label(self.pagina11, text="Segmentación Método Canny")
        self.label_imagen_segmentada = tk.Label(self.pagina11)
        self.label_imagen_segmentada.pack(side="left")
        self.boton_pagina11= tk.Button(self.pagina11, text="Volver", command=self.ir_pagina4)
        self.boton_pagina11.pack()
        self.btn_pagina11 = tk.Button(self.pagina11, text="Archivo", command=self.ir_pagina5)
        self.btn_pagina11.pack()
        self.btn_p = tk.Button(self.pagina11, text="Segmentar",command=self.mostrar_imagen_segmentada2)
        self.btn_p.pack()
        self.btn_segmentar = tk.Button(self.pagina11, text="Segmentar Nitidez", command=self.segmentar_imagen)
        self.btn_segmentar.pack()
        self.btn_aplicar_filtro = tk.Button(self.pagina11, text="Aplicar Filtro", command=self.aplicar_filtro)
        self.btn_aplicar_filtro.pack()
        self.btn_ecualizar = tk.Button(self.pagina11, text="Segmentar imagen ecualizada",command=self.segmentar_imagen3)
        self.btn_ecualizar.pack()
        self.label_imagen_filtrada = tk.Label(self.pagina11)
        self.label_imagen_filtrada.pack(side="left")
        self.btn_descargar = tk.Button(self.pagina11, text="Descargar", command=self.descargar_imagen)
        self.btn_descargar.pack()
        
   
    def aplicar_filtro(self):
        if hasattr(self, 'imagen'):
            imagen_segmentada = self.segmentacion2()
            imagen_gris = Image.fromarray(imagen_segmentada).convert('L')
            self.imagen_gris_np = np.array(imagen_gris)
            imagen_segmentada_np = np.array(self.imagen_gris_np)
            imagen_filtrada = self.filtro(imagen_segmentada_np)
            self.imagen_filtrada_pil = Image.fromarray(imagen_filtrada)
    
            self.imagen_filtrada_mostrada = ImageTk.PhotoImage(self.imagen_filtrada_pil)
            self.label_imagen_filtrada.config(image=self.imagen_filtrada_mostrada)
            self.label_imagen_filtrada.image = self.imagen_filtrada_mostrada

    def descargar_imagen(self):
        if hasattr(self, 'imagen_filtrada_pil'):
            filename = "imagen_filtrada.png"  # Nombre de archivo de la imagen a descargar
            self.imagen_filtrada_pil.save(filename)
            print("La imagen filtrada se ha descargado correctamente.")
        
    
    def filtro(self, imagen_segmentada):
        imagen_segmentada_np = np.array(imagen_segmentada)
        kernel_size = 5
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        imagen_filtrada = cv2.dilate(imagen_segmentada_np, kernel)
        return imagen_filtrada       
    
    def segmentacion2(self):
        if hasattr(self, 'imagen'):
            imagen_gris = self.imagen.convert('L')
            imagen_np = np.array(imagen_gris)
            canny_building = cv2.Canny(imagen_np, 100, 300)
            return canny_building

    def mostrar_imagen_segmentada2(self):
        imagen_segmentada = self.segmentacion2()
        imagen_segmentada_pil = Image.fromarray(imagen_segmentada)
        self.imagen_segmentada_mostrada = ImageTk.PhotoImage(imagen_segmentada_pil)
        self.label_imagen_segmentada.config(image=self.imagen_segmentada_mostrada)
        self.label_imagen_segmentada.image = self.imagen_segmentada_mostrada
        self.label_imagen_segmentada_nueva = tk.Label(self.pagina5, image=self.imagen_segmentada_mostrada)
        self.label_imagen_segmentada_nueva.pack()  
        
    def mostrar_imagen_segmentada(self):
        imagen_segmentada = self.segmentacion()
        imagen_segmentada_pil = Image.fromarray(imagen_segmentada)
        self.imagen_segmentada_mostrada = ImageTk.PhotoImage(imagen_segmentada_pil)
        self.label_imagen_segmentada.config(image=self.imagen_segmentada_mostrada)
        self.label_imagen_segmentada.image = self.imagen_segmentada_mostrada
        self.label_imagen_segmentada_nueva = tk.Label(self.pagina5, image=self.imagen_segmentada_mostrada)
        self.label_imagen_segmentada_nueva.pack()
        
    def segmentar_imagen(self):
        if hasattr(self, 'imagen'):
            imagen_nitida = self.nitidez()
            imagen_gris = Image.fromarray(imagen_nitida).convert('L')
            imagen_gris_np = np.array(imagen_gris)
            imagen_segmentada = self.segmentacion(imagen_gris_np)
            imagen_segmentada_pil = Image.fromarray(imagen_segmentada)
            self.imagen_segmentada_mostrada = ImageTk.PhotoImage(imagen_segmentada_pil)
            self.label_imagen_segmentada.config(image=self.imagen_segmentada_mostrada)
            self.label_imagen_segmentada.image = self.imagen_segmentada_mostrada
            self.label_imagen_segmentada_nueva = tk.Label(self.pagina11, image=self.imagen_segmentada_mostrada)
            self.label_imagen_segmentada_nueva.pack()

    def segmentar_imagen3(self):
        if hasattr(self, 'imagen'):
            imagen_nitida = self.ecualizacion()
            imagen_gris = Image.fromarray(imagen_nitida).convert('L')
            imagen_gris_np = np.array(imagen_gris)
            imagen_segmentada = self.segmentacion(imagen_gris_np)
            imagen_segmentada_pil = Image.fromarray(imagen_segmentada)
            self.imagen_segmentada_mostrada = ImageTk.PhotoImage(imagen_segmentada_pil)
            self.label_imagen_segmentada.config(image=self.imagen_segmentada_mostrada)
            self.label_imagen_segmentada.image = self.imagen_segmentada_mostrada
            self.label_imagen_segmentada_nueva = tk.Label(self.pagina11, image=self.imagen_segmentada_mostrada)
            self.label_imagen_segmentada_nueva.pack()

    def mostrar_imagen_nitidez(self):
        if hasattr(self, 'imagen'):
            imagen_nitida = self.nitidez()
            imagen_nitida_pil = Image.fromarray(imagen_nitida)
            self.imagen_nitida_mostrada = ImageTk.PhotoImage(imagen_nitida_pil)
            self.label_imagen_nitida.config(image=self.imagen_nitida_mostrada)
            self.label_imagen_nitida.image = self.imagen_nitida_mostrada
            self.label_imagen_nitida_nueva = tk.Label(self.pagina5, image=self.imagen_nitida_mostrada)
            self.label_imagen_nitida_nueva.pack()
      
            
    def nitidez(self):
        coeficientes = np.array([[0, 1, 0],
                                 [1, -5, 1],
                                 [0, 1, 0]]) * -1
        if hasattr(self, 'imagen'):
            imagen_gris = self.imagen.convert('L')
            imagen_np = np.array(imagen_gris)
            sharpened = cv2.filter2D(imagen_np, -1, coeficientes)
            return sharpened

    def segmentacion(self, imagen_nitida):
        imagen_gris = Image.fromarray(imagen_nitida.astype('uint8')).convert('L')
        imagen_gris_np = np.array(imagen_gris)
        canny_building = cv2.Canny(imagen_gris_np, 100, 300)
        return canny_building
    

        
    def mostrar_imagen_ecualizada(self):
        imagen_ecualizada = self.ecualizacion()
        imagen_ecualizada_pil = Image.fromarray(imagen_ecualizada)
        self.imagen_ecualizada_mostrada = ImageTk.PhotoImage(imagen_ecualizada_pil)
        self.label_imagen_ecualizada.config(image=self.imagen_ecualizada_mostrada)
        self.label_imagen_ecualizada.image = self.imagen_ecualizada_mostrada
        self.label_imagen_ecualizada_nueva = tk.Label(self.pagina5, image=self.imagen_ecualizada_mostrada)
        self.label_imagen_ecualizada_nueva.pack()
    
    def ecualizacion(self):
        if hasattr(self, 'imagen'):
            imagen_gris = self.imagen.convert('L')
            imagen_np = np.array(imagen_gris)
            hist_eq_img = cv2.equalizeHist(imagen_np)
            return hist_eq_img

    
    def subir_imagen(self):
        self.ruta_imagen = filedialog.askopenfilename(initialdir="/", title="Seleccionar archivo", filetypes=(("Archivos de imagen", "*.png *.jpg *.jpeg"), ("Todos los archivos", "*.*")))
        self.imagen = Image.open(self.ruta_imagen)
        self.imagen.thumbnail((300, 300))  # Redimensionar la imagen para mostrarla en la ventana
        self.imagen_mostrada = ImageTk.PhotoImage(self.imagen)
        self.label_imagen.configure(image=self.imagen_mostrada)
        self.label_imagen.image = self.imagen_mostrada
        
        self.pagina1.pack_forget()
        self.pagina2.pack_forget()
        self.pagina3.pack_forget()
        self.pagina5.pack_forget()
        self.pagina7.pack_forget()
        self.pagina8.pack_forget()
        self.pagina9.pack_forget()
        self.pagina10.pack_forget()
        self.pagina11.pack_forget()
        self.pagina4.pack()
        
    def umbralizar_imagen(self):
            if hasattr(self, 'imagen'):
                umbral = 170
                imagen_gris = self.imagen.convert('L')
                imagen_umbralizada = imagen_gris.point(lambda p: p > umbral and 255)
                #self.imagenes_umbralizadas_pagina5.append(imagen_umbralizada)
                self.imagen_umbralizada_mostrada = ImageTk.PhotoImage(imagen_umbralizada)
                self.imagenes_umbralizadas_pagina5.append(self.imagen_umbralizada_mostrada)
                self.label_imagen_umbralizada.configure(image=self.imagen_umbralizada_mostrada)
                self.label_imagen_umbralizada.image =self.imagen_umbralizada_mostrada
                self.label_imagen_umbralizada_nueva = tk.Label(self.pagina5, image=self.imagen_umbralizada_mostrada)
                self.label_imagen_umbralizada_nueva.pack()


    def ir_pagina1(self):
        self.btn_iniciar.pack_forget()
        self.labeli.pack_forget()
        self.label_imageni.pack_forget()
        self.pagina2.pack_forget()
        self.pagina3.pack_forget()
        self.pagina4.pack_forget()
        self.pagina5.pack_forget()
        self.pagina7.pack_forget()
        self.pagina8.pack_forget()
        self.pagina9.pack_forget()
        self.pagina10.pack_forget()
        self.pagina11.pack_forget()
        self.pagina1.pack()
            
    def ir_pagina2(self):
         self.pagina1.pack_forget()
         self.pagina3.pack_forget()
         self.pagina4.pack_forget()
         self.pagina5.pack_forget()
         self.pagina7.pack_forget()
         self.pagina8.pack_forget()
         self.pagina9.pack_forget()
         self.pagina10.pack_forget()
         self.pagina11.pack_forget()
         self.pagina2.pack()
            
    def ir_pagina3(self):
        self.pagina1.pack_forget()
        self.pagina2.pack_forget()
        self.pagina4.pack_forget()
        self.pagina5.pack_forget()
        self.pagina7.pack_forget()
        self.pagina8.pack_forget()
        self.pagina9.pack_forget()
        self.pagina10.pack_forget()
        self.pagina11.pack_forget()
        self.pagina3.pack()
            
    def ir_pagina4(self):
         self.pagina1.pack_forget()
         self.pagina2.pack_forget()
         self.pagina3.pack_forget()
         self.pagina5.pack_forget()
         self.pagina7.pack_forget()
         self.pagina8.pack_forget()
         self.pagina9.pack_forget()
         self.pagina10.pack_forget()
         self.pagina11.pack_forget()
         self.pagina4.pack()
         
    def ir_pagina5(self):
        self.pagina1.pack_forget()
        self.pagina2.pack_forget()
        self.pagina3.pack_forget()
        self.pagina4.pack_forget()
        self.pagina7.pack_forget()
        self.pagina8.pack_forget()
        self.pagina9.pack_forget()
        self.pagina10.pack_forget()
        self.pagina11.pack_forget()
        self.pagina5.pack()

    def ir_pagina7(self):
        self.pagina1.pack_forget()
        self.pagina2.pack_forget()
        self.pagina3.pack_forget()
        self.pagina4.pack_forget()
        self.pagina5.pack_forget()
        self.pagina8.pack_forget()
        self.pagina9.pack_forget()
        self.pagina10.pack_forget()
        self.pagina11.pack_forget()
        self.pagina7.pack()
        
    def ir_pagina8(self):
        self.pagina1.pack_forget()
        self.pagina2.pack_forget()
        self.pagina3.pack_forget()
        self.pagina4.pack_forget()
        self.pagina5.pack_forget()
        self.pagina7.pack_forget()
        self.pagina9.pack_forget()
        self.pagina10.pack_forget()
        self.pagina11.pack_forget()
        self.pagina8.pack()
        
    def ir_pagina9(self):
        self.pagina1.pack_forget()
        self.pagina2.pack_forget()
        self.pagina3.pack_forget()
        self.pagina4.pack_forget()
        self.pagina5.pack_forget()
        self.pagina7.pack_forget()
        self.pagina8.pack_forget()
        self.pagina10.pack_forget()
        self.pagina11.pack_forget()
        self.pagina9.pack()
        
    def ir_pagina10(self):
        self.pagina1.pack_forget()
        self.pagina2.pack_forget()
        self.pagina3.pack_forget()
        self.pagina4.pack_forget()
        self.pagina5.pack_forget()
        self.pagina7.pack_forget()
        self.pagina8.pack_forget()
        self.pagina9.pack_forget()
        self.pagina11.pack_forget()
        self.pagina10.pack()
      
    def ir_pagina11(self):
        self.pagina1.pack_forget()
        self.pagina2.pack_forget()
        self.pagina3.pack_forget()
        self.pagina4.pack_forget()
        self.pagina5.pack_forget()
        self.pagina7.pack_forget()
        self.pagina8.pack_forget()
        self.pagina9.pack_forget()
        self.pagina10.pack_forget()
        self.pagina11.pack()
        
        
root = tk.Tk()
app = TumoresCerebralesApp(root)

# Iniciar el bucle principal de la ventana
root.mainloop()