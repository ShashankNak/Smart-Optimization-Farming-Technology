import tensorflow as tf
import pickle

def model_predict(form,type):
    form = form.to_dict()
    if type == 'nutrition':
        print(form)
        soilColor = form['soilColor']
        nitrogen = int(form['nitrogen'])
        phosphorous = int(form['phosphorous'])
        potassium = int(form['potassium'])
        pH = float(form['pH'])
        rainfall = int(form['rainfall'])
        temperature = int(form['temperature'])

        # model prediction
        model = tf.keras.models.load_model('models/crop-model.h5')

        with open('models/labels/crop_txt', 'rb') as f:
            crop_label = pickle.load(f)

        with open('models/fertilizers-model', 'rb') as f:
            fertilizer_label = pickle.load(f)

        with open('models/labels/soil_color_txt', 'rb') as f:
            soil_color_label = pickle.load(f)
        
        for key,value in soil_color_label.items():
            if value == soilColor:
                soilColor = key
                break
        
        prediction = model.predict([soilColor,nitrogen,phosphorous,potassium,pH,rainfall,temperature])

        crop = crop_label[tf.argmax(prediction[0])]
        fertilizer = fertilizer_label[crop]
        return {'crop':crop,'fertilizer':fertilizer}

    if type == 'weather':
        N = form['N']
        P = form['P']
        K = form['K']
        temperature = form['temp']
        humidity = form['humidity']
        ph = form['ph']
        rainfall = form['rainfall']

        #model prediction
        with open('models/labels/crops_txt_shubh', 'rb') as f:
            weather_crop_label = pickle.load(f)

        # model prediction
        model = tf.keras.models.load_model('models/crop-nutriemts-model.h5')

        prediction = model.predict([N,P,K,temperature,humidity,ph,rainfall])

        weather_crop = weather_crop_label[tf.argmax(prediction[0])]
        return {'weather_crop':weather_crop}
    
    if type == 'fruits':
        N = form['N']
        P = form['P']
        K = form['K']
        pH = form['pH']
        EC = form['EC']
        S = form['S']
        Cu = form['Cu']
        Fe = form['Fe']
        Mn = form['Mn']
        B = form['B']
        Zn = form['Zn']
        #model prediction

        with open('models/labels/fruits_txt', 'rb') as f:
            fruit_label = pickle.load(f)
        
        # model prediction
        model = tf.keras.models.load_model('models/fruits-model.h5')

        prediction = model.predict([N,P,K,pH,EC,S,Cu,Fe,Mn,Zn,B])

        fruit = fruit_label[tf.argmax(prediction[0])]
        return {'fruit':fruit}
