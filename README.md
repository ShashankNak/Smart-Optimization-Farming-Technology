# S.O.F.T
## SMART OPITMIZED FARMING TECHNOLOGY

<video width="640" height="400" controls>
  <source src="!(https://github.com/user-attachments/assets/2d2b2e82-573a-400d-a956-2ce9febff9bb)" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Overview

This repository contains a Flask-based web application for Smart Farming optimization Analysis. The application uses nutritional information from the farm soil lands and create a yearly plan for growing different crops without depleting the soils nutrition in that period optimally. Also, during that period, it allows to detect diseases in the plants using image localization and classification.

## Features

- **Crops Prediction based on Nutritional Values and Soil Types**: Predicts crops and fertilizers to use to grow in a farm based on soil type and its nutritional value.
- **Fruits and Vegetables Prediction based on Nutritional Values**: Predicts Fruits and Vegetables to grow in a farm based on soil's nutritional value.
- **Crops Prediction based on Nutritional Values and Weather Condition**: Predicts crops to grow in a farm based on soil type and its nutritional value.
- **Optimize the system of Farming**: Display Yearly Plans to optimize the yield of the Farmer crops while maintaining the soil's nutritional value.
- **Plants Leaves Disease Prediction During Farming Period**: Detect and predict the plants that has diseases in its leaves such that it can be prevented using Computer Vision and Classification

## Installation

### Prerequisites

Ensure you have [conda](https://docs.conda.io/en/latest/miniconda.html) installed.

### Step-by-Step Guide

1. **Clone the repository**

    ```sh
    git clone https://github.com/ShashankNak/Smart-Optimization-Farming-Technology
    cd Smart-Optimization-Farming-Technology
    ```

2. **Create a new environment with conda**

    ```sh
    conda create --name smart-farming python=3.11.9
    ```

3. **Activate the environment**

    ```sh
    conda activate smart-farming
    ```

4. **Install the required packages**

    ```sh
    pip install -r requirements.txt
    ```

5. **Run the application**

    ```sh
    python3 app.py
    ```

## Usage

1. **Start the Flask application**

    Running the command `python3 app.py` will start the Flask application. Open your web browser and navigate to `http://localhost:5000` to access the web interface.

2. **Navigate through the website**

    - **Model Information Page**: The homepage displays information about the models being used.
    - **Get Started**: Click the "Get Started" button to proceed to predict the crops.
        - **Crop Based on Nutrition**: Fill the nutritional values and soil type and click the "Predict" button to get the results of crops and fertilizers. 
        - **Fruits and Vegetables**: Fill the nutritional values and click the "Predict" button to get the results Fruits and vegetables to grow.
        - **Crop Based on Weather Conditions and Nutrients**:  Fill the nutritional values and weather Conditions and click the "Predict" button to get the results Fruits and vegetables to grow.
    **Plant Disease Detection** : Click the "Detection" to proceed to detection page.
        - **Upload File**: Upload an image or a video to detect the defective plant leaves
    **Model Insights**: Models and its metrics of accuracy, loss and precisions.

3. **Viewing Results**

    - **Prediction**: After filling the nutritional values, the application will predict crop or fruits or fertilizers and yearly plan
    - **Detection**: The application will detect the plant leaves that has some disease.
    - **Statistics**: Model and its performance metrics like accuracy, loss and precisions graphs.

## Dataset Overview

- We collected datasets of soils, farms, crops and its nutritional value through internet.(Mainly Public Datasets)
- Additionally, we used a public dataset containing 10,000 images of disease Leaves that has 38 diseases.
- These datasets were combined to train several models capable of predicting the crops and classify the diesases Leaves.
- For Optimization, we developed a system that automatically predict the next crop to grow after one crop that changes the soil nutritional value until the year comes to an end.

## Collaboration

This project was developed as part of the DAIICT Hackathon by a team of Four members: Shashank Nakka, Shubham Joshi, Yesha Amin, Yuti Dave.

## Note

The model file is not included in this repository due to its large size. Please contact the project maintainers for access to the model file or instructions on how to obtain it.

## Contact
For issues or questions, please open an issue in this repository.
