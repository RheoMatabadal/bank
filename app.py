from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/munten')
def munten():
    return render_template('munten.html')

@app.route('/transacties')
def transacties():
    return render_template('transacties.html')

@app.route('/overzichten')
def overzichten():
    return render_template('overzichten.html')

if __name__=='__main__':
    app.run(debug=True)