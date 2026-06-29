from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/validate', methods=['GET', 'POST'])
def validate():
    data = request.json or request.args.to_dict()
    print("Received:", data)
    return jsonify({"status": "valid", "message": "OK"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
