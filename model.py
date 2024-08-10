import tensorflow as tf
import pickle
import numpy as np


def model_predict(form, type):
    form = form.to_dict()
    if type == "nutrition":

        soilColor = form["soilColor"]
        nitrogen = int(form["nitrogen"])
        phosphorous = int(form["phosphorous"])
        potassium = int(form["potassium"])
        pH = float(form["pH"])
        rainfall = float(form["rainfall"])
        temperature = float(form["temperature"])

        # model prediction
        model = tf.keras.models.load_model("models/crop-model.h5")

        with open("models/labels/crop_txt", "rb") as f:
            crop_label = pickle.load(f)

        with open("models/fertilizers-model", "rb") as f:
            fertilizer_label = pickle.load(f)

        with open("models/labels/soil_color_txt", "rb") as f:
            soil_color_label = pickle.load(f)

        for key, value in soil_color_label.items():
            if value == soilColor:
                soilColor = key
                break

        prediction = model.predict(
            np.array(
                [
                    [
                        soilColor,
                        nitrogen,
                        phosphorous,
                        potassium,
                        pH,
                        rainfall,
                        temperature,
                    ]
                ]
            )
        )
        print(crop_label)

        crop = crop_label[int(tf.argmax(prediction[0]))]
        fertilizer = fertilizer_label[crop]
        return {"crop": crop, "fertilizer": fertilizer}

    if type == "weather":
        N = int(form["N"])
        P = int(form["P"])
        K = int(form["K"])
        temperature = float(form["temp"])
        humidity = float(form["humidity"])
        ph = float(form["pH"])
        rainfall = float(form["rainfall"])

        # model prediction
        with open("models/labels/crops_txt_shubh", "rb") as f:
            weather_crop_label = pickle.load(f)

        # model prediction
        model = tf.keras.models.load_model("models/crop-nutrients-model.h5")

        prediction = model.predict(
            np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        )

        weather_crop = weather_crop_label[int(tf.argmax(prediction[0]))]
        return {"weather_crop": weather_crop}

    if type == "fruits":
        N = int(form["N"])
        P = int(form["P"])
        K = int(form["K"])
        pH = float(form["pH"])
        EC = float(form["EC"])
        S = float(form["S"])
        Cu = float(form["Cu"])
        Fe = float(form["Fe"])
        Mn = float(form["Mn"])
        B = float(form["B"])
        Zn = float(form["Zn"])
        # model prediction

        with open("models/labels/fruits_txt", "rb") as f:
            fruit_label = pickle.load(f)

        # model prediction
        model = tf.keras.models.load_model("models/fruits_model.h5")

        prediction = model.predict(np.array([[N, P, K, pH, EC, S, Cu, Fe, Mn, Zn, B]]))

        fruit = fruit_label[int(tf.argmax(prediction[0]))]
        return {"fruit": fruit}
