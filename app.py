# coding: utf-8
# -*- coding: utf-8 -*-
import flask
from flask import request,jsonify
from flask_cors import CORS
from flask import render_template
import joblib

    
    


app = flask.Flask(__name__)
from flask_cors import CORS
CORS(app)

@app.route('/')
def login():
    return render_template("index.html")
    
@app.route('/traitement',methods=['POST'])
def traitement():
    mot = request.form['mot']
    mot = str(mot)
    model = joblib.load('word embedding_model.ml')
    mots_similaire = model.most_similar(mot,topn=5)
    
    return render_template('index2.html',liste=mots_similaire)
    

app.run(debug=True)
