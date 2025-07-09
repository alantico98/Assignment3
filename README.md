# Movie Review Sentiment Analyzer

This app uses a Naive Bayes classifier to analyze movie reviews and predict whether they are **positive** or **negative**.

## Prerequisites

Before running this app, make sure you have the following installed:

### 1. Python 3.7+

You can check your version with:

```bash
python --version
```

### 2. pip (Python package manager)

pip --version

### 3. Git

```bash
git --version
```

### 4. WSL 2 Backend (Windows users only)

```bash
wsl --version
```

### 5. Docker Installed (required)

```bash
docker --version
```

## How to Run

Follow these steps to run the app locally (using Docker):

1. Clone the repo using bash (if on Windows, use WSL that allows for ssh cloning):

    bash
    
    git clone git@github.com:alantico98/Assignment3.git
    
    (If not already done) cd Assignment3

2. (Optional ) Create a virtual environment (Skip this if you're only running the app via Docker)

    python -m venv .venv
    
    source .venv\Scripts\activate # If using Windows
    
    source .venv/Scripts/activate # If using Git-bash or WSL on Windows
    
    source .venv/bin/activate     # If using Linux

3. Build the image (using WSL or Mac)

    make build

4. Run the Container (using WSL or Mac)

    make run
    
    Using Postman Desktop, send a request to http://0.0.0:8000/health to check that the
    server is running and healthy

5. Stop and Clean Up (using WSL or Mac)

    make stop
    
    make clean