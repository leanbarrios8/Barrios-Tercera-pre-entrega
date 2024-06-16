#Proyecto gestion de monedas con DJango

Descripcion:
Este es un proyecto dedicado a la creacion de monedas virtuales y administracion.

#Requisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Virtualenv (opcional pero recomendado)

### Instrucciones

1. Clona el repositorio:

    ```sh
    git clone https://github.com/tuusuario/tu-repositorio.git
    cd tu-repositorio
    ```
2. Instala las dependencias:

    ```sh
    pip install -r requirements.txt
    ```

3. Realiza las migraciones de la base de datos:

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Ejecuta el servidor de desarrollo:

    ```sh
    python manage.py runserver
    ```

5. Abre tu navegador y navega a `http://127.0.0.1:8000/`.

## Uso

### Crear una Moneda

1. Navega a `http://127.0.0.1:8000/monedas`.
2. Llena el formulario con el nombre y valor de la moneda.
3. Haz clic en "Enviar".
4. Serás redirigido a la página de `lista` donde podrás ver todas las monedas creadas.

### Ver la Lista de Monedas

1. Navega a `http://127.0.0.1:8000/lista`.
2. Verás una lista de todas las monedas creadas con sus nombres y valores.