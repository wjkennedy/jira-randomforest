# Use an official Jupyter runtime as the base image
FROM jupyter/scipy-notebook

# Set the working directory
WORKDIR /app

# Copy the requirements file and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the pickle file and the notebook file
COPY classifier.pkl .
COPY a9ai.ipynb .

# Expose the port for the notebook
EXPOSE 8888

# Run the command to start the notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser"]

