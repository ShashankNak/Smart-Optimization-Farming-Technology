from flask import Flask, request, jsonify, render_template
from model import model_predict


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/feature_screen')
def feature_screen():
    return render_template('feature_screen.html')

@app.route('/nutrition')
def nutrition():
    return render_template('nutrition.html')

@app.route('/fruits')
def fruits():
    return render_template('fruits.html')

@app.route('/weather')
def weather():
    return render_template('weather.html')

@app.route('/predict/<string:type>', methods=['POST'])
def predict(type):
    details = model_predict(request.form,type)
    return jsonify(details)
    



if __name__ == '__main__':
    app.run(debug=True)