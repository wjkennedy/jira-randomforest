# Jira Random Forest Classifier
This project demonstrates how to use the Jira Python module to connect to Jira, present a text widget and submit button to allow a user to provide a JQL query, display the results of the query as a Pandas dataframe, and use the Project Key, Summary, Description, and Comments to train a random forest classifier. It also shows how to use the output from the training to recommend the appropriate project for a given issue and create the issue in the recommended project using the same OAuth credentials and reading from a config.properties file.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

A Jira instance

Python 3.6 or higher

Pip

Docker (optional)

## Installing

Clone the repository


    git clone https://github.com/<username>/jira-random-forest-classifier.git

### Install the dependencies

    pip install -r requirements.txt

Run the config_generator.ipynb notebook to generate a config.properties file.

Open the a9ai.ipynb notebook and run the cells to connect to Jira, present a text widget and submit button to allow a user to provide a JQL query, display the results of the query as a Pandas dataframe, and use the Project Key, Summary, Description, and Comments to train a random forest classifier. Use the output from the training to recommend the appropriate project for a given issue and create the issue in the recommended project using the same OAuth credentials and reading from a config.properties file.

Use the Dockerfile to build a container for the flask app, including the pickle file

Use the requirements.txt file that includes all the modules needed

Use the Dockerfile to run the Jupyter notebook and the flask app with gunicorn

Please note that this is an example and you may need to adjust it to fit your specific needs and directory structure.

----
## Jupyter Notebook
Connect to Jira using the Jira Python module and OAuth

Present a text widget and submit button for a user to provide a JQL query

Display the results of the query as a Pandas dataframe

Use the Project Key, Summary, Description, and Comments to train a random forest classifier


## Flask App
Use the output from the training to recommend the appropriate project for a given issue

Create the issue in the recommended project using the same OAuth credentials and reading from a config.properties file

Present the user input UI in the eBay application style and font

Add a comment with the metadata about the prediction and a label "a9ai"

Run with Gunicorn instead of the built-in Flask development server

## Docker

Create a Dockerfile for the Flask app, including the pickle file

Create a similar Dockerfile to run the Jupyter notebook

Includes a requirements.txt file that includes all the modules needed
