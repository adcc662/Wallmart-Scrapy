docker build -t walmart_menu .
docker run -v $(pwd):/app walmart_menu