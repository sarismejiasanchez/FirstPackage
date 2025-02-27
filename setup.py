from setuptools import setup, find_packages

setup(
    name="FirstPackage",                                            # Nombre del paquete
    version="0.1.0",                                                # Versión inicial
    packages=find_packages(),                                       # Paquetes a incluir
    description="Un paquete pip simple de saludo",                  # Breve descripción
    author="Sara María Mejía Sánchez",                              # Tu nombre
    author_email="sarismejiasanchez@platzi.com",                    # Tu correo electrónico
    url="https://github.com/sarismejiasanchez/FirstPackage",        # URL del proyecto
)