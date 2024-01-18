import cv2 ## Importar OpenCV --> pip install opencv-contrib-python
import os ## Permite aplicar operaciones en el sistema operativo.

# Abre la cámara predeterminada (índice 0)
camera = cv2.VideoCapture(0)

# Configura la resolución a 4K (4096x2160)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 4096)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)

# Carpeta a guardar las imagenes de Chooper.
output_folder = "Fotos_Chooper"

# Crear la carpeta si no existe.
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Variables para controlar el ciclo principal.
capturing = False
photo_count = 0

while True:
    ret, frame = camera.read()
    frame = cv2.flip(frame, 1) #Dar vuelta la imagen horizontalmente.
    cv2.imshow("Camara", frame)

    if ret: # Si la captura del fotograma fue exitosa...
        
        # Si se presiona la tecla ESPACIO , toma una foto.
        if cv2.waitKey(1) & 0xFF == ord(" "):
            photo_count += 1
            filename = os.path.join(output_folder, f"Chooper_{photo_count}.jpg") #Enlaza las dos rutas, output_folder y crea la ruta de la nueva imagen.
            cv2.imwrite(filename, frame)
            print(f"Foto guardada como {filename}")

        # Si se presiona la tecla "q", salir.
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

# Cierra la cámara y la ventana
camera.release()
cv2.destroyAllWindows()
