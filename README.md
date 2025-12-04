# Organizador de Archivos (Python)

Script en Python que monitoriza una carpeta específica (por defecto Descargas) y mueve automáticamente los archivos entrantes a subcarpetas basándose en su extensión.

El script está diseñado con extensión `.pyw` para ejecutarse en segundo plano sin mostrar una ventana de consola.

## Instalación y Auto-arranque

Para que el script funcione de forma autónoma al iniciar Windows:

1. Descarga el archivo `main.pyw` en una ubicación permanente.
2. Crea un acceso directo del archivo.
3. Presiona `Win + R`, escribe `shell:startup` y pulsa Enter.
4. Mueve el acceso directo creado a esa carpeta.

## Configuración

Antes de ejecutarlo, es necesario definir la ruta a monitorizar:

1. Abre `main.pyw` con un editor de texto.
2. Localiza la variable `folder_path` al inicio del archivo.
3. Modifica la ruta por la carpeta deseada. Ejemplo:
   `folder_path = r"C:\Users\TuUsuario\Downloads"`

## Clasificación

El script organiza los archivos en las siguientes categorías:

* **Imagenes:** jpg, jpeg, png, gif, bmp, svg, webp
* **Documentos:** pdf, docx, txt, xlsx, pptx, csv, doc
* **Ejecutables:** exe, msi, zip, rar, 7z
* **Audio_Video:** mp3, mp4, wav, mkv, avi
* **Minecraft:** litematic, schematic, jar
* **Torrents:** torrent
* **Certificados:** pfx, p7b, cer
* **Desarrollo:** jsx, jnlp, log, ini, json, py, js
* **Otros:** Archivos que no coincidan con las extensiones anteriores.

## Funcionamiento técnico

* El script comprueba la carpeta cada 10 segundos.
* Ignora archivos temporales (`.tmp`, `.crdownload`, `.part`) y accesos directos (`.lnk`).
* Si un archivo está en uso por otro programa, el script espera al siguiente ciclo para moverlo.

## Detener el proceso

Al ejecutarse sin ventana, el proceso no es visible en la barra de tareas. Para detenerlo:

1. Abrir el Administrador de Tareas.
2. Buscar el proceso `pythonw.exe` o `Python`.
3. Finalizar la tarea.