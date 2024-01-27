from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Here, you can add your backend logic, such as authentication or database interactions
    # For simplicity, let's just print the received data
    print(f"Received login request - Username: {username}, Password: {password}")

    return 'Login successful!'

if __name__ == '__main__':
    app.run(debug=True)
