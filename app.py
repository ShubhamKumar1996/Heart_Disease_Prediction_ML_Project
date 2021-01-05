from flask import Flask
app = Flask(__name__)

from flask import render_template, redirect, request, flash, get_flashed_messages
from forms import HeartDiseaseForm
import pickle

app.config['SECRET_KEY'] = '497116cba458f36597855093fd31a1ac'

# load the ML model which we have saved in .pkl format
model = pickle.load(open("model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    form = HeartDiseaseForm()

    if request.method == "POST":
        age = int(request.form["age"])
        sex = int(request.form["sex"])
        cp = int(request.form["cp"])
        trestbps = int(request.form["trestbps"])
        chol = int(request.form["chol"])
        fbs = int(request.form["fbs"])
        restecg = int(request.form["restecg"])
        thalach = int(request.form["thalach"])
        exang = int(request.form["exang"])
        oldpeak = float(request.form["oldpeak"])
        slope = int(request.form["slope"])
        ca = int(request.form["ca"])

        prediction = model.predict([[age, sex, cp, trestbps, chol, fbs,
                                restecg, thalach, exang, oldpeak, slope, ca]])

        if prediction[0] == 0:
            flash("No Heart Disease")
        else:
            flash("Heart Disease")

        return redirect("/")

    messages = get_flashed_messages()

    return render_template("index.html",
                            title="Heart Disease Form",
                            form = form,
                            messages = messages)

if __name__ == "__main__":
    app.run(debug=True)
