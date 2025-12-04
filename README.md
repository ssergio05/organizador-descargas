# 📂 Organizador de Archivos (Python Service)

Un script ligero (`.pyw`) que se ejecuta en segundo plano para mantener tu carpeta de descargas organizada automáticamente.

## 📦 Instalación

1.  **Descarga** el archivo `main.pyw`.
2.  **Configura la ruta:**
    * Abre el archivo con un editor de texto.
    * Busca `folder_path` y pon la ruta de tu carpeta de Descargas.
3.  **Activa el auto-arranque:**
    * Crea un **acceso directo** del archivo `main.pyw`.
    * Pulsa `Win + R`, escribe `shell:startup` y pulsa Enter.
    * Mueve el acceso directo a esa carpeta.

## 🚀 Cómo funciona

Al tener la extensión `.pyw`, el script se ejecuta utilizando el intérprete de Python sin ventana (windowless), por lo que no verás ninguna terminal molesta mientras trabajas.

* **Frecuencia:** Revisa la carpeta cada 10 segundos.
* **Consumo:** Mínimo (usa librerías nativas `os` y `shutil`).

## 🛑 Cómo detenerlo

Al no tener ventana visible, si necesitas detener el script:
1. Abre el Administrador de Tareas (`Ctrl + Shift + Esc`).
2. Busca el proceso **"Python"** o **"pythonw.exe"**.
3. Finaliza la tarea.