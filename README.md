# ML Operations
This repository will be used to manage all the course content and develop models & flows.

Possible Structure of the repo:
mlops/
│── data/                  # Store datasets
│   ├── raw/               # Unprocessed data
│   ├── processed/         # Cleaned datasets
│   ├── lab2/              # Lab-specific data
│       ├── mlflow.db      # Experiment tracking DB
│── experiments/           # MLflow and experiment logs
│   ├── mlruns/            # Stores all MLflow tracking runs
│   ├── lab2/              # Lab-specific tracking
│       ├── mlflow.db      # SQLite tracking for lab2
│── labs/                  # Jupyter Notebooks & development work
│   ├── lab1_development.ipynb
│   ├── lab2_exp_tracking.ipynb
│── models/                # Store trained models
│   ├── checkpoints/       # Intermediate saved models
│   ├── final/             # Production-ready models
│── src/                   # Source code
│   ├── data/              # Data ingestion & transformation scripts
│   ├── models/            # Model training, evaluation, inference scripts
│   ├── tracking/          # Scripts for MLflow tracking
│── logs/                  # Logs for debugging & execution tracking
│── config/                # Config files for parameters, paths, etc.
│── scripts/               # Shell scripts for automation
│── README.md              # Documentation
│── requirements.txt       # Dependencies
│── .gitignore
