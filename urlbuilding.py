from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/admin')
def admin():
    return "This is admin"


@app.route('/librarian')
def librarian():
    return "This is librarian"


@app.route('/student')
def student():
    return "This is student"


@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for( "admin"))
    if name == 'librarian':
        return redirect(url_for("librarian"))
    if name == 'student':
        return redirect(url_for("student"))


if __name__ == '__main__':
    app.run(debug=True)