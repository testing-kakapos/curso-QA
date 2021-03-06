[![Build Status](https://travis-ci.org/testing-kakapos/curso-QA.svg?branch=master)](https://travis-ci.org/github/testing-kakapos/curso-QA)
[![codecov](https://codecov.io/gh/testing-kakapos/curso-QA/branch/master/graph/badge.svg)](https://codecov.io/gh/testing-kakapos/curso-QA)

### Descripción
Rastreador de incidencias de tráfico en Granada, con análisis de las mismas, que sirve los resultados en una plataforma web a partir de una API.

### Contribuidores

Nombre             | Username Github
------------------ | ------------------
 Tarek Bouali | [**@iambouali**](https://github.com/iambouali)
 Guillermo Bueno | [**@guillergood**](https://github.com/Guillergood)

### Herramientas 

Se han discutido las tecnologías en el siguiente [issue](https://github.com/testing-kakapos/curso-QA/issues/6).

* Servidor en cloud: sobre `Debian`.
* API: se usará una `API` pública para obtener la información necesaria.
* Sitio web: en python con el framework `Dash` (capa sobre Flask).
* Gráficos de datos: con la librería `Plotly`, con soporte de Javascript y Python.



### Instrucciones

Para poder ejecutar el proyecto se necesitan instalar las dependencias que vienen en el fichero `requirements.txt`.

Se pueden instalar estas dependencias de forma automatica mediante el siguiente comando: 

```
pip install -r requirements.txt
```

Para ejecutar los tests:

```
pyflow test test
```

Para poder ejecutar los tests de cobertura necesitaremos ejecutar alguno de los siguientes comando:
```
pyflow test coverage
```
O (recomendado):
```
pytest --cov=./flaskr/app/tests/
```

### Licencia

[**GNU GENERAL PUBLIC LICENSE**](https://github.com/testing-kakapos/curso-QA/blob/master/LICENSE)
