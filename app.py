# -*- coding: utf-8 -*-

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from movie_recommended_complete import movie_recommendations
app = Flask(__name__,template_folder='template')



@app.route("/")
def home():
    return render_template('index.html')
@app.route("/index")
def index():
    return render_template('index.html')

@app.route('/predict' ,methods=['POST'])
def predict():
    x= request.form["Movie"]
    
    predictm= movie_recommendations(x)
    
    return render_template('index.html', prediction_text='Suggested movies are $ {}'.format(predictm))

@app.route("/seri")
def seri():
    return render_template('series.html')
@app.route("/movi")
def movi():
    return render_template('movie.html')
if __name__ == "__main__":
    app.run(debug= False)