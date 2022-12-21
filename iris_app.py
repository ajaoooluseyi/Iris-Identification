from flask import Flask, render_template, request

import pickle
import numpy as np

app = Flask(__name__)

iris = pickle.load(open(r'C:\Users\AJAO SEYI\Desktop\ML\iris identification\iris.pkl', 'rb'))


@app.route("/result", methods = ['GET', 'POST'])
def result():
        if request.method == 'POST':
            rawfeatures = [float(x) for x in request.form.values()]
            features = [np.array(rawfeatures)]
            prediction = iris.predict(features)
            return render_template("index.html", pred_text = "This is a {} flower!".format(prediction))
        else:
            return render_template("index.html")


@app.route("/sub", methods = ['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['username']
    return render_template('sub.html', n = name)


if __name__ == "__main__":
    app.run(debug=True)
