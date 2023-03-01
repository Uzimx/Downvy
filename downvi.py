import pytube

# Establecer la URL del video de YouTube

video = input("introduce la url del video a descargar:\n")
video_url = video

# Crear un objeto de YouTube
youtube = pytube.YouTube(video_url)

# Obtener la mejor resolución disponible del video
video = youtube.streams.get_highest_resolution()

# Descargar el video en el directorio actual
video.download()

while True:
    respuesta = input("¿Desea descargar otro archivo? (sí/no): ")
    if respuesta.lower() == "sí":
        # El usuario ha elegido continuar, así que el ciclo continúa
        continue
    elif respuesta.lower() == "no":
        # El usuario ha elegido salir del programa, así que el ciclo termina
        break
    else:
        # El usuario ha proporcionado una respuesta no válida, así que se le pedirá que lo intente de nuevo
        print("Respuesta no válida. Inténtalo de nuevo.")





