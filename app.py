from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample list of valid usernames and passwords
valid_users = {
    'admin': 'password123',
    'user1': 'qwerty',
    'user2': '123456'
}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/auth', methods=['POST'])
def auth():
    username = request.form['username']
    password = request.form['password']

    if username in valid_users and valid_users[username] == password:
        return redirect(url_for('external_redirect'))
    else:
        error_msg = 'Invalid username or password'
        return render_template('login.html', error=error_msg)

@app.route('/settings')
def settings():
    return 'Welcome to the router settings page'

@app.route('/external-redirect')
def external_redirect():
    return redirect('http://www.google.pl')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=8888)
