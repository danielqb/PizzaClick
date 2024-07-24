# Dockerfile

# Usar una imagen base oficial de Python
FROM python:3.9-slim AS pizzaclick

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el contenido del proyecto al directorio de trabajo
COPY apps/pizzaclick .

# Copiar los archivos de requerimientos y luego instalarlos
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Exponer el puerto que usará la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# Usar una imagen base oficial de Python
FROM python:3.9-slim AS pizzatable

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de requerimientos y luego instalarlos
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copiar el contenido del proyecto al directorio de trabajo
COPY apps/pizzatable .

# Exponer el puerto que usará la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]