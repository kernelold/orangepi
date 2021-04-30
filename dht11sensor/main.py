#!/usr/bin/env python
from subprocess import check_output
from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def index():
  data = check_output(['./dht11']).split(' ')
  return render_template('dht11.html',data=data)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
