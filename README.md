# ci-cd-project

This project uses data from Kaggle called "Vehicle Dataset 2024" found at https://www.kaggle.com/datasets/kanchana1990/vehicle-dataset-2024. 

The goal of the project is to create a simple linear regression model to predict the price of a car based on make-year-mileage. The latest version predicts price with R^2 = 0.48.


## Github Actions: CI/CD pipeline
This Repo is using Github Actions CI/CD workflow with tests run with each push, including style checks for all Python files. Also, there are unit tests run with each push to confirm the .pkl file of the model is valid, and also to confirm the accuracy of the model for a few selected data points. 


The "Build and Push Docker Image" workflow is still in progress, and next steps include creating Docker images with GitHub Container Registry to be able to use the linear regression model to make predictions.

