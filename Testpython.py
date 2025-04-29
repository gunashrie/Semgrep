
from flask import Flask, request, escape

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    # Potential XSS vulnerability if not using escape
    return f"Hello, {escape(name)}!"  # Use escape to prevent XSS

if __name__ == '__main__':
    app.run(debug=True)

