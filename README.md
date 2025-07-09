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

### 5. Docker Installed (for containerized setup)

```bash
docker --version
```

## How to Run

Follow these steps to run the app locally (using Docker):

1. Clone the repo using bash (if on Windows, use WSL that allows for ssh cloning):

    bash
    git clone git@github.com:alantico98/COMP_4705_Adv_Topics_MLOps_Assignments.git
    (If not already done) cd COMP_4705_Adv_Topics_MLOps_Assignments

2. (Optional ) Create a virtual environment (Skip this if you're only running the app via Docker)

    python -m venv .venv
    source .venv\Scripts\activate # If using Windows
    source .venv/Scripts/activate # If using Git-bash or WSL on Windows
    source .venv/bin/activate     # If using Linux

3. Build the image (using WSL or Mac)

    make build

4. Run the Container (using WSL or Mac)

    make run
    
    Navigate to Local URL: https://localhost:8501

5. Stop and Clean Up (using WSL or Mac)

    make clean