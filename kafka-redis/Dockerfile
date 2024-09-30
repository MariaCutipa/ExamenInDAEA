# Usar una imagen base de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /usr/src/app

# Copiar el archivo de requisitos e instalar dependencias
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación al contenedor
COPY app.py ./

# Establecer las variables de entorno para Kafka y Redis (opcional)
ENV KAFKA_SERVERS=3.86.34.96:9092
ENV REDIS_HOST=redis

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]

