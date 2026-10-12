# EVA - Entorno Virtual de Aprendizaje sobre Sensores Hídricos

## Descripción

EVA es un entorno virtual de aprendizaje desarrollado para apoyar la enseñanza del manejo básico de sensores hídricos en el Instituto Técnico Comercial de Capellanía (ITCC).

El proyecto busca facilitar el aprendizaje mediante recursos digitales sobre Arduino, pH, temperatura y turbidez del agua, así como actividades de evaluación.

## Tecnologías utilizadas

- Python
- Django
- SQLite
- HTML y CSS
- Bootstrap 5
- Git y GitHub

## Requisitos previos

Para ejecutar el proyecto se requiere:

- Python instalado.
- Git instalado.
- Una terminal como PowerShell o la terminal de Visual Studio Code.

## Instalación en Windows

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

Entrar en la carpeta del repositorio descargado:

```bash
cd Entorno_virtual_de_aprendizaje-
```

Si la carpeta del proyecto Django está dentro de `gestion_estudiantes`, entrar en ella:

```bash
cd gestion_estudiantes
```

**Nota:** ejecutar `cd gestion_estudiantes` únicamente si allí se encuentra el archivo `manage.py`.

### 2. Crear el entorno virtual

```bash
python -m venv venv
```

Activar el entorno virtual en PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

En CMD:

```cmd
venv\Scripts\activate.bat
```

### 3. Instalar las dependencias

Con el entorno virtual activado, ejecutar:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Preparar la base de datos

```bash
python manage.py migrate
```

### 5. Crear un administrador (opcional)

```bash
python manage.py createsuperuser
```

Seguir las instrucciones que aparecen en la terminal.

### 6. Ejecutar la aplicación

```bash
python manage.py runserver
```

Abrir en el navegador:

 http://127.0.0.1:8000/

## Funcionalidades

- Registro e inicio de sesión.
- Página principal del entorno virtual de aprendizaje.
- Consulta de módulos educativos sobre Arduino y sensores hídricos.
- Contenidos relacionados con pH, temperatura y turbidez del agua.
- Actividades de evaluación, según las funcionalidades implementadas.

## Estructura del proyecto

El repositorio contiene la carpeta `gestion_estudiantes`, donde se encuentra el proyecto Django. Dentro de ella están los archivos y las aplicaciones que conforman el sistema.

## Control de versiones

El proyecto utiliza Git para controlar los cambios y GitHub para alojar el código fuente.

## Consideraciones

- Las dependencias deben estar registradas en `requirements.txt`.
- Las migraciones de Django permiten preparar la estructura de la base de datos.
- Las plantillas HTML y los recursos estáticos necesarios deben estar incluidos en el repositorio.
- El servidor `runserver` se utiliza para desarrollo local.
