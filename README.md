# Extracción de datos wallmart
Elabora un proyecto o script para la extracción del menú de despensa del sitio
web https://super.walmart.com.mx/.
En este proceso, es necesario incluir un Dockerfile que permita la automatización del
proyecto o script.
Como resultado final, se deberá generar un archivo en formato JSON (respuesta en
un servicio) que contenga la información formateada de los departamentos,
categorías y subcategorías del menú de despensa, con el fin de visualizar de manera
clara la estructura de la información obtenida.

## Tecnologias usadas   
- **Scrapy python**
- **Docker**

## Comandos para correr la aplicación
```sh
git clone git@github.com:adcc662/Wallmart-Scrapy.git
cd Wallmart-scrapy
docker build -t walmart_menu .
docker run -v $(pwd):/app walmart_menu
```

## Recomendaciones
Tuve algunos bloqueos por parte de wallmart y tuve que hacer algunas modificaciones en el archivo ```settings.py```.

## Comentarios
Fue muy divertido hacer el challege y hacer investigación ya que tenía tiempo sin hacer web scraping.