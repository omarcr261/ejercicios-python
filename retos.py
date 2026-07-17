# 01. Inicio en Python.

'''nombre = input("¿Cómo te llamas? ")
print ( f'¡Hola {nombre}! Python 3.14.3 esta funcionando en tu Mac.')'''

# 02 Calculadora edad actual.

'''nacimiento =input ( '¿En qué año naciste? ')
edad = 2026 - int(nacimiento)
print ( f"Omar, en este año 2026 tienes (o vas a cumplir) {edad} años.")'''

# 03. Saludo.

'''nombre = input("¿Cuál es tu nombre? ")
meta = input("¿Cuál es tu meta? ")

print(f"Hola mi nombre es {nombre} y mi meta es ser {meta}.")'''

# 04. Calculadora de años 2030.

'''edad = int(input("¿Cuál es tu edad "))
año_actual = 2026
año_futuro = 2030
edad_2030 = (edad + (2030 - 2026))

print(f"Tu edad en el 2030 va a ser de {edad_2030} años.")'''

# 05. Multiplicaciones.

'''tabla_a_desarrollar = int(input("¿Qué tabla deseas desarrollar? "))
for desarrollo in range(1,11):
    resultado = tabla_a_desarrollar * desarrollo
    print(f"{tabla_a_desarrollar} * {desarrollo} = {resultado}")'''

# 06. Cadenero de fiesta.

'''edad = int(input("Ingresa tu edad: "))
usuario = input("Ingresa tu nombre: ")

if edad <18:
    print("Lo siento no tienes edad suficiente.")
elif usuario == "Brais":
    print("Bienvenido Brais, entra por la puerta trasera.")
else:
    print("Bienvenido, disfruta la fiesta.")'''

# 07. Lista de compras.

'''shopping_list = ["Leche", "Pan", "Café"]
articulo_extra = input("¿Qué articulo deseas agregar? ")

shopping_list.append(articulo_extra)

for articulos in shopping_list:
    print(f"🔳 {articulos}")'''

# 08. Bucle de repetición.
'''frase = "Voy a ser ingeniero de datos"

for numero in range(10):
    print(f"{(numero + 1)}. {frase}")'''

# 09. Registro de proyectos.

'''database = []
project_name = input("Project name: ")
project_lenguage = input("Project lenguage: ")
data_dictionary = {"Name":(project_name), "Lenguage":(project_lenguage)}

database.append(data_dictionary)

print(database)
print("Project succesfully registered in data base")'''

# 10. Calificador de exámenes.

'''calificacion = int(input("¿Cuál es tu calificación? "))

if calificacion < 0 or calificacion > 100:
     print("Error:Calificacion no valida.")
elif calificacion >= 90:
     print("Excelente, estas en el cuadro de honor.")
elif calificacion >= 70:
     print("Aprobado, buen esfuerzo.")
else:
     print("Reprobado, necesitas presentar recuperación")'''


# 11. Promedio de calificaciones.

'''mis_calificaciones = []

for univ in range(3):
    nota = int(input(f"Ingresa la calificación {univ + 1}: "))
    mis_calificaciones.append(nota)

promedio = sum(mis_calificaciones) / len(mis_calificaciones)

print(f"\nTus calificaciones son: {mis_calificaciones}")
print(f"Tu promedio final es: {promedio:.2f}")'''

# 12. Promedio calificaciones 2.

'''mis_notas = []

for i in range(3):
    nota = int(input(f"Ingresa la calificación {i + 1}: "))
    
    if nota >= 0 and nota <= 100:
        print("Calificación válida, guardando...")
        mis_notas.append(nota)
    else:
        print("Error: Esa nota no existe. No se guardará.")

if len(mis_notas) > 0:
    promedio = sum(mis_notas) / len(mis_notas)
    print(f"\nNotas finales: {mis_notas}")
    print(f"Tu promedio es: {promedio:.2f}")
else:
    print("\nNo se ingresó ninguna nota válida para promediar.")'''

# 13. Calificaciones 2.

'''calificacion = int(input("¿Cual es tu calificacion? "))

if calificacion >= 0 and calificacion <= 100:
    if calificacion >= 90:
        print("Cuadro de honor")
    elif calificacion >= 70:
        print("Aprobado")
    else: 
        print("Reprobado")
else:
    print("Error")'''

# 14. Promedio calificaciones.

'''lista_calificaciones = []

for pregunta in range(3):
    calificaciones = int(input(f"Cual es tu calificaion? {pregunta + 1} "))

    lista_calificaciones.append(calificaciones)

print(f"Estas son tus calificaciones registradas:{lista_calificaciones}")

promedio = sum(lista_calificaciones) / len(lista_calificaciones)
print(f"Tu promedio es: {promedio:.2f}")'''

# 15. Ventas importantes.

'''ventas_importantes = []

for pregunta in range(5):
    ventas_trabajador = int(input(f"¿Cual es tu venta? {pregunta + 1} "))
    if ventas_trabajador >0:
     print("Guardando su respuesta")
     if ventas_trabajador >= 100:
        ventas_importantes.append(ventas_trabajador)
    else:
        print("Error")

print(f"Sus ventas guardadas son: {ventas_importantes}")
ventas_registradas = len(ventas_importantes)

print(f"El numero de ventas registradas es de; {ventas_registradas}")
total_ventas = sum(ventas_importantes)

print(f"El total de sus ventas es de: ${total_ventas}")'''


# 16. Diccionario .get.

'''peril_pro = {"Nombre":"Omar", "Edad":24, "Objetivo":"Ingeniero de datos"}

my_name = peril_pro["Nombre"]
my_age = peril_pro.get("Edad")
my_limit = peril_pro.get("Objetivo")

print(f"Mi nombre es {my_name}, tengo {my_age} años y quiero ser {my_limit}.")'''

# 17. Datos que recibes (el sensor_2 no tiene 'temperatura').

'''lecturas = [{"id": "sensor_1", "temperatura": 25},{"id": "sensor_2"}, {"id": "sensor_3", "temperatura": 22}]

print("--- Procesando lecturas de hoy ---")

for lectura in lecturas:
    temp = lectura.get("temperatura", "ERROR: Sensor sin lectura")
    
    print(f"ID: {lectura['id']} | Estado: {temp}")'''

# 18. Tu base de datos (Diccionario) .get.
'''perfil_pro = {"Nombre": "Tu Nombre","Objetivo": "Data Engineer"}
nombre = perfil_pro["Nombre"]
edad = perfil_pro.get("Edad", "Secreta")
pais = perfil_pro.get("Pais", "Global")

print(f"--- REPORTE DE USUARIO ---")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Ubicación: {pais}")
print(f"Meta: {perfil_pro.get('Objetivo')}")'''

# 19. Diccionario proyecto.

'''proyecto = {"Nombre":"Analizador de datos", "Lenguaje":"Python"}

nombre_proy = proyecto["Nombre"]
lenguaje_proy = proyecto.get("Lenguaje", "No especificado")
fecha_proy = proyecto.get("Fecha", "Pendiente")
estatus_proy = proyecto.get("Estatus", "En espera")

print(f" Nombre del proyecto: {nombre_proy}.\n Lenguaje: {lenguaje_proy}.\n Fue entregado en la fecha: {fecha_proy}.\n Estatus: {estatus_proy}.")'''

# 20. Lista de diccionarios.

'''portafolio = [{"Nombre":"Proyecto 1", "Lenguaje":"Python", "Estatus":"Entregado"},{"Nombre":"Proyecto 2", "Lenguaje":"Python"}, {"Nombre":"Proyecto 3"}]

for datos in portafolio:
     nombre_v = datos["Nombre"]
     lenguaje_v = datos.get("Lenguaje", "Por definir")
     estatus_v = datos.get("Estatus", "En espera")
     print(f"Nombre: {nombre_v} | Lenguaje: {lenguaje_v} | Estatus: {estatus_v}")'''

# 21. Agregar datos a lista de diccionarios.

'''portafolio = [{"Nombre":"Proyecto 1", "Lenguaje":"Python", "Estatus":"Entregado"},{"Nombre":"Proyecto 2", "Lenguaje":"Python"}, {"Nombre":"Proyecto 3"}]

nuevo_nombre = input("Nombre del proyecto: ")
nuevo_lenguaje = input("Lenguaje: ")
nuevo_estatus = input("Estatus: ")

proyecto_nuevo = {"Nombre":nuevo_nombre, "Lenguaje":nuevo_lenguaje, "Estatus":nuevo_estatus}

portafolio.append(proyecto_nuevo)

for datos in portafolio:
     nombre_v = datos["Nombre"]
     lenguaje_v = datos.get("Lenguaje", "Por definir")
     estatus_v = datos.get("Estatus", "En espera")
     print(f"Nombre: {nombre_v} | Lenguaje: {lenguaje_v} | Estatus: {estatus_v}")'''

# 22. Portafolio filtrar datos con una busqueda.

'''portafolio = [{"Nombre":"Proyecto 1", "Lenguaje":"Python", "Estatus":"Entregado"},{"Nombre":"Proyecto 2", "Lenguaje":"Python"}, {"Nombre":"Proyecto 3"}]

nuevo_nombre = input("Nombre del proyecto: ")
nuevo_lenguaje = input("Lenguaje: ")
nuevo_estatus = input("Estatus: ")

proyecto_nuevo = {"Nombre":nuevo_nombre, "Lenguaje":nuevo_lenguaje, "Estatus":nuevo_estatus}

portafolio.append(proyecto_nuevo)

busqueda = input("¿Qué lenguaje quieres filtrar? ")

for datos in portafolio:
     lenguaje_v = datos.get("Lenguaje", "Por definir")

     if busqueda == lenguaje_v:
          nombre_v = datos["Nombre"]
          estatus_v = datos.get("Estatus", "En espera")
          print(f"Nombre: {nombre_v} | Lenguaje: {lenguaje_v} | Estatus: {estatus_v}")'''

# 23. Filtrar datos de listas.

'''lista_numeros = [10, 55, 42, 78, 32, 90, 11]
nueva_lista = []

for datos in lista_numeros:
    if datos > 50:
        nueva_lista.append(datos)
print(nueva_lista)'''

# 24. Portafolio filtrar datos 2.0.

'''proyectos = [{"Nombre":"Proyecto 1", "Lenguaje":"Python", "Estatus":"Entregado"}, {"Nombre":"Proyecto 2", "Lenguaje":"Python"}, {"Nombre":"Proyecto 3"}]

nombre_nuevo = input("Nombre del proyecto: ")
lenguaje_nuevo = input("Lenguaje: ")
estatus_nuevo = input("Estatus: ")

proyecto_nuevo = {"Nombre":nombre_nuevo, "Lenguaje":lenguaje_nuevo, "Estatus":estatus_nuevo}

proyectos.append(proyecto_nuevo)

filtro = input("¿Qué lenguaje quieres filtrar?")

for datos in proyectos:
    lenguaje = datos.get("Lenguaje", "Otro")
    if lenguaje == filtro:
        nombre = datos["Nombre"]
        estatus = datos.get("Estatus", "Sin estatus")
        print(f"Nombre: {nombre} Estatus: {estatus} Lenguaje: {lenguaje}")'''

# 25. Analizador de gastos automatico.

'''transactions = [ {"item": "Laptop", "price": 1200, "category": "Tech"}, {"item": "Coffee", "price": 5, "category": "Food"}, {"item": "Monitor", "price": 300, "category": "Tech"},{"item": "Pizza", "price": 20, "category": "Food"},
                {"item": "Keyboard", "price": 50, "category": "Tech"}]

categoria_usuario = input("Categoria: ")
total_spent = 0 

for datos in transactions:
    categoria_lista = datos.get("category")

    if categoria_lista == categoria_usuario:
        total_spent += datos.get("price", 0)

print(f"El total de sus compras en la categoria {categoria_lista} es de ${total_spent}.")'''

# 26. Filtro inventario seguro.

'''bodega = [
    {"prod": "Martillo", "precio": 20, "disponible": True},
    {"prod": "Clavos", "precio": "5", "disponible": True}, # <--- Texto!
    {"prod": "Taladro", "precio": 150, "disponible": False},
    {"prod": "Sierra", "precio": None, "disponible": True}, # <--- Sin precio!
    {"prod": "Lija", "precio": 2, "disponible": True}
]

valor_total = 0

for producto in bodega:
    try:
        if producto.get("disponible") == True:

            precio_limpio = int(producto.get("precio"))
            
            valor_total += precio_limpio
            
    except:
        print(f"Saltando producto: {producto.get('prod')} por dato inválido.")

print(f"El valor total es: {valor_total}")'''

# 27. Contador de categorias 

'''# 1. Los Datos
ventas = [
    {"item": "Teclado", "monto": 50, "cat": "Tech"},
    {"item": "Silla", "monto": 150, "cat": "Oficina"},
    {"item": "Monitor", "monto": 300, "cat": "Tech"},
    {"item": "Café", "monto": "5", "cat": "Comida"},
    {"item": "Escritorio", "monto": 200, "cat": "Oficina"},
    {"item": "Pan", "monto": None, "cat": "Comida"}
]

# 2. El contenedor vacío
totales = {}

# 3. El proceso
for datos in ventas:
    try:
        categoria = datos.get("cat")
        monto = int(datos.get("monto"))
        
        # LA LÓGICA DEL DICCIONARIO:
        if categoria in totales:
            # Si "Tech" ya existe en totales, le sumamos el nuevo monto
            totales[categoria] += monto
        else:
            # Si "Tech" no existe, lo creamos con el monto que lleva
            totales[categoria] = monto
            
    except:
        # Aquí caen el "Pan" (None) y cualquier otro error
        continue

# 4. Resultado final
print(totales)'''

# 28. Filtro de datos por ciudad 

'''personas = [
    {"nombre": "Ana", "edad": "25", "ciudad": "CDMX"},
    {"nombre": "Luis", "edad": "17", "ciudad": "Guadalajara"},
    {"nombre": "Carlos", "edad": "no disponible", "ciudad": "CDMX"},
    {"nombre": "Marta", "edad": "30", "ciudad": "Monterrey"},
    {"nombre": "Sofia", "edad": "22", "ciudad": "CDMX"}
]

persona_mayor = []

ciudad_usuario = input("Elige una ciudad: ")

print(f"Estos son los datos encontrados.")

ciudad_filtrada = []

for datos in personas:
    try:
        nombre = datos["nombre"]
        ciudad = datos["ciudad"]
        edad = int(datos.get("edad"))
        if ciudad_usuario == ciudad:
            print(f"Nombre: {nombre} | Edad: {edad} | Ciudad: {ciudad}")
            datos_filtrados = {"Nombre":nombre, "Edad": edad, "Ciudad": ciudad}
            ciudad_filtrada.append(datos_filtrados)

    except:
        continue

lista_edad = []

for contenido in ciudad_filtrada:
    
    
    edad_final = contenido["Edad"]
    lista_edad.append(edad_final)

numero_usuarios = len(lista_edad)
suma_edades = sum(lista_edad)
promedio = (suma_edades / numero_usuarios)
print(F"{ciudad_usuario} cuenta con {numero_usuarios} habitantes con una edad promedio de {promedio} años.")'''

# 29. Filtro por ciudad (chat gpt)

'''personas = [
    {"nombre": "Ana", "edad": "25", "ciudad": "CDMX"},
    {"nombre": "Luis", "edad": "17", "ciudad": "Guadalajara"},
    {"nombre": "Carlos", "edad": "no disponible", "ciudad": "CDMX"},
    {"nombre": "Marta", "edad": "30", "ciudad": "Monterrey"},
    {"nombre": "Sofia", "edad": "22", "ciudad": "CDMX"}
]

# Input del usuario
ciudad_usuario = input("Ingresa una ciudad: ").strip().upper()

# Filtrar y limpiar datos
ciudad_filtrada = []

for persona in personas:
    try:
        edad = int(persona["edad"])
        if persona["ciudad"].upper() == ciudad_usuario:
            ciudad_filtrada.append({"nombre": persona["nombre"], "edad": edad})
    except:
        continue

# Validar si hay datos
if not ciudad_filtrada:
    print("No hay datos para esa ciudad")
else:
    # Calcular promedio
    suma = 0
    for persona in ciudad_filtrada:
        suma += persona["edad"]

    promedio = suma / len(ciudad_filtrada)

    # Encontrar persona mayor
    persona_mayor = None
    for persona in ciudad_filtrada:
        if persona_mayor is None or persona["edad"] > persona_mayor["edad"]:
            persona_mayor = persona

    # Resultados
    print(f"\nPersonas en {ciudad_usuario}: {len(ciudad_filtrada)}")
    print(f"Edad promedio: {promedio:.2f}")
    print(f"Persona mayor: {persona_mayor['nombre']} ({persona_mayor['edad']} años)")'''

   
'''hola = [{"nombre":"omar", "edad":24}, {"nombre":"jose", "edad":30}]

mayor = max(hola, key=lambda x: x["edad"])

# Aquí usamos 'mayor' porque es el diccionario individual
print(f"El mayor es {mayor['nombre']} con {mayor['edad']} años.")'''