# Python 3.8-slim (Debian buster-slim based)
FROM python:3.8-slim

# Se indica mantenedor de la imagen
LABEL maintainer="Carlos Morales <carlos7ma@correo.ugr.es>"

# Se etiqueta la imagen para almacenarla en Github Container Registry
LABEL org.opencontainers.image.source https://github.com/carlosma7/medauth

# Etiquetas relativas a la imagen creada
LABEL build-date="21/10/2020"
LABEL description="Medical Authorization Project on Python3.8-slim debian based docker."
LABEL github.url="https://github.com/Carlosma7/MedAuth"
LABEL version="1.0.0"

# Se configura el PATH para ejecutar paquetes de Pip
ENV PATH=/home/medauth/.local/bin:$PATH

# Creación de usuario con permisos básicos
RUN useradd -ms /bin/bash medauth \
	&& mkdir -p app/test \
	&& chown medauth /app/test

# Se configura para utilizarse el usuario creado
USER medauth

# Se configura el directorio de trabajo
WORKDIR /app/test

# Se copia el fichero de requisitos de paquetes pip
COPY requirements.txt .

# Instalación de los requisitos y se borra el fichero tras la instalación
RUN pip install -r requirements.txt --no-warn-script-location \
	&& rm requirements.txt


# Ejecución
CMD ["invoke", "test"]
