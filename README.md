# Demos de Raspberry Pi para sensores, camara y comunicacion TCP

Coleccion de scripts Python de 2017 para probar hardware comun en Raspberry Pi: sensor DHT11, pantalla LCD I2C, camara PiCamera, OpenCV, modulo ESP8266, servidor TCP y lectura de orientacion con MPU6050. El repositorio conserva su valor como material educativo y de referencia para laboratorios o prototipos con hardware de esa epoca.

## El problema

Cuando se trabaja con Raspberry Pi en cursos, laboratorios o prototipos, una parte importante del tiempo se pierde comprobando por separado si cada componente esta bien conectado, si las librerias funcionan y si los datos llegan correctamente. Sin scripts pequenos de prueba, diagnosticar una falla puede mezclarse con problemas de hardware, red, permisos o dependencias.

## La solucion

Este proyecto reune demos independientes para validar cada pieza del sistema. Cada archivo se puede ejecutar de forma puntual para confirmar una funcion concreta: leer temperatura y humedad, mostrar datos en LCD, capturar imagen o video, detectar rostros, levantar un servidor web sencillo para un MPU6050, visualizar orientacion en 3D o probar comunicacion TCP con un ESP8266.

## Funcionalidades principales

- Lectura de temperatura y humedad con sensor DHT11.
- Envio de lecturas a ThingSpeak mediante una API key configurada por variable de entorno.
- Escritura de lecturas en pantalla LCD conectada por I2C.
- Captura de fotos y video con PiCamera.
- Captura de video con OpenCV.
- Deteccion basica de rostros con OpenCV y Haar Cascade.
- Servidor web con `web.py` para exponer angulos calculados desde un MPU6050.
- Visualizacion 3D con Pygame y PyOpenGL a partir de lecturas remotas.
- Cliente y servidor TCP para pruebas de comunicacion local.
- Pruebas de conexion WiFi y TCP con ESP8266 por comandos AT.

## Que mejora este proyecto

- Reduce el tiempo de diagnostico al separar las pruebas por componente.
- Ayuda a distinguir fallas de cableado, red, librerias o codigo.
- Sirve como base didactica para cursos de IoT, sensores y vision computacional en Raspberry Pi.
- Evita dejar secretos en el codigo usando variables de entorno para valores sensibles o dependientes del entorno.

## Para quien esta pensado

- Estudiantes que estan aprendiendo Raspberry Pi, sensores e IoT.
- Docentes o instructores que necesitan demos cortos para laboratorio.
- Personas que estan armando prototipos con DHT11, LCD I2C, PiCamera, MPU6050, ESP8266 u OpenCV.

## Tecnologias utilizadas

- Python.
- Raspberry Pi GPIO/I2C mediante librerias de hardware.
- Adafruit DHT para DHT11.
- SMBus para LCD I2C y MPU6050.
- PiCamera.
- OpenCV.
- PySerial para comunicacion serial con ESP8266.
- `web.py` para servidor HTTP simple.
- Pygame y PyOpenGL para visualizacion 3D.
- Sockets TCP.
- ThingSpeak como servicio externo opcional para telemetria.

## Requisitos

El proyecto requiere una Raspberry Pi o un entorno compatible con el hardware usado por cada demo.

Dependencias Python declaradas en `requirements.txt`:

```bash
pip install -r requirements.txt
```

Algunas dependencias de Raspberry Pi pueden requerir paquetes del sistema o instalacion especifica segun la version del sistema operativo, por ejemplo soporte I2C, camara, OpenCV o librerias de desarrollo.

## Instalacion

```bash
git clone <url-del-repositorio>/raspberry-pi-sensor-demos.git
cd raspberry-pi-sensor-demos
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

En Linux o Raspberry Pi OS, la activacion del entorno virtual suele ser:

```bash
source .venv/bin/activate
```

## Configuracion

Copia el archivo de ejemplo y ajusta los valores para tu entorno:

```bash
copy .env.example .env
```

En Linux o Raspberry Pi OS:

```bash
cp .env.example .env
```

Variables disponibles:

| Variable | Uso |
| --- | --- |
| `THINGSPEAK_API_KEY` | API key de escritura para enviar datos a ThingSpeak desde `cloud_temp.py`. |
| `TCP_SERVER_HOST` | Host usado por los scripts TCP y ESP8266. |
| `TCP_SERVER_PORT` | Puerto usado por los scripts TCP y ESP8266. |
| `LEVEL_SENSOR_URL` | URL del servidor que expone lecturas de orientacion para `level.py`. |

No subas el archivo `.env` al repositorio.

## Base de datos

Este proyecto no incluye base de datos, migraciones ni seeds.

## Ejecutar el proyecto

Cada demo se ejecuta de forma independiente. Algunos ejemplos:

```bash
python temperatura.py
python lcd_temp.py
python cloud_temp.py
python server.py
python level.py
python tcp_server.py
python tcp_cliente.py "mensaje de prueba"
python opencv.py
python opencv_video.py
python picamara.py
python picamara_sec.py
python picamera_video.py
python face.py
```

Los scripts `tcp_test.py` y `tcp_test2.py` esperan SSID y password como argumentos para enviar comandos AT al ESP8266:

```bash
python tcp_test.py "NOMBRE_WIFI" "PASSWORD_WIFI"
```

La contrasena se enmascara en la salida para evitar que quede completa en logs.

## Uso

1. Conecta el componente que quieres probar.
2. Activa las interfaces necesarias en Raspberry Pi, como I2C o camara.
3. Configura las variables de entorno cuando el script lo requiera.
4. Ejecuta el demo correspondiente.
5. Revisa la salida en consola, pantalla LCD, ventana de OpenCV/Pygame o servicio remoto.

## Estructura del proyecto

```text
.
|-- cloud_temp.py          # Envia temperatura y humedad a ThingSpeak
|-- temperatura.py         # Lee DHT11 y muestra valores en consola
|-- lcd_temp.py            # Muestra lecturas del DHT11 en LCD I2C
|-- lcd_i2c_driver.py      # Driver basico para LCD I2C
|-- server.py              # Servidor web para angulos del MPU6050
|-- level.py               # Visualizador 3D de orientacion
|-- tcp_server.py          # Servidor TCP local
|-- tcp_cliente.py         # Cliente TCP local
|-- tcp_test.py            # Prueba ESP8266 por serial USB
|-- tcp_test2.py           # Prueba ESP8266 por serial UART
|-- opencv.py              # Captura de imagen con PiCamera y OpenCV
|-- opencv_video.py        # Video con PiCamera y OpenCV
|-- face.py                # Deteccion de rostros con OpenCV
|-- picamara*.py           # Demos de foto, secuencia y video con PiCamera
|-- requirements.txt
|-- .env.example
`-- .gitignore
```

## Capturas

El proyecto no incluye capturas reales por el momento. Pueden agregarse despues de ejecutar los demos en hardware real.

## Seguridad

- Los secretos no deben almacenarse en el codigo fuente.
- Usa variables de entorno y conserva solo placeholders en `.env.example`.
- No subas `.env`, claves privadas, bases de datos locales, dumps, backups ni archivos generados por la camara.
- Si una credencial fue expuesta en Git, eliminarla del archivo actual no basta: debe rotarse o revocarse y, si aplica, limpiarse del historial.

## Pruebas

No hay suite automatizada de pruebas en este proyecto. La validacion principal es manual sobre el hardware correspondiente.

Comprobaciones recomendadas:

```bash
python -m py_compile *.py
```

## Estado del proyecto

Material educativo historico de 2017, preparado para revision y publicacion como referencia. No hay evidencia suficiente para declararlo listo para produccion.

## Limitaciones actuales

- Los scripts dependen de hardware especifico y no todos pueden ejecutarse en un equipo de escritorio.
- Parte del codigo usa patrones y librerias comunes en Raspberry Pi alrededor de 2017; puede requerir adaptaciones para sistemas actuales.
- No existe suite automatizada de tests.
- `face.py` requiere el archivo `haarcascade_frontalface_default.xml`, que no esta incluido en el proyecto.
- Algunas librerias de Raspberry Pi pueden requerir instalacion fuera de `pip` segun el sistema operativo.
- Los scripts son demos independientes; no forman una aplicacion unificada.

## Proximas mejoras

- Agregar una guia por componente con diagrama de conexion.
- Incorporar scripts de verificacion por hardware.
- Agregar pruebas unitarias para funciones puras.
- Parametrizar puertos seriales y pines desde variables de entorno.
- Incluir capturas reales de cada demo funcionando.

## Contribuciones

1. Haz un fork del repositorio.
2. Crea una rama para tu cambio.
3. Mantén los ejemplos sin credenciales reales ni datos personales.
4. Prueba el script modificado en el hardware correspondiente cuando aplique.
5. Abre un pull request describiendo el cambio y la validacion realizada.

## Licencia

Este proyecto todavia no incluye un archivo de licencia.
