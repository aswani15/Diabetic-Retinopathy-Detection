# Blindness Detection

## Introduction
Imagine being able to detect blindness before it happened! Diabetic retinopathy is a condition that affects the blood vessels in the light-sensitive tissues called the retina. People with all types of diabetes are at the risk of this condition. Millions of people suffer from diabetic retinopathy, the leading cause of blindness among working aged adults. Our goal is to build a machine learning model to speed up disease detection.  More information can be found <a href="https://www.kaggle.com/c/aptos2019-blindness-detection" target="_blank">here</a>

---



## Methodology

In this project I would be working with 3 neural network architectures in order to predict blindness.

- AlexNet
- VggNet
- Deep FishNet



## Web application

Iam in process of building a web application which, given an X-ray image, would predict if the patient is in risk of diabetic retinopathy.

<img src="https://github.com/aswani15/Diabetic-Retinopathy-Detection/blob/master/data/DB1.png?raw=true" />

Introduction:
Imagine being able to detect blindness before it happened. Millions of people suffer from this condition, the leading cause 
of blindness among working adults. I want to design a AI Deep learning model that would help us detect the complications at 
an early stage and prevent permanent damage to the eyes.

Model Building:

I have tried 3 different deep learning architectures and used the best model to predict blindness.
Deep Learning models:

1.	AlexNet
2.	VggNet11
3.	Deep FishNet
An overview of our architecture can be given as follows:

<img src="https://github.com/aswani15/Diabetic-Retinopathy-Detection/blob/master/data/DB2.png?raw=true" />

Results:

I have used F1- Score as scoring metric. The prediction model result can be summarized using the following confusion matrix:

<img src="https://github.com/aswani15/Diabetic-Retinopathy-Detection/blob/master/data/DB3.png?raw=true" />


## Initialization

The app will start using the following commands:

```
cd src
python start_app.py
```

Additional options

```
cd src
python start_app.py --client-port <client-port> --server-port <server-port>
```
