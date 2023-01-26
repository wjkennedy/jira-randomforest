import configparser
from jira import JIRA
from flask import Flask, request, jsonify
import pickle

# Load the classifier from the pickle file
with open('classifier.pkl', 'rb') as f:
    clf = pickle.load(f)

# Create a Flask app
app = Flask(__name__)

# Define a route for the user input
@app.route('/predict', methods=['POST'])
def predict():
    # Get the user input
    user_input = request.get_json(force=True)
    issue_keys = user_input.get('issue_keys', [])
    predictions = []
    if issue_keys:
        for key in issue_keys:
            # Retrieve the issue details
            issue = jira.issue(key)
            summary = issue.fields.summary
            description = issue.fields.description
            comments = [c.body for c in jira.comments(issue)]
            # Use the classifier to predict the appropriate project
            prediction = clf.predict([[summary,description,comments]])
            predictions.append({'issue_key': key, 'prediction': prediction[0]})
    else:
        # Use the classifier to predict the appropriate project
        prediction = clf.predict([user_input])
        predictions.append({'prediction': prediction[0]})
    # Return the prediction as a json object
    return jsonify(predictions)

# Run the app
if __name__ == '__main__':
    app.run(port=8000, debug=True)


# Connect to the Jira instance using the OAuth credentials
jira = JIRA(
    'https://yourjirainstance.com',
    oauth={
        'access_token': access_token,
        'access_token_secret': access_token_secret,
        'consumer_key': client_id,
        'key_cert': client_secret
    }
)

# Retrieve the prediction from the classifier
prediction = classifier.predict(issue_data)

# Create a new issue in the recommended project
issue = jira.create_issue(project=prediction['project'], summary='Issue Summary', description='Issue Description')

# Add a comment with the metadata about the prediction and a label "a9ai" to the newly created issue
jira.add_comment(issue, f"Predicted project: {prediction['project']}\nConfidence: {prediction['confidence']}\nLabel: a9ai")

