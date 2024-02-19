from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return "Hello, welcome to our website";

@app.route('/home/<Saishna>')
def home1(Saishna):
    return "Hello," + Saishna;

@app.route('/home/<int:age>')
def home2(age):
    return "Age = %d" %age;


def about():
    return "This is about page";

app.add_url_rule("/about", "about", about)

if __name__ == "__main__":
    app.run(debug=True)
