from flask import Flask, render_template

app = Flask(__name__)

'''@app.route('/')
def message():
    return render_template('message.html')'''


@app.route('/user/<Saishna>')
def message(Saishna):
    return render_template('message.html', name=Saishna)


@app.route('/table/<int:num>')
def table(num):
    return render_template('print-table.html', n=num)


@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/ttable')
def table1():
    return render_template('timetable.html')


if __name__ == '__main__':
    app.run(debug=True)
