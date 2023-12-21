
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash



app = Flask(__name__)

@app.get('/')
def folio():
    return render_template("index.html")



if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)
