# DB GAME CARDS - Versión 1.2

## Descripción
**Dragon Ball Game Cards** es un sistema interactivo basado en el concepto de tiradas de gacha, donde los usuarios pueden obtener cartas de distintas rarezas y construir su propia colección. Además, incluye un sistema de gestión de usuarios y progresos, con datos almacenados en archivos planos (`usuarios.txt`).

Este proyecto combina conceptos fundamentales de programación, como estructuras de datos, clases, funciones, manejo de archivos, ciclos y condicionales.

---

## Funcionalidades

### **1. Sistema de Tiradas (Gacha)**
- **Costo por tirada:** 100 Zennis.
- **Rarezas disponibles:**
  - **Común**: Mayor probabilidad (70%).
  - **Rara**: Probabilidad intermedia (25%).
  - **Legendaria**: Menor probabilidad (5%).
- **Duplicados:** Si se obtiene una carta repetida, el usuario recibe 50 Zennis como compensación.
- **Visualización de cartas:** Muestra una imagen asociada a la carta obtenida (requiere que las imágenes estén organizadas en carpetas específicas).

---

### **2. Gestión de Colección**
- **Mostrar colección:** Lista todas las cartas obtenidas por el usuario.
- **Ordenar colección:** Las cartas se ordenan alfabéticamente.
- **Buscar carta:** Permite buscar una carta específica en la colección ingresando el nombre completo.
- **Búsqueda dinámica:** Encuentra cartas basándose en un término parcial del nombre.

---

### **3. Estadísticas de Tiradas**
- Muestra un resumen de las cartas obtenidas por rareza:
  - Total de cartas comunes.
  - Total de cartas raras.
  - Total de cartas legendarias.

---

### **4. Gestión de Usuarios**
- **Crear usuario:** Crea un nuevo usuario con un nombre único.
- **Cargar usuario existente:** Recupera el progreso de un usuario previamente guardado.
- **Monedero virtual:** Muestra la cantidad de Zennis disponibles.
- **Guardar progreso:** Guarda el estado actual del usuario, incluyendo nombre, Zennis y colección, en un archivo plano (`usuarios.txt`).

---

### **5. Menú Principal**
El menú principal permite acceder a todas las funcionalidades del programa:

1. Realizar una tirada.
2. Mostrar la colección de cartas.
3. Consultar el monedero virtual.
4. Buscar una carta en la colección.
5. Ver estadísticas de tiradas.
6. Buscar cartas dinámicamente.
7. Salir (guarda automáticamente el progreso del usuario).

---

## Estructura del Archivo `usuarios.txt`
El archivo almacena los datos de cada usuario en el siguiente formato:

**Ejemplo:**

- `nombre_usuario`: Nombre del usuario.
- `zennis`: Monedas disponibles.
- `nombre_carta`: Nombre de la carta.
- `rareza`: Rareza de la carta.
- `id`: Identificador único de la carta.

---

## Requisitos
- **Python 3.x**
- **Librería Pillow** (para mostrar imágenes).
  ```bash
  pip install pillow
