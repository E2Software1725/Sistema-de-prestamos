# Este archivo es una nota sobre cómo diagnosticar errores comunes y configurar WSGI en PythonAnywhere.

"""
DIAGNÓSTICO DE ERROR 404 NOT FOUND EN PYTHONANYWHERE
------------------------------------------------------

Un error 404 ("Not Found") significa que el servidor está funcionando, pero no puede encontrar la página específica que estás pidiendo.

Pasos para diagnosticar el problema:

1.  **Revisar el Registro de Errores (Error Log):**
    *   Este es el paso MÁS IMPORTANTE. Siempre empieza por aquí.
    *   Ve a la pestaña "Web" en PythonAnywhere.
    *   Baja a la sección "Log files".
    *   Haz clic en el enlace que termina en ".error.log" (ej., `tu_sitio.pythonanywhere.com.error.log`).
    *   Los errores más recientes estarán al final del archivo. Búscalos y analízalos. Este log te dará una pista mucho más precisa si tu aplicación Django está lanzando alguna excepción.

2.  **Verificar las URLs de tu Proyecto (`urls.py`):**
    *   Un error 404 a menudo significa que no tienes una URL configurada para la dirección que estás visitando (por ejemplo, la página de inicio "/").
    *   Revisa tu archivo `prestamos_project/config/urls.py` para ver qué patrones de URL están definidos y si la URL que intentas visitar coincide con alguno.

3.  **Verificar `ALLOWED_HOSTS` en `settings.py`:**
    *   Aunque un error de `ALLOWED_HOSTS` suele resultar en un error 400 Bad Request (no un 404), es bueno asegurarse.
    *   En tu `settings.py`, la línea `ALLOWED_HOSTS` debería incluir el nombre de tu dominio de PythonAnywhere (ej., `'E2Software1725.pythonanywhere.com'`). La configuración actual (`if not DEBUG: ALLOWED_HOSTS.extend(['127.0.0.1', 'localhost'])`) es para desarrollo local, y en producción `DEBUG` es `False`, por lo que deberías asegurarte de que `RENDER_EXTERNAL_HOSTNAME` se esté leyendo correctamente o que el dominio de PA esté en `ALLOWED_HOSTS`.

---

CONFIGURACIÓN DEL ARCHIVO WSGI PARA DJANGO EN PYTHONANYWHERE
--------------------------------------------------------------

El archivo WSGI es el punto de entrada para que el servidor web de PythonAnywhere se comunique con tu aplicación Django.

**Ruta del archivo WSGI:** `/var/www/tu_usuario_pythonanywhere_com_wsgi.py` (ej. `/var/www/e2software1725_pythonanywhere_com_wsgi.py`)

**Contenido correcto para este archivo:**

```python
import os
import sys
from pathlib import Path

# Añade la ruta a la carpeta del proyecto que contiene manage.py
# En tu caso: /home/E2Software1725/Sistema-de-prestamos/prestamos_project
path = Path('/home/E2Software1725/Sistema-de-prestamos/prestamos_project')
if str(path) not in sys.path:
    sys.path.insert(0, str(path))

# Añade la ruta a la carpeta raíz del repositorio para que encuentre el .env
# En tu caso: /home/E2Software1725/Sistema-de-prestamos
parent_path = path.parent
if str(parent_path) not in sys.path:
    sys.path.insert(0, str(parent_path))

# Establece el módulo de configuración de Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

# Carga la aplicación WSGI de Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```
"""
