import os
from google.cloud import dialogflow
from flask import Flask, request, jsonify
from flask_cors import CORS

from google.protobuf.json_format import MessageToJson
import json

app = Flask(__name__)
CORS(app)


def detect_intent_text(project_id, session_id, text, language_code='en-US'):
    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "AidriveCredentials.json"

    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )

    return response.query_result


def main():
    # project_id = 'test-chatbot-mkbn'
    project_id = 'aidrive-project'
    session_id = '0123D34'

    while True:
        user_input = input("User: ")
        if user_input.lower() == 'exit':
            break

        response = detect_intent_text(project_id, session_id, user_input)
        print(f"Bot: {response.fulfillment_text}")


@app.route('/api/endpoint', methods=['POST'])
def chatbot_api():
    user_message = request.json.get('message', '')
    project_id = 'aidrive-project'
    session_id = '0123E34'

    response = detect_intent_text(project_id, session_id, user_message)
    bot_response = response.fulfillment_text
    return jsonify({'botResponse': bot_response})


if __name__ == "__main__":
   
    # main()
