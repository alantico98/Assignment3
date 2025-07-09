# Makefile for Dockerized Streamlit App

# Define variables for the image name and tag
IMAGE_NAME := sentiment-api
CONTAINER_NAME := sentiment-api-container

build:
	@echo "Building Docker image: $(IMAGE_NAME)"
	docker build -t $(IMAGE_NAME) .

run:
	@echo "Running Docker container..."
	docker run --rm -p 8000:8000 --name $(CONTAINER_NAME) $(IMAGE_NAME)

stop:
	@echo "Stopping Docker container..."
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true

clean:
	@echo "Removing Docker image: $(IMAGE_NAME)"
	docker rmi $(IMAGE_NAME) || true