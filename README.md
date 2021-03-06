
# Servicio de solicitudes de autorizaciones médicas

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Language](https://img.shields.io/badge/Language-Python-red.svg)](https://www.python.org/)

[![Build Status](https://travis-ci.com/Carlosma7/MedAuth.svg?branch=main)](https://travis-ci.com/Carlosma7/MedAuth) [![Build Status](https://circleci.com/gh/Carlosma7/MedAuth.svg?style=svg)](https://app.circleci.com/pipelines/github/Carlosma7/MedAuth) [![Run Status](https://api.shippable.com/projects/5fca65728d5266000640fc4c/badge?branch=main)](https://app.shippable.com/github/Carlosma7/MedAuth/dashboard/jobs) [![Build Status](https://github.com/Carlosma7/MedAuth/workflows/GitHub-Actions-CI/badge.svg)](https://github.com/Carlosma7/MedAuth/actions?query=workflow%3AGitHub-Actions-CI)

---

![Logo MedAuth](./doc/img/logo_medauth.png "Logo MedAuth")

---

**MedAuth** es una plataforma para empresas en el sector de la salud, destinada a resolver los problemas derivados de la gestión de autorizaciones médicas. Es una herramienta que pretende realizar el proceso de una autorización médica de un modo ágil, no presencial y lo más automatizado posible.

## Información del proyecto

---

:hospital: [Introduccion](https://carlosma7.github.io/MedAuth/doc/descripcion_problema).

:triangular_ruler: [Arquitectura](https://carlosma7.github.io/MedAuth/doc/arquitectura) del proyecto.

:hammer: [Herramientas](https://carlosma7.github.io/MedAuth/doc/justificacion_herramientas) utilizadas.

:round_pushpin:[Roadmap](https://carlosma7.github.io/MedAuth/doc/roadmap) del proyecto.

:package: [Modelo actual](https://carlosma7.github.io/MedAuth/doc/modelo_inicial) del proyecto.

:computer: [Slides](https://slides.com/carlosma7/deck) de presentación del proyecto.

## Descarga del proyecto

**Con** Git.

```shell
git clone https://github.com/Carlosma7/MedAuth.git
```

**Con** GitHub CLI.

```shell
gh repo clone Carlosma7/MedAuth
```

**Sin** GitHub.

```shell
wget https://github.com/carlosma7/medauth/archive/main.zip
```

## Dependencias


```shell
pip3 install -r requirements.txt
```

## Ejecución

Para ejecutar el servidor, una vez instalados los requisitos previos y descargado el proyecto, se ejecuta la siguiente orden:

```shell
invoke execute
```

Para limpiar la caché, se ejecuta:

```shell
invoke clean
```

Para comprobar el estado, se pueden ejecutar los tests con:

```shell
invoke test
```

