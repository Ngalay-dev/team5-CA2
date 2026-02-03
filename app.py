from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get the expression string from the frontend
    data = request.get_json()
    expression = data.get('expression', "")
    
    try:
        # Replicating your original eval() logic
        # Note: In a production app, you'd want to sanitize this!
        result = str(eval(expression))
        return jsonify({"result": result})
    except (SyntaxError, ZeroDivisionError, NameError):
        return jsonify({"result": "Error"})
 @app.route('/health', methods=['GET'])
 def health_check():
     return jsonify({
        "status": "UP"
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
