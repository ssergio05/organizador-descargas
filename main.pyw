import os
import shutil
import time 

# --- CONFIGURACIÓN ---
folder_path = r"C:\Users\TU_USUARIO\Downloads"

extension_map = {
    "Imágenes":   [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv", ".doc"],
    "Ejecutables": [".exe", ".msi", ".zip", ".rar", ".7z"],
    "Audio_Video": [".mp3", ".mp4", ".wav", ".mkv", ".avi"],
    "Minecraft":  [".litematic", ".schematic", ".jar"], 
    "Torrents":   [".torrent"],
    "Certificados": [".pfx", ".p7b", ".cer"],
    "Desarrollo": [".jsx", ".jnlp", ".log", ".ini", ".json", ".py", ".js"]
}

folder_icons = {
    "Imágenes":   "🖼️",
    "Documentos": "📄",
    "Ejecutables": "🚀",
    "Audio_Video": "🎬",
    "Minecraft":  "⛏️",
    "Torrents":   "magnet🧲",
    "Certificados": "🔒",
    "Desarrollo": "💻",
    "Otros":      "📦"
}

def organizar_archivos():
    """Función principal que revisa y mueve los archivos"""
    # Variable para saber si hemos hecho algo en esta vuelta
    cambios_realizados = 0

    for filename in os.listdir(folder_path):
        # 1. Rutas absolutas
        file_path = os.path.join(folder_path, filename)

        # 2. Seguridad: Si es carpeta, ignorar
        if os.path.isdir(file_path):
            continue

        name, extension = os.path.splitext(filename)
        extension = extension.lower()

        # 3. Seguridad: Ignorar archivos temporales o de descarga activa
        if extension in [".tmp", ".crdownload", ".part"]:
            continue
        
        # Ignorar archivos sin extensión o archivos ocultos de sistema
        if not extension:
            continue

        moved = False 

        # 4. Lógica de clasificación (Intento de mover)
        for folder_name, extensions_list in extension_map.items():
            if extension in extensions_list:
                destination_path = os.path.join(folder_path, folder_name)
                os.makedirs(destination_path, exist_ok=True)
                
                try:
                    shutil.move(file_path, os.path.join(destination_path, filename))
                    icon = folder_icons.get(folder_name, "✅")
                    print(f"{icon} {filename} -> {folder_name}")
                    moved = True
                    cambios_realizados += 1
                except PermissionError:
                    # Si el archivo está en uso (como tu PDF), no hacemos nada y esperamos
                    pass
                except Exception as e:
                    print(f"❌ Error moviendo {filename}: {e}")
                
                break 

        # 5. Si no encajó en ninguna (Carpeta Otros)
        if not moved:
            other_folder = "Otros"
            destination_path = os.path.join(folder_path, other_folder)
            os.makedirs(destination_path, exist_ok=True)
            
            try:
                shutil.move(file_path, os.path.join(destination_path, filename))
                icon = folder_icons.get("Otros", "⚠️")
                print(f"{icon} {filename} (Ext: {extension}) -> {other_folder}")
                cambios_realizados += 1
            except PermissionError:
                pass
            except Exception as e:
                print(f"❌ Error moviendo a Otros: {e}")

    # Solo imprimimos si hubo movimiento para no ensuciar la consola
    if cambios_realizados > 0:
        print(f"✨ Ciclo terminado. Se organizaron {cambios_realizados} archivos.")

# --- EL MOTOR DEL SERVICIO ---
if __name__ == "__main__":
    print(f"🤖 SERVICIO INICIADO vigilando: {folder_path}")
    print("Pulsa 'Ctrl + C' en la terminal para detenerlo.")
    print("-" * 40)
    
    try:
        while True:
            organizar_archivos()
            
            # Esperar 10 segundos antes de volver a mirar
            time.sleep(10) 
            
    except KeyboardInterrupt:
        print("\n🛑 Servicio detenido por el usuario.")