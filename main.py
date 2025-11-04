import pickle
from flask import Flask,render_template,request
app=Flask(__name__)
load=pickle.load(open('brain_model.pkl','rb'))
@app.route('/')

def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])

def predict():
    if request.method=="POST":
        gender=int(request.form['gender'])
        age=int(request.form['age'])
        hypertension=int(request.form['hypertension'])
        heart_disease=int(request.form['heart_disease'])
        work_type=int(request.form['work_type'])
        Residence_type=int(request.form['Residence_type'])
        avg_glucose_level=int(request.form['avg_glucose_level'])
        bmi=int(request.form['bmi'])
        smoking_status=int(request.form['smoking_status'])
        prediction= load.predict([[gender,age,hypertension,heart_disease,work_type,Residence_type,avg_glucose_level,bmi,smoking_status]])
        if prediction==1:
            result="You Have Brain disease"
        else:
            result="You are healthy"
        return render_template("index.html",prediction_text="{}".format(result))
    return render_template("index.html")

if __name__=='__main__':
    app.run(debug=True)
    