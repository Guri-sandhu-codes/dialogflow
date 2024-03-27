from flask import Flask, jsonify, request

app = Flask(__name__)


# Route to return student number in JSON format
@app.route('/')
def get_student_number():
    student_number = "YourStudentNumberHere"
    return jsonify({"student_number": 200553737})


# Route to handle webhook requests for restaurant finder and opening hours intents
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(force=True)
    intent_name = req['queryResult']['intent']['displayName']

    if intent_name == 'FindRestaurant':
        # Logic to handle restaurant finder intent
        # Extract parameters from request if necessary
        # Perform restaurant search based on parameters
        # Generate response text for Dialogflow
        response_text = "Here are some restaurants matching your criteria..."
    elif intent_name == 'GetOpeningHours':
        # Logic to handle opening hours intent
        # Extract restaurant name and day from request
        restaurant_name = req['queryResult']['parameters']['restaurant_name']
        day = req['queryResult']['parameters'].get('day', None)
        # Perform lookup of opening hours based on restaurant name and day
        # Generate response text for Dialogflow
        response_text = f"The opening hours are 10 AM - 11 PM" 
    else:
        response_text = "Sorry, I couldn't understand your request."

    return jsonify({"fulfillmentText": response_text})


if __name__ == '__main__':
    app.run(debug=True)
