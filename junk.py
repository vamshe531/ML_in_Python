#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 23:01:43 2018

@author: vamshi
"""

from flask import Flask, request

app  = Flask(__name__)

@app.route('/query-example')

def query_example():
    language = request.args.get('language')
    framework = request.args.get('framework')
    return '''<h1> The language is :{}</h1>
              <h1>The framework value is: {}</h1>'''.format(language,framework)


@app.route('/form-example', methods =['GET','POST'])
def form_example():
    if request.method =="POST":
        language = request.form.get("language")
        framework = request.form.get("framework")
        return '''<h1> The language is :{}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language,framework)


    return '''<form method="POST">
                    Language: <input type="text" name="language"><br>
                    Framework: <input type="text" name="framework"><br>
                    <input type="submit" value="Submit"><br>
              </form>'''


@app.route('/json-example')
def json_example():
    return "Reddy"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
