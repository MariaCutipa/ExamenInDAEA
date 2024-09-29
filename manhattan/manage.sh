# Directorio de trabajo
WORKDIR="/tmp/recomendaciones"

# Clonar el repositorio
git clone https://github.com/MariaCutipa/ExamenInDAEA.git $WORKDIR

# Cambiar al directorio del repositorio
cd $WORKDIR/manhattan

# Construir la imagen Docker
docker build -t recomendacion .

# Ejecutar el contenedor con la aplicación Blazor
docker run -d --name mi-python-re -p 5000:5000 recomendacion

# Eliminar los archivos clonados después de la ejecución 
cd /tmp
rm -rf $WORKDIR

