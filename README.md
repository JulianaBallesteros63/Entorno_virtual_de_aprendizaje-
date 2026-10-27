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

## Definition of Done (DoD) — Proyecto EVA

### 1. Objetivo

Establecer los criterios que debe cumplir una funcionalidad del Entorno Virtual de Aprendizaje (EVA) para considerarse terminada, garantizando que su implementación cumpla con los requisitos definidos y pueda utilizarse correctamente dentro de la plataforma.

### 2. Criterios generales de finalización

Una funcionalidad se considera terminada cuando:

- El código está implementado dentro del proyecto Django.
- La funcionalidad cumple con el propósito para el cual fue desarrollada.
- Las vistas, las plantillas y las rutas relacionadas están configuradas.
- La interfaz permite al usuario interactuar con la funcionalidad de manera comprensible.
- Se verifica que las operaciones principales funcionen correctamente.
- Los cambios se integran con los componentes existentes del proyecto.
- El código se guarda en el repositorio de GitHub.
- La documentación se actualiza cuando se realizan cambios relevantes.

### 3. Funcionalidades implementadas

#### 3.1. Inicio de sesión

La funcionalidad de inicio de sesión permite a los usuarios ingresar a la plataforma mediante sus credenciales.

Criterios de finalización:

- El usuario puede ingresar su correo electrónico y contraseña.
- Django valida las credenciales utilizando su sistema de autenticación.
- El sistema muestra mensajes cuando el correo no está registrado o la contraseña es incorrecta.
- Las contraseñas se gestionan mediante los mecanismos de seguridad de Django.
- Se establece una sesión para el usuario autenticado.

#### 3.2. Cierre de sesión

La plataforma dispone de una funcionalidad para cerrar la sesión del usuario.

Criterios de finalización:

- El usuario puede cerrar su sesión desde la interfaz.
- Django finaliza la sesión activa.
- Después del cierre de sesión, el usuario es redirigido a la página de inicio de sesión.

#### 3.3. Registro de usuarios

La plataforma cuenta con una estructura de registro de usuarios para permitir la creación de cuentas.

Criterios de finalización:

- Se dispone de un formulario para ingresar los datos requeridos.
- Los datos se procesan mediante las vistas de Django.
- Las contraseñas se almacenan utilizando el mecanismo de protección de Django.
- Los datos del usuario se guardan en la base de datos cuando el registro es válido.

#### 3.4. Módulos educativos

La plataforma presenta módulos orientados al aprendizaje básico sobre sensores hídricos.

Criterios de finalización:

- Los módulos se presentan mediante páginas HTML integradas con Django.
- Los contenidos están relacionados con los sensores hídricos y sus aplicaciones.
- Se incluyen recursos visuales de apoyo cuando corresponden.
- El usuario puede navegar por los contenidos disponibles mediante los enlaces de la interfaz.

#### 3.5. Interfaz de navegación

La plataforma dispone de elementos de navegación para facilitar el acceso a sus diferentes secciones.

Criterios de finalización:

- La interfaz cuenta con enlaces hacia las secciones implementadas.
- Los botones y enlaces conducen a las rutas configuradas.
- La presentación mantiene una estructura visual coherente con el proyecto EVA.
- Las páginas utilizan las plantillas y los estilos definidos para la aplicación.

#### 3.6. Modelos y persistencia de datos

El proyecto utiliza los modelos de Django para representar y almacenar información de la aplicación.

Criterios de finalización:

- Los modelos contienen los campos definidos para la información gestionada.
- La base de datos permite almacenar y consultar los registros correspondientes.
- Las operaciones se realizan mediante el ORM de Django cuando aplica.
- Las migraciones requeridas se encuentran aplicadas en el entorno de ejecución.

### 4. Integración y control de versiones

Los cambios realizados en las funcionalidades implementadas se incorporan al proyecto y se gestionan mediante Git y GitHub.

Criterios de finalización:

- El código fuente se encuentra organizado dentro de la estructura de la aplicación.
- Los cambios relevantes se registran mediante commits.
- El repositorio contiene la documentación principal del proyecto.
- Las instrucciones de ejecución y las dependencias se mantienen actualizadas cuando corresponde.

### 5. Condición para declarar una funcionalidad como terminada

Una funcionalidad puede considerarse terminada cuando cumple los criterios que le corresponden, ha sido probada y funciona correctamente dentro del proyecto.

Las funcionalidades que todavía presentan errores o requieren integración adicional deben permanecer en desarrollo hasta que cumplan los criterios establecidos.

### 6. Alcance de esta definición

Este Definition of Done contempla las funcionalidades implementadas hasta el momento en el proyecto EVA: autenticación, cierre de sesión, estructura de registro, módulos educativos, navegación y persistencia de datos.

Las funcionalidades administrativas, como la asignación de roles desde un panel personalizado, no se consideran terminadas en esta versión de la definición y deberán validarse por separado antes de incorporarse como funcionalidades completadas.
