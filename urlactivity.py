from flask import redirect, url_for, Flask

app = Flask(__name__)

@app.route('/admin')
def admin():
    return "This is admin Site."

@app.route('/employer')
def employer():
    return "This is employer site."

@app.route('/worker')
def worker():
    return "This is worker site."

@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    if name == 'employer':
        return redirect(url_for('employer'))
    if name == 'worker':
        return redirect(url_for('worker'))

if __name__ =='__main__':
    app.run(debug = True)