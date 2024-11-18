import os
from PIL import Image
import random

# Ruta base relativa al script actual
CARPETA_BASE = os.path.dirname(os.path.abspath(__file__))
CARPETA_IMAGENES = CARPETA_BASE
ARCHIVO_USUARIOS = os.path.join(CARPETA_BASE, "usuarios.txt")

# Crear el directorio si no existe
if not os.path.exists(CARPETA_IMAGENES):
    os.makedirs(CARPETA_IMAGENES)
    print(f"Carpeta de imágenes creada en: {CARPETA_IMAGENES}")

# Colores
def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def verificar_directorio():
    if not os.path.exists(CARPETA_IMAGENES):
        os.makedirs(CARPETA_IMAGENES)
        print_colored(f"Directorio '{CARPETA_IMAGENES}' creado.", "33")  # Amarillo

    # Crear subcarpetas para las imágenes si no existen
    for subcarpeta in ["comun", "rara", "legendaria"]:
        ruta_subcarpeta = os.path.join(CARPETA_IMAGENES, subcarpeta)
        if not os.path.exists(ruta_subcarpeta):
            os.makedirs(ruta_subcarpeta)
            print_colored(f"Subcarpeta '{subcarpeta}' creada en: {ruta_subcarpeta}", "33")

# Verificación y creación del bloc de notas
def verificar_o_crear_archivo():
    if not os.path.exists(ARCHIVO_USUARIOS):
        with open(ARCHIVO_USUARIOS, "w") as archivo:
            archivo.write("")  # Crear el archivo vacío si no existe
        print_colored("Archivo usuarios.txt creado automáticamente.", "33")  # Amarillo

# Cargar Usuarios
def cargar_usuarios():
    usuarios_existentes = {}
    if os.path.exists(ARCHIVO_USUARIOS):
        with open(ARCHIVO_USUARIOS, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) >= 2:
                    usuario = datos[0]
                    zennis_usuario = int(datos[1])
                    cartas_usuario = datos[2:]
                    usuarios_existentes[usuario] = (zennis_usuario, cartas_usuario)
    return usuarios_existentes

# Usuarios Registrados
def mostrar_usuarios_existentes(usuarios_existentes):
    if usuarios_existentes:
        print_colored("Usuarios existentes:", "36")  # Azul claro
        for idx, usuario in enumerate(usuarios_existentes.keys(), start=1):
            print_colored(f"{idx}. {usuario}", "33")  # Amarillo
    else:
        print_colored("No hay usuarios existentes. Debes crear uno nuevo.", "31")  # Rojo

# Cargar Usuarios
def cargar_o_crear_usuario():
    global nombre_usuario, zennis, coleccion
    usuarios_existentes = cargar_usuarios()  # Cargar los usuarios
    mostrar_usuarios_existentes(usuarios_existentes)  # Mostrar los usuarios

    while True:
        print_colored("¿Deseas entrar con un usuario existente o crear uno nuevo?", "33")
        print("1. Entrar con usuario existente")
        print("2. Crear un nuevo usuario")
        opcion = input("Elige una opción (1 o 2): ").strip()

        if opcion == '1':
            nombre_usuario = input("Ingresa el nombre de usuario: ").strip()
            if nombre_usuario in usuarios_existentes:
                zennis, coleccion = usuarios_existentes[nombre_usuario]
                print_colored(f"Bienvenido de nuevo, {nombre_usuario}. Tu progreso ha sido cargado.", "32")
                return
            else:
                print_colored("El usuario no existe. Por favor, intenta de nuevo.", "31")
        elif opcion == '2':
            nombre_usuario = input("Ingresa tu nombre de usuario: ").strip()
            zennis = 500
            coleccion = []
            print_colored(f"Bienvenido, {nombre_usuario}. ¡Tu aventura comienza ahora!", "32")
            return
        else:
            print_colored("Opción no válida. Por favor, elige 1 o 2.", "31")

# Colección de cartas
def mostrar_coleccion():
    if len(coleccion) == 0:
        print_colored("Aún no tienes cartas en tu colección.", "33")
    else:
        for carta in coleccion:
            print(f"- {carta}")

# Implementación del algoritmo MergeSort para ordenar la colección con comentarios
def merge_sort(lista):
    if len(lista) > 1:
        # Paso 1: Dividir la lista en dos mitades
        mitad = len(lista) // 2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]
        
        # Mostrar la división
        #print(f"Dividiendo: {lista} en {izquierda} y {derecha}")

        # Llamada recursiva para dividir cada mitad hasta que tengan un solo elemento
        merge_sort(izquierda)
        merge_sort(derecha)

        # Inicialización de índices
        i = j = k = 0

        # Paso 2: Comparar los elementos de las sublistas y mezclarlos en orden
        while i < len(izquierda) and j < len(derecha):
            # Mostrar la comparación de elementos
            #print(f"Comparando: {izquierda[i]} y {derecha[j]}")
            
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        # Paso 3: Agregar los elementos restantes de la sublista izquierda si los hay
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        # Paso 4: Agregar los elementos restantes de la sublista derecha si los hay
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
        # Mostrar cómo se está combinando de nuevo
        #print(f"Combinando: {izquierda} y {derecha} en {lista}")

# Función para ordenar la colección de cartas usando MergeSort
def ordenar_coleccion():
    # Aplicar MergeSort a la colección
    merge_sort(coleccion)
    print_colored("Colección ordenada alfabéticamente:", "34")
    mostrar_coleccion()

# Monedas
def mostrar_monedero():
    print_colored(f"Tienes {zennis} Zennis.", "34")

# Búsqueda de cartas
def buscar_carta():
    carta_a_buscar = input("Ingresa el nombre de la carta que deseas buscar: ").strip()
    if carta_a_buscar in coleccion:
        print_colored(f"Tienes la carta {carta_a_buscar} en tu colección.", "32")
    else:
        print_colored(f"No tienes la carta {carta_a_buscar} en tu colección.", "31")

# Historial de tiradas, aquí se aplica las matrices
def mostrar_estadisticas():
    print_colored("Estadísticas de cartas obtenidas:", "34")
    print(f"Común: {historial_tiradas[0][0]}")
    print(f"Rara: {historial_tiradas[0][1]}")
    print(f"Legendaria: {historial_tiradas[0][2]}")

# Guardar datos 
def guardar_progreso():
    with open(ARCHIVO_USUARIOS, "a") as archivo:
        archivo.write(f"{nombre_usuario},{zennis},{','.join(coleccion)}\n")
    print_colored("Progreso guardado correctamente.", "32")

# Variables
zennis = 0
coleccion = []
nombre_usuario = ""
historial_tiradas = [[0, 0, 0]]  # Matriz para registrar las tiradas (comun, rara, legendaria)

cartas = {
    "comun": ["Arale", "Launch Base", "Launch Transformada"],
    "rara": ["Kid Buu", "Goku Ssj", "Trunks"],
    "legendaria": ["Gohan Definitivo", "Goku Super Saiyan 3", "Goku Ultra Instinto"]
}
probabilidades = {
    "comun": 0.7,
    "rara": 0.25,
    "legendaria": 0.05
}

def mostrar_imagen(rareza, carta_numero):
    # Combina correctamente la ruta base con las subcarpetas
    ruta_imagen = os.path.join(CARPETA_IMAGENES, rareza, f"{carta_numero}.jpg")
    
    if os.path.exists(ruta_imagen):
        img = Image.open(ruta_imagen)
        img.show()
    else:
        print_colored(f"No se pudo cargar la imagen de la carta. Ruta: {ruta_imagen}", "31")  # Mensaje en rojo


# Tirar al gacha
def realizar_tirada():
    global zennis, coleccion, historial_tiradas
    if zennis < 100:
        print_colored("¡No tienes suficientes Zennis para hacer una tirada!", "31")  # Rojo
        return
    
    zennis -= 100
    rareza = random.choices(
        ["comun", "rara", "legendaria"],
        [probabilidades["comun"], probabilidades["rara"], probabilidades["legendaria"]]
    )[0]
    carta_numero = random.randint(1, 3)  # Hay 3 cartas por rareza
    carta_sacada = cartas[rareza][carta_numero - 1]

    if carta_sacada in coleccion:
        print_colored(f"Ya tienes la carta {carta_sacada}, se convierte en 50 Zennis.", "31")  # Rojo
        zennis += 50
    else:
        coleccion.append(carta_sacada)
        print_colored(f"¡Felicidades! Has obtenido la carta {carta_sacada} de rareza {rareza}.", "32")  # Verde
        mostrar_imagen(rareza, carta_numero)

        # Registrar en la matriz
        if rareza == "comun":
            historial_tiradas[0][0] += 1
        elif rareza == "rara":
            historial_tiradas[0][1] += 1
        elif rareza == "legendaria":
            historial_tiradas[0][2] += 1

def mostrar_cartas_por_rareza(rareza):
    cartas_filtradas = [carta for carta in coleccion if carta in cartas[rareza]]
    if cartas_filtradas:
        print_colored(f"Cartas de rareza {rareza}:", "36")
        for carta in cartas_filtradas:
            print(f"- {carta}")
    else:
        print_colored(f"No tienes cartas de rareza {rareza}.", "31")

def eliminar_carta():
    carta_a_eliminar = input("Ingresa el nombre de la carta que deseas eliminar: ").strip()
    if carta_a_eliminar in coleccion:
        coleccion.remove(carta_a_eliminar)
        print_colored(f"La carta {carta_a_eliminar} ha sido eliminada de tu colección.", "32")
    else:
        print_colored(f"No tienes la carta {carta_a_eliminar} en tu colección.", "31")

def agregar_carta_personalizada():
    nueva_carta = input("Ingresa el nombre de la nueva carta: ").strip()
    rareza = input ("Ingresa la rareza de la carta (comun, rara, legendaria): ").strip().lower()

    if rareza in cartas:
        coleccion.append(nueva_carta)
        cartas[rareza].append(nueva_carta)
        print_colored(f"La carta {nueva_carta} ha sido agregada a tu colección y a la lista de cartas.", "32")
    else:
        print_colored("La rareza ingresada no es válida. La carta no ha sido agregada.", "31")

# Función principal del juego
def juego():
    verificar_directorio()
    verificar_o_crear_archivo()
    cargar_o_crear_usuario()
    while True:
        print_colored("\nMenú principal:", "36")
        print("1. Realizar una tirada")
        print("2. Mostrar colección")
        print("3. Mostrar monedero")
        print("4. Buscar carta en la colección")
        print("5. Mostrar estadísticas")
        print("6. Mostrar cartas por rareza")
        print("7. Eliminar carta de la colección")
        print("8. Agregar carta personalizada")
        print("9. Salir")
        
        comando = input("Ingresa un comando: ").strip().lower()
        if comando == "1":
            realizar_tirada()
        elif comando == "2":
            ordenar_coleccion()
        elif comando == "3":
            mostrar_monedero()
        elif comando == "4":
            buscar_carta()
        elif comando == "5":
            mostrar_estadisticas()
        elif comando == "6":
            rareza = input("¿Qué rareza quieres ver? (comun, rara, legendaria): ").strip().lower()
            mostrar_cartas_por_rareza(rareza)
        elif comando == "7":
            eliminar_carta()
        elif comando == "8":
            agregar_carta_personalizada()
        elif comando == "9":
            guardar_progreso()
            print_colored("Guardando el juego... ¡Hasta la próxima!", "34")
            break
        else:
            print_colored("Comando no reconocido. Por favor, intenta nuevamente.", "31")

# Iniciar el juego
juego()
