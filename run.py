import os
from app import create_app
from dotenv import load_dotenv  # Carga de variables .env

# Cargar variables desde el archivo .env
load_dotenv()

app = create_app()

if __name__ == '__main__':
    # Puerto leído desde .env o 5000 por defecto
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, port=port)
  #  ejemplo