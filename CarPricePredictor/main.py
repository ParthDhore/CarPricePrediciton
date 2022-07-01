from flask import Flask,render_template,request, jsonify
import pickle
app=Flask(__name__)
model=pickle.load(open('carprediction_randomforest.pkl','rb'))
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    fuel_type_petrol=0
    fuel_type_diesel=0
    if request.method=='POST':
        Year=int(request.form['years'])
        curprice=float(request.form['curprice'])
        kms=int(request.form['kms'])
        owners=int(request.form['owners'])
        fuel_type=request.form['fuel']
        if(fuel_type=='petrol'):
            fuel_type_petrol=1
        elif(fuel_type=='diesel'):
            fuel_type_diesel=1
        seller=request.form['seller_type']
        if(seller=='Individual'):
            individual=1
        else:
            individual=0
        transmission=request.form['transmission']
        if(transmission=='Manual'):
            manual=1
        else:
            manual=0
        predictions=model.predict([[curprice,kms,owners,Year,fuel_type_diesel,fuel_type_petrol,individual,manual]])
        output=round(predictions[0],2)
        return render_template('index.html',final_prediction="You can sell the car at {}".format(output))
    
    else:
        return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)
