# Define variables para la IP de Kafka y la dirección pública
KAFKA_IP="3.95.33.16" # Cambia esto a tu IP de Kafka
PUBLIC_IP="http://ec2-3-88-32-98.compute-1.amazonaws.com:5000" # Cambia esto a tu IP pública

# Instalar Docker
sudo apt update
sudo apt install -y docker.io
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose


# Clonar los repositorios
git clone https://github.com/dockersamples/example-voting-app.git 
git clone https://github.com/MariaCutipa/ExamenInDAEA.git

# Copiar archivos necesarios
cp -f ExamenInDAEA/Vote/app.py example-voting-app/vote/
cp -f ExamenInDAEA/Vote/requirements.txt example-voting-app/vote/
cp -f ExamenInDAEA/Vote/index.html example-voting-app/vote/templates/


# Modificar app.py en kafka-redis
sed -i "s/44.211.43.47:9092/$KAFKA_IP/g" ExamenInDAEA/kafka-redis/app.py
sed -i "s/ENV KAFKA_SERVERS=.*/ENV KAFKA_SERVERS=$KAFKA_IP/" ExamenInDAEA/kafka-redis/Dockerfile

# Modificar app.py en vote
sed -i "s/bootstrap_servers='44.211.43.47:9092'/bootstrap_servers='$KAFKA_IP'/g" example-voting-app/vote/app.py

# Modificar index.html para la dirección pública
sed -i "s|http://ec2-54-164-120-0.compute-1.amazonaws.com:5000|$PUBLIC_IP|g" example-voting-app/vote/templates/index.html

mv ExamenInDAEA/docker-compose.yml .

# Levantar la aplicación
sudo docker-compose up --build -d