from flask import Flask, render_template,request
from app.utils import Prediction
import app.CONFIG as path



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form

    project_obj = Prediction(data)
    result= project_obj.output_prediction()
    return render_template('index.html',result= result)
    


if __name__ == "__main__":
    app.run(debug=True,host=path.host,port=path.port)