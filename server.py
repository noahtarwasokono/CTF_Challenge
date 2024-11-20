from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session
import base64

app = Flask(__name__)
app.secret_key = 'your_secret_key'

VALID_USERNAME = "admin"
VALID_PASSWORD = "password"

def encode_cookie_value():
    # Example encoded cookie value
    clue = "flag{CTF_partial_flag_edit_me_123}"
    return base64.b64encode(clue.encode('utf-8')).decode('utf-8')

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Validate credentials
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            # Store the username in session
            session['username'] = username

            # Set a cookie and redirect to the cookie page
            response = make_response(redirect(url_for('cookie_page')))
            response.set_cookie('flag_cookie', encode_cookie_value())
            return response
        else:
            # Flash an error message and reload the login page
            flash('Incorrect username or password. Please try again.')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/cookie_page', methods=['GET'])
def cookie_page():
    # Get the username from the session
    username = session.get('username')

    # Check if the user has a valid cookie
    flag_cookie = request.cookies.get('flag_cookie')
    if flag_cookie:
        return render_template('cookie.html', username=username)  # Pass username to the template
    else:
        return "No flag cookie found. Please log in first.", 403

@app.route('/reveal_flag', methods=['GET'])
def reveal_flag():
    # Get the manipulated cookie value
    cookie_value = request.args.get('cookie')

    # Correct manipulated cookie value
    correct_flag = "flag{CTF_partial_flag_complete_123}"

    # Final flag to reveal upon success
    revealed_flag = "flag{CTF_final_flag_success_67890}"

    # Check if the manipulated cookie matches the correct value
    if cookie_value and cookie_value == correct_flag:
        return f"Congratulations! You found the real flag: {revealed_flag}"
    else:
        return "Invalid flag value. Try again!", 403

if __name__ == '__main__':
    app.run(debug=True)


