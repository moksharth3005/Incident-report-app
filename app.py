from flask import Flask, render_template, redirect, request, session, url_for

app = Flask(__name__)
app.secret_key = "NationalIncidientReportAppByMoksharth1234@$"

@app.route('/', methods=['POST', 'GET'])
def login():
    if 'user' in session:
        return redirect(url_for('incidents'))  # Redirect logged-in users to the incident page
    elif request.method == 'POST':
        # Check if 'email' and 'password' fields exist in the form data
        if 'email' in request.form and 'password' in request.form:
            user = request.form['email']
            session['user'] = user
            return redirect(url_for('incidents'))
        else:
            return 'Bad Request: Email or password field is missing.'
    else:
        return render_template("login.html")
    
@app.route("/incident", methods=["GET", "POST"])
def incidents():
    if 'user' in session:
        return "You are logged in!"
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/Create_Account', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        # Check if 'signup', 'sighuppass', and 'DOB' fields exist in the form data
        if 'signup' in request.form and 'sighuppass' in request.form and 'DOB' in request.form:
            signup_email = request.form['signup']
            signup_password = request.form['sighuppass']
            dob = request.form['DOB']

            # Handle account creation logic here

            return 'Your Response has been recorded. You can now log in.'
        else:
            return 'Bad Request: Form data is missing or invalid.'
    else:
        return render_template("sighup.html")

if __name__ == "__main__":
    app.run(debug=True)