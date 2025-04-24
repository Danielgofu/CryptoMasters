# Crypto API

## Descripción
Una API para gestionar criptomonedas utilizando Flask. Incluye funcionalidades como listar, agregar, actualizar y eliminar criptomonedas, además de estadísticas básicas. También cuenta con una interfaz web para visualizar datos y gráficos, y un modo oscuro para mejorar la experiencia del usuario.

---

## Características
- **API REST**:
  - Listar todas las criptomonedas.
  - Obtener detalles de una criptomoneda específica.
  - Agregar nuevas criptomonedas.
  - Actualizar información de una criptomoneda.
  - Eliminar criptomonedas.
- **Interfaz Web**:
  - Visualización de estadísticas como capitalización de mercado, volumen de 24h y dominio de Bitcoin.
  - Gráficos dinámicos generados con `Chart.js`.
  - Modo oscuro y diseño responsivo.
- **Pruebas Unitarias**:
  - Cobertura para las rutas principales de la API.

---

## Requisitos Previos
Antes de comenzar, asegúrate de tener instalado lo siguiente:
- Python 3.8 o superior
- `pip` (administrador de paquetes de Python)
- Git

---

## Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/crypto-api.git
   cd crypto-api
   ```

2. **Crea un entorno virtual**:
   ```bash
   python -m venv venv
   ```

3. **Activa el entorno virtual**:
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Configura la base de datos**:
   - La aplicación utiliza SQLite por defecto. Si necesitas configuraciones adicionales, crea un archivo `.env` en la carpeta `instance/` con las variables necesarias.

6. **Inicia la aplicación**:
   ```bash
   python main.py
   ```

7. **Accede a la aplicación**:
   - API: [http://127.0.0.1:5000/api/cryptos](http://127.0.0.1:5000/api/cryptos)
   - Interfaz web: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## Uso de la API

### Endpoints Disponibles

1. **Listar todas las criptomonedas**:
   - **GET** `/api/cryptos`
   - Respuesta:
     ```json
     [
       {
         "name": "Bitcoin",
         "symbol": "BTC",
         "current_price": 30000,
         "percentage_change": 2.5
       }
     ]
     ```

2. **Obtener una criptomoneda específica**:
   - **GET** `/api/cryptos/<symbol>`
   - Ejemplo: `/api/cryptos/BTC`

3. **Agregar una nueva criptomoneda**:
   - **POST** `/api/cryptos`
   - Cuerpo:
     ```json
     {
       "name": "Ethereum",
       "symbol": "ETH",
       "current_price": 2000,
       "percentage_change": 1.8
     }
     ```

4. **Actualizar una criptomoneda**:
   - **PUT** `/api/cryptos/<symbol>`
   - Cuerpo:
     ```json
     {
       "current_price": 2500,
       "percentage_change": 2.0
     }
     ```

5. **Eliminar una criptomoneda**:
   - **DELETE** `/api/cryptos/<symbol>`

---

## Pruebas

1. **Ejecutar las pruebas unitarias**:
   Asegúrate de estar en el entorno virtual y ejecuta:
   ```bash
   python -m unittest discover -s tests
   ```

2. **Cobertura de las pruebas**:
   - Pruebas para listar criptomonedas.
   - Pruebas para obtener una criptomoneda específica.
   - Pruebas para agregar, actualizar y eliminar criptomonedas.

---

## Estructura del Proyecto

```
crypto-api/
├── app/
│   ├── __init__.py          # Configuración de la aplicación Flask
│   ├── models.py            # Definición del modelo Cryptocurrency
│   ├── routes.py            # Rutas de la API
│   ├── templates/
│   │   └── index.html       # Interfaz web
│   └── static/
│       └── style.css        # Estilos CSS
├── tests/
│   └── test_routes.py       # Pruebas unitarias
├── instance/
│   └── database.db          # Base de datos SQLite (generada automáticamente)
├── main.py                  # Punto de entrada de la aplicación
├── requirements.txt         # Dependencias del proyecto
├── README.md                # Documentación del proyecto
└── .gitignore               # Archivos y carpetas ignorados por Git
```

---

## Modo Oscuro

La aplicación incluye un botón para alternar entre modo claro y oscuro. Este botón se encuentra en la esquina inferior derecha de la interfaz web.

---

## Notas Adicionales

- **Base de Datos**:
  - Por defecto, se utiliza SQLite. Si deseas cambiar a otra base de datos (como PostgreSQL o MySQL), actualiza la configuración en `app/__init__.py`.

- **Extensiones**:
  - La API utiliza `flasgger` para generar documentación Swagger automáticamente. Puedes acceder a ella en: [http://127.0.0.1:5000/apidocs](http://127.0.0.1:5000/apidocs).

---

## Contribuciones

Si deseas contribuir al proyecto:
1. Haz un fork del repositorio.
2. Crea una rama para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza un pull request.

---

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.