#Encabezado
# Sección: crea el archivo que contendrá el encabezado de la factura.

archivo = open("encabezadofactura.txt", "w")              # Abre (o crea) 'encabezadofactura.txt' en modo escritura ("w"). Si existe, lo sobrescribe.
archivo.write("=====================================\n")
archivo.write("        FACTURA DE COMPRA\n")              
archivo.write("=====================================\n")
archivo.write("Cliente: Jhojan Silva\n")                  # Escribe el nombre del cliente 
archivo.write("Fecha: 08/09/2025\n")                      # Escribe la fecha de la factura 
archivo.close()                                          
print("Encabezado creado.")                               

#lista de productos

archivo2 = open("listadeproductos.txt","w")               # Abre (o crea) 'listadeproductos.txt' en modo escritura; sobrescribe si existe.
archivo2.write("==========================================================================\n") 
archivo2.write("            LISTA DE PRODUCTOS\n")          
archivo2.write("==========================================================================\n")  
archivo2.write("1. Teclado mecanico 120.000$..............................................\n")  
archivo2.write("2. Mause gamer 70.000$....................................................\n")  
archivo2.write("3. Audifonos bluetoon 200.000.............................................\n")  
archivo2.write("4. Pc gamer 8.900.000$....................................................\n")  
archivo2.write("5. Monitor huawei 700.000$................................................\n")  
archivo2.write("6. Mausepad 20.000$.......................................................\n")   
archivo2.write("7. Silla gamer gamer 670.000$.............................................\n")   
archivo2.write("==========================================================================\n")  
archivo2.close()                                         

# Totales

archivo2 = open("totales.txt", "w")                      
archivo2.write("==========================================================================\n")  
archivo2.write("Subtotal:   $690.000\n")                 
archivo2.write("IVA (19%):  $131.100\n")                 
archivo2.write("TOTAL:      $821.100\n")                 
archivo2.write("==========================================================================\n")  
archivo2.close()                                         # Cierra el archivo de totales.
print("Totales creados.")

# Observaciones

archivo3 = open("mensajes.txt", "w")                     # Abre (o crea) 'mensajes.txt' en modo escritura.
archivo3.write("Gracias por su compra.\n")                 
archivo3.write("No se aceptan devoluciones sin factura.\n")
archivo3.close()                                         # Cierra el archivo de mensajes.
print("Observaciones creadas.")                          # Informa que se creó el archivo de observaciones.

# Leer los archivos
# Sección: abre el archivo de lista de productos en modo lectura y muestra su contenido por consola.

archivo1 = open("listadeproductos.txt", "r")             # Abre 'listadeproductos.txt' en modo lectura r.
contenido = archivo1.read()                              # Lee todo el contenido del archivo y lo guarda en la variable 'contenido'.
archivo1.close()                                         # Cierra el archivo que se abrió para lectura.

print("\nContenido de los productos en la factura:\n")    
print(contenido)                                         # Imprime el contenido leído del archivo de productos.

# Agregar datos adicionales al final del archivo de totales
# Sección: abre (o crea) otro archivo para añadir información final (modo append).

archivo2 = open("factura_totales.txt", "a")              # Abre 'factura_totales.txt' en modo "a" (append): agrega al final sin sobrescribir.
archivo2.write("Método de pago: Efectivo\n")            
archivo2.close()                                         # Cierra el archivo tras la escritura.
print("Gracias por su compra. Vuelva pronto.")           
print    ("==========================================================================\n") 
