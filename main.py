import os
import random
import string
from yt_dlp import YoutubeDL
import imageio_ffmpeg as ffmpeg
from ftplib import FTP

# Conexion a FTP
FTP_USER = "tu-usuario"
FTP_HOST = "tu-host"
FTP_PASSWD = "tu-contraseña"
STREAM_URL = "link-publico"

# Carpeta donde almacena la musica para subirla
carpeta_temporal = "./descargas"

# Genera nombre corto
def url_corto():
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choices(caracteres, k=8))

# Descarga la musica con yt-dlp y convierte con FFmpeg
def yt_dl(url):
    if not os.path.exists(carpeta_temporal):
        os.makedirs(carpeta_temporal)
    descarga = {
        'format': 'bestaudio/best',
        'outtmpl': f'{carpeta_temporal}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': ffmpeg.get_ffmpeg_exe(),  # Indica la ubicación de FFmpeg portable
    }
    with YoutubeDL(descarga) as ydl:
        informacion = ydl.extract_info(url, download=True)
        ruta_musica = f"{carpeta_temporal}/{informacion['title']}.mp3"
        return ruta_musica, informacion['title']
    
# Sube la musica por ftp 
def subir_musica(ruta_musica, nombre_musica):
    with FTP(FTP_HOST) as ftp:
        ftp.login(user=FTP_USER, passwd=FTP_PASSWD)
        ftp.set_pasv(True) # Modo pasivo cambiar a False si no funciona
        with open(ruta_musica, 'rb') as archivo:
            ftp.storbinary(f"STOR {nombre_musica}", archivo)
        return f"{STREAM_URL}/{nombre_musica}"

# Descarga, generara un nombre aleatorio, y sube el archivo
def procesar_cancion(url):
    print(f"Procesando link: {url}")
    ruta_musica, nombre_musica = yt_dl(url)
    link_corto = url_corto() + ".mp3"
    print(f"Cancion descargada: {nombre_musica}")
    enlace_cancion = subir_musica(ruta_musica, link_corto)

# Ahorro de espacio en el servidor
    if os.path.exists(ruta_musica):
        os.remove(ruta_musica)
    return enlace_cancion

# Flujo principal
if __name__ == "__main__":
    print("App Funcionando...") # Le indica al Panel Pterodactyl que se encuentra funcionando
    try:
        while True: # Ciclo infinito para el panel
            print("\nPega el link de musica de youtube: ")
            print("Ejemplo: https://www.youtube.com/watch?v=9sYK_azN3Vo\n")
            youtube_url = input("Link: ")
            if not youtube_url:
                print("No se ingreso link")
                continue
            enlace_streaming = procesar_cancion(youtube_url)
            print("\n===============================")
            print(f"Enlace de la canción: {enlace_streaming}")
            print("===============================\n")

    except KeyboardInterrupt: # Para detener en el panel
        print("App Detenida...")
        