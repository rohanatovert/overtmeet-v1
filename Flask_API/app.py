from flask import Flask, request, jsonify
from datetime import datetime
import json
app = Flask(__name__)

# List to store transcripts
transcripts = []

@app.route('/api/transcripts', methods=['POST'])
def receive_transcript():
    data = request.json

    if 'username' not in data or 'transcription' not in data or 'timestamp' not in data:
        return jsonify({"error": "Invalid JSON format"}), 400

    username = data['username']
    transcription = data['transcription']
    timestamp = data['timestamp']

    # Store the received transcript
    transcripts.append({"username": username, "transcription": transcription, "timestamp": timestamp})

    # Sort the transcripts based on timestamps
    transcripts.sort(key=lambda x: datetime.fromisoformat(x['timestamp']))

    return jsonify({"message": "Transcript received successfully"})

@app.route('/api/stop', methods=['POST'])
def stop_transcripts():
    # Save transcripts to a file, database, or perform any desired action
    save_transcripts_to_file()

    return jsonify({"message": "Transcripts stopped and saved successfully"})

def save_transcripts_to_file():
    # For simplicity, this example saves transcripts to a file
    filename = f"transcripts_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
    with open(filename, 'w') as json_file:
        json.dump(transcripts, json_file, indent=4)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8501)