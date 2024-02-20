from importlib.resources import files

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def upload():
    return render_template("file_upload.html")


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files.getlist("file")
        for file in f:
            file.save(file.filename)
        return render_template("success.html",name=file.filename)

if __name__ =='__main__':
    app.run(debug = True)