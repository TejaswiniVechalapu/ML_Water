from flask import Flask, render_template , request
import pickle 
import numpy as np
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        ph = request.form['ph']
        Hardness = request.form['Hardness']
        Solids = request.form['Solids']
        Chloramines = request.form['Chloramines']
        Sulfate = request.form['Sulfate']
        Conductivity = request.form['Conductivity']
        Organic_carbon = request.form['Organic_carbon']
        Trihalomethanes = request.form['Trihalomethanes']
        Turbidity= request.form['Turbidity']
        data=np.array([[float(ph),float(Hardness),float(Solids),float(Chloramines),float(Sulfate),float(Conductivity),float(Organic_carbon),float(Trihalomethanes),float(Turbidity)]])
        model=pickle.load(open('water_potability.pkl','rb'))
        prediction=int(model.predict(data))
    return render_template('index.html',prediction=prediction)

if __name__=='__main__':
    app.run(debug=True)


