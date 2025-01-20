# Base Python image
FROM python:3.11-slim

# working dir
WORKDIR /app

# install dependencies based on requirements
COPY requirements.txt requirements.txt 
RUN pip install --no-cache-dir -r requirements.txt

# model file and columns list
COPY linear_model.pkl linear_model.pkl
COPY columns.pkl columns.pkl

# coppy the application code
COPY app.py app.py

# run the appwhich predicts prices
CMD ["python", "app.py"]

