from flask import Flask,render_template,url_for, request ,send_from_directory
import joblib
app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    return render_template('predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    Attr1 = request.form['Attr1'] 
    Attr2 = request.form['Attr2'] 
    Attr3 = request.form['Attr3'] 
    Attr4 = request.form['Attr4'] 
    Attr5 = request.form['Attr5'] 
    Attr6 = request.form['Attr6'] 
    Attr7 = request.form['Attr7'] 
    Attr8 = request.form['Attr8'] 
    Attr9 = request.form['Attr9'] 
    Attr10 = request.form['Attr10']
    X = [[int(Attr1), int(Attr2),int(Attr3), int(Attr4), int(Attr5),int(Attr6), int(Attr7), int(Attr8),int(Attr9),int(Attr10)]]
    prediction = model.predict(X)
    

    return render_template('final.html', prediction='Detected_YES {}'.format(prediction))
if __name__ == "__main__":
    app.run(debug=True)