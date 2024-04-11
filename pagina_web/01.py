from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='templates/img')

@app.route('/')

def home():
    return render_template ("home1.html")

@app.route('/comc')
def comc():
     return render_template ("comcepto.html")

@app.route('/his')
def his():
     return render_template ("historia.html")

@app.route('/tip')
def tip():
     return render_template ("tipos1.html")



if __name__ == '__main__':
    app.run(debug=True)