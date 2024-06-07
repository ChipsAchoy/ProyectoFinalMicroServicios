# Usar una imagen base de Python
FROM python:3.9-slim


RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    python3-dev \
    build-essential

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo de requisitos y instalar dependencias
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copiar el código fuente en el contenedor
COPY . .


EXPOSE 8777

# Definir el comando de entrada predeterminado
CMD ["python", "main.py"]
