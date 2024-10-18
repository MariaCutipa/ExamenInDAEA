# Configuración y Ejecución de la Aplicación

Este repositorio contiene un script para levantar una aplicación basada en Docker que incluye un sistema de votación, Redis y Kafka. A continuación, se detallan los pasos para configurar y ejecutar el proyecto.

## Requisitos

- Docker
- Docker Compose

## Instrucciones

### 1. Clonar el Repositorio
Clona el repositorio en tu máquina local:

```bash
git clone https://github.com/MariaCutipa/ExamenInDAEA.git
```

### 2. Modificar las IPs
Antes de ejecutar el script, asegúrate de modificar las siguientes variables en el script `manage.sh`:

```bash
# Cambia esto a tu IP de Kafka
KAFKA_IP="3.95.33.16"

# Cambia esto a tu URL pública donde se está ejecutando el script
PUBLIC_IP="http://ec2-3-88-32-98.compute-1.amazonaws.com:5000"
```

- `KAFKA_IP`: Debe ser la dirección IP donde se está ejecutando tu instancia de Kafka.
- `PUBLIC_IP`: Debe ser la misma IP donde se está ejecutando `manage.sh`, que es la dirección pública accesible de la aplicación.

### 3. Mover el Script

Después de clonar el repositorio, **no ejecutes el script `manage.sh` dentro de `ExamenInDAEA`**. Debes moverlo a la raíz de tu proyecto (directorio superior) antes de ejecutarlo:

```bash
mv ExamenInDAEA/manage.sh .
```

### 4. Ejecutar el Script

Asegúrate de que Docker y Docker Compose están instalados y funcionando. Si ya tienes Docker y Docker Compose instalados, puedes eliminar las líneas del script relacionadas con su instalación.

Ejecuta el script con:

```bash
chmod +x manage.sh
./manage.sh
```

### 6. Acceso a la Aplicación

Una vez que todos los contenedores estén en funcionamiento, podrás acceder a la aplicación en la URL pública que especificaste en `PUBLIC_IP`.
