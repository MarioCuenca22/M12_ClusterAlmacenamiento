# Configuración de la Página Web

**ESPETONETA** es un proyecto de Síntesis final diseñado para facilitar el acceso a todo el contenido de nuestro servidor a través de una página web. Este repositorio contiene los archivos principales del sitio web, incluyendo `index.html`, `main.js`, y `main.css`.

## Contenidos Principales
- [`index.html`](https://github.com/MarioCuenca22/M12_ClusterAlmacenamiento/blob/main/Cl%C3%BAster%20de%20Almacenamiento%20-%20Web/index.html)
- [`main.js`](https://github.com/MarioCuenca22/M12_ClusterAlmacenamiento/blob/main/Cl%C3%BAster%20de%20Almacenamiento%20-%20Web/assets/js/main.js)
- [`main.css`](https://github.com/MarioCuenca22/M12_ClusterAlmacenamiento/blob/main/Cl%C3%BAster%20de%20Almacenamiento%20-%20Web/assets/css/main.css)

## Estructura
```Documentos/
├── assets                      # Contiene todos los recursos estáticos del sitio web
│   ├── css                     # Archivos CSS para el estilo del sitio
│   │   ├── main.css            # Hoja de estilos principal
│   │   └── noscript.css        # Estilos para cuando JavaScript está deshabilitado
│   ├── js                      # Archivos JavaScript para la funcionalidad del sitio
│   │   ├── breakpoints.min.js  # Script para manejar puntos de quiebre en el diseño responsivo
│   │   ├── browser.min.js      # Detección de características del navegador
│   │   ├── jquery.min.js       # Biblioteca jQuery
│   │   ├── main.js             # Script principal del sitio
│   │   └── util.js             # Scripts utilitarios
│   ├── sass                    # Archivos SASS para generar los CSS
│   │   ├── base                # Estilos base para la página
│   │   ├── components          # Estilos para componentes individuales
│   │   ├── layout              # Estilos para el layout de la página
│   │   ├── libs                # Librerías y utilidades SASS
│   │   ├── main.scss           # Archivo principal SASS
│   └── webfonts                # Fuentes web utilizadas en el sitio
├── images                      # Imágenes utilizadas en el sitio
│   ├── apache                  # Imágenes relacionadas con Apache
│   ├── botpython               # Imágenes relacionadas con BotPython
│   ├── default                 # Imágenes por defecto
│   ├── gracias                 # Imágenes de agradecimientos
│   ├── grafana                 # Imágenes relacionadas con Grafana
│   ├── instalarch              # Imágenes relacionadas con la instalación de Arch Linux
│   ├── nosotros.jpg            # Imagen de la sección "Nosotros"
│   ├── nuestro servidor        # Imágenes del servidor
│   ├── overlay.png             # Imagen de superposición utilizada en el diseño
│   └── raspberry               # Imágenes relacionadas con Raspberry Pi
└── index.html                  # Página principal del sitio web

```

## HTML (index.html)
Este archivo HTML es la estructura principal de la página web **ESPETONETA**. A continuación, se describe su contenido y estructura principal:

#### Encabezado (`<head>`):
- **Título**: ESPETONETA
- **Meta etiquetas**: Define el juego de caracteres y la configuración de la vista para hacer la página responsive.
- **Favicon**: Icono de la página usando Font Awesome.
- **Hojas de estilo**: Se incluyen las hojas de estilo principales (`main.css` y `noscript.css`) y los íconos de Font Awesome.

#### Cuerpo (`<body>`):
- **Wrapper**: Un contenedor principal que envuelve todo el contenido.
- **Header**: Encabezado que contiene el logo, la descripción del proyecto, botones de navegación, y un menú de navegación con enlaces a diferentes secciones de la página.
- **Main**: Contiene diferentes artículos (`<article>`) que describen varias secciones del proyecto como Introducción, Contenido, y otros apartados específicos.
- **Footer**: Sección para el pie de página (aunque no detallada en los fragmentos proporcionados).

## CSS (main.css)
Este archivo CSS define el estilo visual de la página. A continuación, se describen algunas de las clases y estilos importantes:

#### Estilos Generales:
- Configuración básica para el cuerpo (`body`), fuentes, y colores de fondo.
- Clases para ajustar el comportamiento de elementos cuando JavaScript está deshabilitado (`noscript`).

#### Wrapper:
- Estilo para el contenedor principal que envuelve el contenido.

#### Header:
- Estilos para el encabezado, incluyendo la posición del logo y la alineación del texto y botones.

#### Main:
- Estilos para la sección principal que contiene los artículos. Incluye configuraciones para imágenes, texto y elementos interactivos.

#### Responsiveness:
- Media queries para ajustar el diseño en diferentes tamaños de pantalla, asegurando que la página se vea bien en dispositivos móviles y de escritorio.

## JavaScript (main.js)
Este archivo JavaScript gestiona la interactividad y las animaciones de la página. Algunos puntos clave incluyen:

#### Inicialización y Configuración:
- Define variables para manejar elementos del DOM como el `window`, `body`, `wrapper`, `header`, `footer`, y `main`.
- Configura puntos de interrupción (breakpoints) para hacer la página responsive.

#### Animaciones Iniciales:
- Al cargar la página, se quita la clase `is-preload` después de 100ms para iniciar animaciones.

#### Corrección de Bugs:
- Soluciona un bug específico de Flexbox en Internet Explorer ajustando la altura del `wrapper`.

#### Navegación:
- Gestiona la navegación entre diferentes artículos. Muestra y oculta artículos según la navegación del usuario, manejando el bloqueo de animaciones para evitar conflictos.
- Implementa un sistema de historial para manejar el retroceso y avance en la navegación usando hashes.

#### Eventos:
- Controla eventos de clic y teclas (como Escape) para mostrar u ocultar artículos.
- Maneja el cambio de hash en la URL para mostrar el artículo correspondiente.

## Instalación y Uso
Para usar esta página web, simplemente clona el repositorio y abre `index.html` en tu navegador preferido.

```bash
git clone https://github.com/tu_usuario/ESPETONETA.git
cd ESPETONETA
```
