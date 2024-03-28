from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    try:
        # Extract data from the webhook request
        data = request.get_json()
        file_name = data['file_name']
        object_url = data['object_url']

        # Process the received data (e.g., log, store in database)
        print(f'File uploaded: {file_name}, Object URL: {object_url}')

        return 'Webhook received successfully', 200

    except Exception as e:
        print(f'Error processing webhook data: {e}')
        return 'Error', 500

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production
