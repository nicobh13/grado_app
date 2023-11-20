Este sitio web fue el proyecto presentado como proyecto de grado en el año 2023 por las estudiantes Nicolle Bustamante Hernández y Laura Sofía Pineda Buitrago, pertenecientes a la especialidad de Diseño y Desarrollo de Sitios Web (P02) del Instituto Técnico Superior de Pereira.
Para dicho proyecto, se generó la propuesta de que, ya que la institución cumplió 80 años, se generara un sitio web enfocado hacia la misma.
Por esta razón, se comenzó con un proyecto de mejora a la comunicación del colegio, llamado Red de Hermes, para el cual los recursos gráficos y la identidad se le encargaron a Laura, y el desarrolllo del sitio a Nicolle. Se generó un portal institucional donde se podían generar canales de comunicación vía internet, correo electróninco y SMS.
En este repositorio se encuentran todos aquellos archivos alusivos al sitio web, y el proceso con el que se desarrollaron, con excepción a los archivos que corresponden al sistema de SMS y comunicaciones externas, pues para ello se utilizaron versiones de prueba que incluían datos personales de las autoras.

Para ejecutar el sitio web:
    1. Instale todos los archivos que se encuentran en el repositorio
    2. Asegurese de que el lenguaje python esté instalado en su equipo.
    3. Una vez instalado, dirijase a la terminal. Asegurese de que está en el mismo directorio del proyecto, y ejecute la linea:
        pip install -r requirements.txt
    Así, instalará todas las librerias necesarias para el proyecto. En caso de no querer estas librerias de manera global, puede establecer un entorno virtual antes de ejecutar la linea.
    4. En el archivo config.py, coloque los datos requeridos para la conexión a la base de datos MySQL, en la línea 8.
    5. En el archivo modelos.py, elimine las líneas de la 73 a la 77, para posteriormente entrar al Símbolo del Sistema, Powershell o alguna terminal donde pueda ejecutar las lineas:
        >python
        >from config import db
        >db.create_all()
        >db.session.commit()
        >exit()

        Y posteriormente, una vez se haya asegurado de que los modelos de la base de datos se crearon correctamente, vuelva a pegar las líneas borradas.
    6. Ejecute los archivos insertar_roles.py e insertar_grupos.py

Con estas configuraciones, el sitio web se debería poder observar sin problema alguno. Si desea poder observar libremente todos los archivos, registrese en el sitio, y posteriormente, ingrese al archivo hacer_admin.py, reemplace el target_email con el correo que registró y ejecute el archivo. Esto de dará acceso a todas las funcionalidades del sitio.

En caso de dudas o inquietudes sobre el sitio, puede enviar un correo:

    nicole.bustamante@itspereira.edu.co
