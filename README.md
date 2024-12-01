
## 📖 Descripción
Esta aplicación permite descargar música desde YouTube utilizando `yt-dlp`, convertirla a formato MP3 con `FFmpeg`, y subirla automáticamente al almacenamiento en la nube a tu servicio FTP. También genera un enlace público para compartir el archivo subido.

---

## 🌟 Características
- 🎧 Descarga de audio de YouTube en buena calidad (192 kbps).
- 🔄 Conversión automática a MP3 utilizando `FFmpeg`.
- 🆔 Generación de nombres únicos para los archivos subidos.
- 📤 Subida automatizada al almacenamiento FTP.
- 🧹 Limpieza automática de archivos temporales para optimizar espacio en el servidor.

---

## 💻 Requisitos
1. 🐍 Python 3.7 o superior.
2. 📦 Librerías requeridas (puedes instalarlas con `pip install -r requirements.txt`):
    - `yt-dlp`
    - `imageio-ffmpeg`
    - `ftplib` (viene preinstalada con Python).
3. 🔑 Configuración de credenciales FTP:
    - Usuario, contraseña y host del almacenamiento FTP.

---

## ⚙️ Instalación
1. Clona este repositorio en tu máquina:
    ```bash
    git clone https://github.com/Alvaro17mz/yt-to-mp3-proyectomz.git
    cd yt-to-mp3-proyectomz
    ```
2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
3. Crea un archivo llamado `ftp_login.json` en el directorio raíz del proyecto con el siguiente contenido.
    ```bash
    {
        "FTP_USER": "tu-usuario",
        "FTP_HOST": "tu-host",
        "FTP_PASSWD": "tu-contraseña",
        "STREAM_URL": "link-publico"
    }
    ```
---

## 🚀 Uso
1. Ejecuta el programa:
    ```bash
    python main.py
    ```
2. Pega el enlace de YouTube cuando se te solicite.
3. El programa descargará, convertirá y subirá automáticamente el archivo a tu servicio FTP.
4. 📎 Recibirás un enlace público para compartir.

---

## 📝 Ejemplo de salida
```plaintext
App Funcionando...
Pega el link de musica de youtube: 
Ejemplo: https://www.youtube.com/watch?v=UgYSUYamucI
Procesando link: https://www.youtube.com/watch?v=UgYSUYamucI
Cancion descargada: Nombre-de-la-canción.mp3
===============================
Enlace de la canción: https://music.example.com/abc123.mp3
===============================
```

---

## 🤝 Contribución
Este proyecto es de uso personal. Si deseas mejorarlo, puedes enviar ideas o pull requests.

---

## ⚠️ Advertencia
Este proyecto es de uso personal y no está afiliado ni respaldado por YouTube, ni ninguna otra plataforma mencionada. Asegúrate de cumplir con los términos de servicio de YouTube y otros servicios utilizados.
