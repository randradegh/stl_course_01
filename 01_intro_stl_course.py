####
## Status: revisado
## Fecha revisión: 20230302
####

##
# Utilerías del proyecto
##
from utils import *

#st.markdown(my_footer, unsafe_allow_html=True)
# Título
header("9 casos de negocio con Streamlit")
st.subheader("1. ¡Bienvenidos al Curso!")
st.subheader("Introducción")

st.markdown(""" 
    En esta sesión se expondrán  los objetivos del curso y se repasarán rapidamente los conceptos 
    que se establecieron como requerimientos.

    Además, revisaremos el ambiente de desarrollo que usaremos en el curso: Miniconda.
""")

st.subheader("Objetivos")
"""
    Los objetivos del curso son los siguientes:
"""
st.info("""

    - Instalar y configurar un ambiente de desarrollo que permita ejecutar una aplicación hecha con Python y Streamlit en los sistemas operativos Linux y Windows;
    - Conocer los comandos básicos de la biblioteca Streamlit;
    - Revisar en que situaciones usar los diversos tipos de gráficos;
    - Conocer los elementos básicos de un tablero de control (*dashboard*);
    - Revisar algunos casos de uso de Streamlit para visualización de datos para negocios;
    - Desplegar la aplicación en el sitio de Streamlit.
""")

st.subheader("Conocimientos básicos previos")
st.markdown("""
    - Linux o Windows
    - HTML básico
    - CSS básico
    - Python
        - Manejo básico del lenguaje
        - Bibliotecas
            - Pandas
            - Plotly Express
            - Otras bibliotecas
    - Una cuenta en Github
    - Tener instalado en su equipo Conda o Miniconda y Pip
    - Creación de ambientes de desarrollo con Miniconda o Pip
    - Un poco de inglés puede ser de ayuda
""")
st.subheader("Ambiente de desarrollo")

st.write("""
    Para el curso usaremos el lenguaje de programación Python (el cual es uno de los requisitos) 
    y la biblioteca Streamlit en un ambiente de desarrollo creado y administrado con Conda.
           
    Crearemos y configuraremos el ambiente de desarrollo necesario para la ejecución de las aplicaciones que desarrollaremos.
""")

st.markdown("""
    **Python**

    > *Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código. Se trata de un lenguaje de programación multiparadigma,  ya que soporta parcialmente la orientación a objetos, programación imperativa y, en  menor medida, programación funcional. Es un lenguaje interpretado, dinámico y multiplataforma.     Administrado por la Python Software Foundation, posee una licencia de código abierto, denominada Python Software Foundation License.*
    Python se clasifica frecuentemente como uno de los lenguajes de programación más populares.
    
    [Python, Wikipedia](https://es.wikipedia.org/wiki/Python)

    **Conda y Miniconda**

    El ambiente de desarrollo para el curso será [Conda](https://anaconda.org/anaconda/conda) o Miniconda.

     > *Conda es un sistema de gestión de paquetes de código abierto y un sistema de gestión del entorno para instalar múltiples versiones de paquetes de software y sus dependencias y cambiar fácilmente entre ellos. Funciona en Linux, OS X y Windows. Fue creado para programas     Python, pero puede empaquetar y distribuir cualquier software.*
""")

st.subheader("Configuración de Conda")

st.markdown("""
**Anaconda, Miniconda y Conda**
- Requerimientos del sistema
    - Computadora de 32 o 64 bits:
    - Para Miniconda, 400 MB de espacio en disco;
    - Para Anaconda, mínimo 3 GB de espacio en disco para descargar e instalar;
    - Windows, macOS, or Linux;
    - Para Windows: Windows 8.1 o mejor para Python 3.9, o Windows Vista o mejor para Python 3.8.
""")

st.subheader("Creación del ambientes de desarrollo para el curso")

st.markdown("""
    - Revisando las versiones instaladas, en Linux
""")

"""
`$python --version`

    Python 3.10.8

`$pip --version`

    pip 22.3.1 from /home/randrade/miniconda3/envs/stl_course/lib/python3.10/site-packages/pip (python 3.10)

`$conda --version`

    conda 22.11.1

"""
"""
- Instalación y actualización de pip

`$ pip install --upgrade pip`

    Requirement already satisfied: pip in /home/randrade/miniconda3/envs/stl_course_ready/lib/python3.9/site-packages (21.2.4)

    Collecting pip

    Using cached pip-22.0.4-py3-none-any.whl (2.1 MB)

    Installing collected packages: pip

    Attempting uninstall: pip

    Found existing installation: pip 21.2.4

    Uninstalling pip-21.2.4:

      Successfully uninstalled pip-21.2.4

    Successfully installed pip-22.0.4

- Instalación de Miniconda

    - Installing on Linux
    Download the installer:

    Miniconda installer for Linux.

        https://docs.conda.io/en/latest/miniconda.html#linux-installers

    In your terminal window, run:

    Miniconda:

    `~bash Miniconda3-latest-Linux-x86_64.sh`

- Instalación de los paquetes necesarios para el curso

A lo largo de las sesiones crearemos varias aplicaciones con Streamlit, en las cuales usaremos diversas bibliotecas de funciones, las cuales instalaremos en su momento en el ambiente base creado.

Las bibliotecas mínimas que usaremos (e instalaremos en su caso) serán:

- Streamlit

`pip install streamlit`

- Pandas

`conda install -c anaconda pandas`

- Plotly
`conda install -c plotly plotly`

- Pydeck
`conda install -c conda-forge pydeck`


- numpy
`conda install -c anaconda numpy`

¡OJJJO!
- SciPy
`conda install -c anaconda scipy`

___
"""

#footer("Copyrigth © 2023, RAF")
