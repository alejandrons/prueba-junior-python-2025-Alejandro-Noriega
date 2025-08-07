## Prueba técnica Bayma 2025

@autor: Alejandro Noriega Soto

El contenido del siguiente repositorio consta de la solución de la prueba técnica requerida por la empresa Bayma Internet Servicios Comerciales S.L.U.
para el puesto de desarrollador Python/.NET.

### Organización:

El repositorio consta de tres módulos:

📦 prueba-junior-python.2025
├── 📁 parte1_mysql/
│   └── 📄 main.py
├── 📁 parte2_api/
│   └── 📄 main.py
├── 📁 parte3_webhook/
│   └── 📄 main.py
├── 📄 requirements.txt
├── 📄 .gitignore
└── 📄 README.md

### Instalación y ejecución

La prueba técnica ha sido desarrollada con diversas librerías para Python buscando la mayor simplicidad posible, las librerías usadas son:

* MySQLConnector
* Dotenv
* Requests
* FastAPI

Se recomienda que para la ejecución de los scripts contenidos en cada carpeta se cree un entorno virtual de python donde se almacenen las dependencias
de manera controlada y no colisionen con otras posibles versiones ya instaladas en el sistema anfitrión.

Para crear un entorno virtual de Python desde Windows e instalar las dependencias puede usarse el comando en la terminal situado en la raíz del proyecto:

```
py -m venv .venv
pip install -r requirements.txt
```

Nota: Dentro del archivo .gitignore ya está contemplado la omisión de los archivos concernientes a las dependencias para evitar saturar de código innecesario
el proyecto.

### Reto 1: MySQL

Para este reto se decidió usar la librería **MySQLConnector** debido que tiene compatibilidad con el motor de base de datos suministrado por el cliente en
los requisitos de diseño; por otra parte, para la ejecución del script es necesaria la creación de un archivo *.env* con las credenciales de acceso a la 
base de datos, es por ello que se proporciona un archivo *.env.example* con los nombres de las variables de entorno requeridas por el script para realizar
la conexión de manera exitosa.

Una vez conectado a la base de datos se proporciona un menú por consola que permite al usuario del script interactuar con las diferentes opciones
contempladas según los requisitos de diseño del reto:

1. Listar los clientes activos dados de alta en los últimos 60 días, ordenados de manera descendente por fecha.
2. Insertar un nuevo cliente (Se piden los datos necesarios por consola y se realiza la inserción en la base de datos).
3. Desactivar un cliente cambiando su atributo activo por cero (0) especificando su e-mail.
4. Terminar la ejecución del menú.

Cabe resaltar que después de ejecutada la función el script regresa automáticamente al menú, sin embargo, el resultado de las funcionalidades
puede verse antes de regresar al menú para validar que el programa se ejecute correctamente.

Como nota aclaratoria, no se optó por separar las funcionalidades por módulos de python en scripts diferentes debido a la poca cantidad de requisitos
funcionales y que no se dan pistas de escalabilidad del sistema.

### Reto 2: Consumo de una API

Para la consecución de este reto se decidió utilizar la librería **Requests** que permite realizar peticiones HTTP de manera sencilla en lenguaje
Python; al igual que en el reto anterior, también se crea un menú por consola que ofrece las funcionalidades contempladas en los requisitos
otorgados por el usuario:

1. Mostrar los títulos de todos los posts del usuario con ID = 1.
2. Añadir un nuevo post (se pide el título y el contenido por consola).
3. Actualizar el título de un post existente (se pide el título del post actual y el nuevo título por consola).
4. Terminar la ejecución del menú.

Como en el reto anterior, una vez ejecutada cada funcionalidad el script regresa de nuevo al menú principal para permitir la ejecución de otras
funcionalidades, a su vez, también hay una opción limpia para la finalización del script.

### Reto 3: Creación de un Endpoint

Como último, para la realización de este reto se optó por usar la librería **FastAPI** para la creación del endpoint que la empresa Bayma necesita.

Para el levantamiento del servidor que contiene el endpoint se debe ejecutar por terminal (ubicado en la carpeta *parte3_webhook*) el comando:

```
uvicorn main:app
```

Y una vez levantado el servidor, se puede dirigir a la página web otorgada por uvicorn en la ruta **/docs** y probar la petición REST desarrollada
(en este caso *POST*)

Cabe resaltar que por la falta de especificidad sobre el almacenamiento de las notificaciones recibidas por el endpoint se optó por guardar los
datos en una lista de python disponible durante la actividad del servidor, de ser necesario, puede contemplarse el almacenamiento de las
notificaciones de manera persistente.

### Notas Finales

* Debido al tamaño de cada reto se optó por una arquitectura monolítica para su solución, de ser necesario que el sistema sea resiliente a escalabilidad en las funcionalidades puede cambiarse la arquitectura.
* Las librerías escogidas buscan la mayor facilidad y mantenibildad del código a largo plazo.
* Como mecanismo de seguridad y mayor adaptabilidad del código a diferentes equipos se escoge usar variables de entorno que eviten la revelación de credenciales dentro del repositorio donde se almacena el código.
* Se entiende que el cliente final del software tiene preferencia por el motor de base de datos administrado por Oracle *"MySQL"*, sin embargo la transición del código contenido en el primer reto de un motor de base de datos a otro no es complicada.
* En el historial del repositorio quizás no puede observarse, pero como buena práctica se dividió la solución de cada reto en una rama diferente de git, se aseguró que cada solución fuera funcional y después de solucionado el reto completo se combinaron todas las ramas a la rama principal, ésto para asegurar que no hubiera conflictos y tener organizado el desarrollo de la solución a cada reto.
* Los ejemplos de ejecución y capturas de pantalla de la solución a cada reto pueden encontrarse en la carpeta *ejemplos_uso* donde se puede observar la solución a cada reto y cada requisito en funcionamiento.