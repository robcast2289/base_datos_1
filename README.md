# Proyecto Base de Datos 1

Proyecto del curso de Base de Datos 1, de la carrera de Ingeniería en Sistemas de la Universidad Mariano Gálvez de Guatemala

## Requerimientos
- Python 3.10

## Instalación

- Clonar el proyecto
```bash
$ git clone git@github.com:robcast2289/base_datos_1.git
```
- Entrar a la carpeta del proyecto
```bash
$ cd base_datos_1
```
- Crear ambiente virtual
Si se usa Visual Studio con plugins de Python presionar **Ctrl + Shift + P** y     seleccionar Python: Create Enviroment. Esto creara automaticamente el ambiente virutal e instalará los paquetes necesario.

- Instalar cliente de Oracle
    - [Descargar el paquete del cliente](https://www.oracle.com/database/technologies/instant-client/linux-x86-64-downloads.html) Para este proyecto en Linux con Oracle 21c, descargar el paquete llamado **instantclient-basic-linux.x64-21.11.0.0.0dbru.zip**
    - Crear la carpeta oracle en el directorio opt
    ```bash
    $ sudo mkdir /opt/oracle
    ```
    - Mover el archivo descargado al directorio creado y descomprimirlo
    ```bash
    $ sudo mv instantclient-basic-linux.x64-21.11.0.0.0dbru.zip /opt/oracle/
    $ sudo unzip /opt/oracle/instantclient-basic-linux.x64-21.11.0.0.0dbru.zip
    ``
    - Instalar libreria libaio1
    ```bash
    $ sudo apt-get install libaio1
    ```
    - Finalmente agregar la ruta de la variable externa al LD_LIBRARY_PATH
    ```bash
    $ vim ~/.bashrc
    ```
    - Y agregar esta linea al archivo .bashrc
    ```bash
    $ export LD_LIBRARY_PATH=/opt/oracle/instantclient_21_11:$LD_LIBRARY_PATH
    ```
    - Luego de grabar el archivo .bashrc ejecutar
    ```bash
    $ source ~/.bashrc
    ```