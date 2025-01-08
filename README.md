# M6S6_TemplateBootstrap2
M6S6 - TEMPLATES EN DJANGO DRILLING: AGREGANDO NAVBAR CON BOOTSTRAP
# Proyecto Django: Implementación de Layout Reutilizable con Bootstrap

Este proyecto es un ejemplo práctico de cómo implementar un **layout reutilizable** en un proyecto Django utilizando la herencia de plantillas y Bootstrap para un diseño responsivo y moderno.

## Descripción

El objetivo del proyecto es crear una estructura básica en Django que permita reutilizar un diseño principal (layout) en múltiples páginas de una aplicación web. Para lograr esto, se utiliza un archivo `layout.html` como plantilla principal, que contiene elementos comunes como la barra de navegación y los estilos de Bootstrap. Las plantillas secundarias extienden esta plantilla base, sobrescribiendo solo las secciones necesarias.

## Funcionalidades

1. **Layout Reutilizable:**
   - Un diseño principal con una barra de navegación que puede ser utilizado en todas las páginas.
   - Uso de bloques `{% block %}` en Django para personalizar contenido en plantillas secundarias.

2. **Integración de Bootstrap:**
   - Uso de la librería Bootstrap 5 para un diseño moderno y responsivo.
   - Componentes de Bootstrap, como la barra de navegación y listas estilizadas.

3. **Vistas Dinámicas:**
   - Páginas dinámicas que muestran datos simulados de libros.
   - Filtrado de libros según criterios, como valoración alta.

## Estructura de Archivos

```plaintext
Proyecto
├── templates
│   ├── layout.html          # Layout principal
│   ├── index.html         # Página de inicio
│   └── list_books.html    # Página que muestra la lista de libros
├── views.py               # Vistas de Django
├── urls.py                # Configuración de URLs
└── README.md              # Documentación del proyecto
```

## Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

1. Clona este repositorio:
   ```bash
   git clone <URL-del-repositorio>
   cd <directorio-del-repositorio>
   ```

2. Crea un entorno virtual y actívalo:
   ```bash
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   ```

3. Instala Django:
   ```bash
   pip install django
   ```

4. Ejecuta el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

5. Abre el navegador y visita:
   - **Inicio:** [http://localhost:8000/](http://localhost:8000/)
   - **Libros:** [http://localhost:8000/list_book/](http://localhost:8000/list_book/)

## Explicación Técnica

### 1. `layout.html`
Esta plantilla principal define la estructura básica del sitio:
- Incluye Bootstrap desde una CDN.
- Contiene la barra de navegación con enlaces a las diferentes páginas.
- Define los bloques `{% block title %}` y `{% block content %}` para personalizar el título y contenido en las plantillas secundarias.

### 2. Herencia de Plantillas
Las plantillas como `index.html` y `list_books.html` extienden `layout.html` usando la directiva `{% extends 'layout.html' %}`. Esto permite sobrescribir solo los bloques necesarios sin duplicar código.

### 3. Datos Simulados
En `views.py`, se crean listas de diccionarios que representan libros con atributos como título, autor y valoración. Estos datos se pasan a las plantillas mediante el contexto.

### 4. Rutas
En `urls.py`, se configuran las rutas para las páginas de inicio y de libros, vinculando las URLs a las vistas correspondientes.

## Tecnologías Utilizadas

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap 5
- **Servidor Local:** Django Development Server

## Próximos Pasos

- Integrar una base de datos para gestionar los libros dinámicamente.
- Agregar más estilos y personalización en las páginas.
- Implementar formularios para interactuar con los datos.

## Créditos

Este proyecto fue desarrollado como parte de un ejercicio práctico para aprender la implementación de layouts reutilizables en Django.

---
¡Gracias por revisar este proyecto! Si tienes alguna duda o sugerencia, no dudes en abrir un issue o contactarme.
