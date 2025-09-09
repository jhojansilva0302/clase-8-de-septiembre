# Agenda de estudiantes 
# Se crea el archivo 'base_de_datos.txt'
archivo = open("base_de_datos.txt", "w", encoding="utf-8")  # abre o crea el archivo en modo escritura
archivo = open("base_de_datos.txt","w",encoding="utf-8")   # abre o crea el archivo en modo escritura

# escribimos todos los estudiantes de la base en formato cc,nombre,telefono,correo
archivo.write("1001202162,JOAN SEBASTIAN BORDA CASTIBLANCO,3105885793,johansebastianborda@gmail.com\n")
archivo.write("1015397949,DAVID ALEJANDRO APARICIO ROMERO,3204308710,davidaar05@gmail.com\n")
archivo.write("1016009825,MIGEL ESTEBAN MARTINEZ VARON,3219404978,miguelmartinezvaron32143@gmail.com\n")
archivo.write("1019989868,STEBAN CARRIZOSA ORTEGON,3006898362,carrizosaortegon.steban@gmail.com\n")
archivo.write("1028481891,DAVID SANTIAGO CAMELO CRUZ,3193866413,johansebastianborda@gmail.com\n")
archivo.write("1029520748,JOSEPH NICOLAS TORRES CASTELBLANCO,3122224003,josephnicolastorres6@gmail.com\n")
archivo.write("1047041996,ANDRES CAMILO GUARDIA ALTAMAR,3219404978,miguelmartinezvaron32143@gmail.com\n")
archivo.write("1019989868,STEBAN CARRIZOSA ORTEGON,3017852867,chamolocoporsiempre@gmail.com\n")
archivo.write("1070384473,NATALIA AVILAN LAROTTA,3105281043,nataliaavilan24@gmail.co\n")
archivo.write("1141114537,OSCAR FELIPE GUACANEME SANCHEZ,3125056545,guacanemeoscarfelipe@gmail.com\n")
archivo.write("1142714477,DANNA VALENTINA DIAZ GUALDRON,3229150145,dannadiazgualdron@gmail.com\n")
archivo.write("1193552312,DIEGO ALEJANDRO SANCHEZ LOPEZ,3026826919,hiphopclan99@gmail.com\n")
archivo.write("80154727,MARIO DAVIS AGUILLON PUENTES,3188676690,aguillondavis@gmail.com\n")
archivo.write("1013117356,JULIAN ANDRES MONROY MELO,3112237515,julianjamm321123@gmail.com\n")
archivo.write("1028486643,SAMUEL ANDRES PINZON MONROY,3203985749,yosoyanel02@gmail.com\n")
archivo.write("1071914553,JHOJAN STIVEN SILVA GARCIA,3115867655,jhojansilva0302@gmail.com\n")
archivo.write("1072746935,JOHAN SEBASTIAN RODRIGUEZ GONZALEZ,3053039737,johansebastian201107@gmail.com\n")
archivo.write("1001329164,MISCHAELL ANDRES PULIDO SALDAÑA,3227336328,katerinaguilar12345@gmail.com\n")
archivo.write("80166347,ERWIN JOYA PULIDO,3196479318,ejoya7@soy.sena.edu.co\n")

archivo.close()   # cerramos el archivo
print("documento en txt")   # confirmamos en pantalla
         # escribe el título en el archivo
archivo.close()                                             # cierra el archivo
print("documento en txt")                                   # mensaje de confirmación en consola


# Función para cargar todos los estudiantes desde el archivo
def cargar_estudiantes():
    estudiantes = []                                        # lista vacía donde guardo los datos
    with open("base_de_datos.txt", "r", encoding="utf-8") as archivo:  # abrimos en lectura
        lineas = archivo.readlines()                        # leemos todas las líneas
        for linea in lineas[1:]:                            # ignoramos la primera línea que es el titulo
            linea = linea.strip()                           # se quita espacios y salto de línea
            if linea:                                       # si la línea no está vacía
                cc, nombre, telefono, correo = linea.split(",")  # se divide en 4 partes separadas por coma
                estudiantes.append({
                    "cc": int(cc),                          # convertimos la cédula a un número entero
                    "nombre": nombre,                       # se guarda el nombre
                    "Telefono": telefono,                   # se guarda el teléfono
                    "Correo": correo                        # se guarda el correo
                })
    return estudiantes                                      # devolvemos toda la lista 


# Función para guardar la lista de estudiantes en el archivo
def guardar_estudiantes(estudiantes):
    with open("base_de_datos.txt", "w", encoding="utf-8") as archivo:  # abrimos para escritura
        archivo.write("base de datos de estudiantes\n")     # reescribimos el título
        for e in estudiantes:                               # recorremos cada estudiante
            archivo.write(f"{e['cc']},{e['nombre']},{e['Telefono']},{e['Correo']}\n")  
            # escribimos los datos separados por coma
    print("💾 Cambios guardados en base_de_datos.txt")      # confirmamos al usuario la accion


# OPCIONES DE LA AGENDA

# Mostrar todos los estudiantes
def mostrar_estudiantes(estudiantes):
    print("\n=== LISTA DE ESTUDIANTES ===")
    if not estudiantes:                                     # si la lista está vacía
        print("No hay estudiantes registrados.")            # avisamos al usuario
    else:
        for e in estudiantes:                               # recorremos la lista
            print(f"{e['cc']} - {e['nombre']} - {e['Telefono']} - {e['Correo']}")  
            # mostramos los datos

# Buscar un estudiante por cédula
def buscar_estudiante(estudiantes):
    print("\n=== BUSCAR ESTUDIANTE ===")
    cc = int(input("Ingrese la cédula del estudiante: "))   # pedimos la cédula
    encontrado = next((e for e in estudiantes if e["cc"] == cc), None)  
    # buscamos una igual en la lista
    if encontrado:                                          # si si esta
        print(f"Encontrado: {encontrado['nombre']} - {encontrado['Telefono']} - {encontrado['Correo']}")
    else:                                                   # si no esta
        print("Estudiante no registrado.")

# Agregar un estudiante
def agregar_estudiante(estudiantes):
    print("\n=== AGREGAR ESTUDIANTE ===")
    cc = int(input("Cédula: "))                             # pedimos cédula
    if any(e["cc"] == cc for e in estudiantes):             # verificamos si ya hay otra igual
        print("⚠️ Ya existe un estudiante con esa cédula.") #si hay otra igual
        return
    nombre = input("Nombre: ")                              # pedimos nombre
    telefono = input("Teléfono: ")                          # pedimos teléfono
    correo = input("Correo: ")                              # pedimos correo
    estudiantes.append({"cc": cc, "nombre": nombre, "Telefono": telefono, "Correo": correo})  
    # añadimos el estudiante a la lista
    guardar_estudiantes(estudiantes)                        # guardamos en el archivo
    print("✅ Estudiante agregado con éxito.")              # confirmamos que si se pudo

# Modificar un estudiante
def modificar_estudiante(estudiantes):
    print("\n=== MODIFICAR ESTUDIANTE ===")
    cc = int(input("Ingrese la cédula del estudiante: "))   # pedimos cédula
    encontrado = next((e for e in estudiantes if e["cc"] == cc), None)  
    if not encontrado:                                      # si no esta
        print("Estudiante no encontrado.")
        return
    print(f"Modificando a {encontrado['nombre']}")          # mostramos a quién van modificar
    encontrado["nombre"] = input("Nuevo nombre: ") or encontrado["nombre"]  
    encontrado["Telefono"] = input("Nuevo teléfono: ") or encontrado["Telefono"]  
    encontrado["Correo"] = input("Nuevo correo: ") or encontrado["Correo"]  
    guardar_estudiantes(estudiantes)                        # guardamos cambios
    print("✅ Datos actualizados.")                        # confirmamos

# Eliminar un estudiante
def eliminar_estudiante(estudiantes):
    print("\n=== ELIMINAR ESTUDIANTE ===")
    cc = int(input("Ingrese la cédula del estudiante: "))   # pedimos la cédula
    encontrado = next((e for e in estudiantes if e["cc"] == cc), None)  
    if not encontrado:                                      # si no esta
        print("Estudiante no encontrado.")
        return
    estudiantes.remove(encontrado)                          # lo quitamos de la lista
    guardar_estudiantes(estudiantes)                        # guardamos
    print("🗑️ Estudiante eliminado.")                      # confirmamos


 #MENÚ 
def menu():
    estudiantes = cargar_estudiantes()                      # cargamos estudiantes del archivo
    while True:                                             # bucle infinito hasta salir con 6
        print("\n=== AGENDA DE ESTUDIANTES ===")
        print("1. Mostrar estudiantes")
        print("2. Buscar estudiante")
        print("3. Agregar estudiante")
        print("4. Modificar estudiante")
        print("5. Eliminar estudiante")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")           # pedimos opción
        if opcion == "1":
            mostrar_estudiantes(estudiantes)
        elif opcion == "2":
            buscar_estudiante(estudiantes)
        elif opcion == "3":
            agregar_estudiante(estudiantes)
        elif opcion == "4":
            modificar_estudiante(estudiantes)
        elif opcion == "5":
            eliminar_estudiante(estudiantes)
        elif opcion == "6":
            print("👋 Saliendo de la agenda...")            # mensaje de salida
            break
        else:
            print("Opción inválida, intente de nuevo.")     # cuando haya error


# --- EJECUCIÓN ---
if __name__ == "__main__":                                  # para apenas se ejecute este archivo
    menu()                                                  # se llama al menu