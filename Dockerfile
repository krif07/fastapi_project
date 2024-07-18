# Usar una imagen base oficial de Python
FROM python:3.10

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar los archivos de requisitos al contenedor
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copiar el resto del código de la aplicación al contenedor
COPY . .

# Exponer el puerto que usará la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
