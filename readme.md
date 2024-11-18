# DB GAME CARDS - Versión 1.1

Este proyecto en Python implementa un sistema de gacha donde los jugadores pueden realizar tiradas, coleccionar cartas y gestionar sus recursos de forma interactiva. 

En esta versión 1.1 se integró la funcionalidad de **listas**, lo que permite una gestión avanzada de las cartas del jugador.

---

## **Novedades en la Versión 1.1**
### **1. Filtrar cartas por rareza**
- Ahora los jugadores pueden filtrar su colección para ver solo cartas de una rareza específica (común, rara o legendaria).
- **Comando**: Opción 6 en el menú principal.
- **Ejemplo de uso**:
  - Si seleccionas "común", verás todas las cartas comunes que tienes en tu colección.

### **2. Eliminar cartas**
- Los jugadores pueden eliminar cartas específicas de su colección.
- **Comando**: Opción 7 en el menú principal.
- **Ejemplo de uso**:
  - Ingresa el nombre de la carta que deseas eliminar y será removida de la colección.

### **3. Agregar cartas personalizadas**
- Ahora es posible agregar nuevas cartas manualmente, asignándoles un nombre y una rareza.
- **Comando**: Opción 8 en el menú principal.
- **Ejemplo de uso**:
  - Ingresa el nombre "Vegeta SSJ" y la rareza "rara", y esta carta será añadida a tu colección.

---

## **Cómo usar el proyecto**
1. Ejecuta el programa `Gacha.py` desde tu terminal o entorno de desarrollo.
2. En el menú principal, selecciona las opciones para interactuar:
   - Realizar tiradas.
   - Ver tu colección.
   - Filtrar cartas por rareza.
   - Eliminar o agregar cartas personalizadas.
3. Sigue las instrucciones del programa para cada opción.

---

## **Estructura del proyecto**
- **`Gacha.py`**: Archivo principal que contiene el código del sistema.
- **Carpetas de imágenes**:
  - `comun/`: Cartas comunes.
  - `rara/`: Cartas raras.
  - `legendaria/`: Cartas legendarias.
- **`usuarios.txt`**: Archivo que almacena los datos de los jugadores.

---

## **Funcionalidades completas**
### **Gestión de usuarios**
- Crear o cargar usuarios.
- Guardar progreso automáticamente.

### **Sistema de cartas**
- Tiradas con rarezas específicas:
  - 70% común.
  - 25% rara.
  - 5% legendaria.
- Mostrar colección ordenada alfabéticamente.
- Buscar cartas en la colección.

### **Monedas**
- Gestión de Zennis para realizar tiradas.

### **Listas (versión 1.1)**
- Filtrar cartas por rareza.
- Eliminar cartas de la colección.
- Agregar cartas personalizadas.

---

## **Próximas mejoras**
- Implementación de cadenas dinámicas para búsquedas avanzadas.
- Reestructuración de datos usando registros (diccionarios o clases).
