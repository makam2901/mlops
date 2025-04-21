# ML Operations
This repository will be used to manage all the course content and develop models & flows.

Following topics will be covered:
- Requirements gathering and system design
- Experiment tracking
- Registering artifacts
- Data versioning and quality
- Orchestration
- Infrastructure as code
- CI/CD/CT
- Model serving
- Model and operational monitoring

_**Current Workflow:**_

- **Lab 1: Set up and Organization**
  
  To instill the practice and discipline of standardizing your development process. Please, do not become too comfortable with a *specific* way of doing things. For example, it's nice if you like to organize your projects and documentation or style your code a certain way, but when you join a new team, you may be expected to switch over to their way of doing things. You must do this, and be a team player, even if you believe your way is the *right* way. It isn't. The *right* way is however the team decides, and it may change from team to team, company to company. If you are very opinionated, you may be lucky enough to join a new team that has not yet established their best practices, and then you can have your say and influence the team.

- **Lab 2: Experiment Tracking and Model Registery**
  
  In this lab you will each download a new dataset and attempt to train a good model, and use mlflow to keep track of all of your experiments, log your metrics, artifacts and models, and then register a final set of models for "deployment", though we won't actually deploy them anywhere yet

- **Lab 3: Data Quality and Version Control**
  
  The goal in this lab is to become familiar with the importance of keeping track of different versions of your data sets. Although we will use DVC in this lab, we are **not** trying to learn all we can about it. DVC has too much functionality for us to learn in a single lab.

- **Lab 4: Containerization and Orchestration**

  The goal of this lab is to get a little practice with creating Docker images and running containers, and then deploying those images in a kubernetes cluster on our laptops using minikube and kubectl.

- **Lab 5: Experiment Tracking with MLFlow (GCP)**

The goal of this lab is to get MLFlow running in GCP. Using MLFlow locally on our laptops is useful only for classroom assignments and small personal/work projects. In a team environment, where results need to be shared with multiple data scientists, or where multiple data scientists are working on multiple projects, MLFlow should be set up so that all team members can access it.

- **Lab 6: ML Workflows using Metaflow (Local)**

The goal in this lab is to create two flows, one for training our model (using the same dataset we selected for the previous MLFlow labs), and one for model scoring (sometimes called inference), and run these flows locally. We will likely modify our training flow later when we move Metaflow to GCP, and our scoring flow later when we get to the model deployment section of the course. We will also integrate MLFlow model registration with our flow.

- **Lab 7: ML Workflows using Metaflow (GCP)**

In this lab we will set up a scalable machine learning training pipeline using Metaflow and GCP and then test our ML training pipeline code from the previous lab.


_**Current Directory (Local)**_:
```
mlops/
├── .dvc/
├── .metaflow/
├── app/
├── data/
├── experiments/
├── homeworks/
├── labs/
├── metaflow_gcp/
├── mlflow_gcp/
├── mlflow_test/
├── models/
├── src/
├── .dvcignore
├── .gitignore
├── dvc.lock
├── dvc.yaml
├── params.yaml
├── README.md
└── requirements.txt
```

