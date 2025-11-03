from flask import Flask, render_template, request, jsonify
from ranpass import generate_password  # ✅ Correct import

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('front.html')  # ✅ Make sure this file is in templates/

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    length = int(data.get('length', 8))
    password = generate_password(length)
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)
