# Blindness Detection

## Introduction
Imagine being able to detect blindness before it happened! Diabetic retinopathy is a condition that affects the blood vessels in the light-sensitive tissues called the retina. People with all types of diabetes are at the risk of this condition. Millions of people suffer from diabetic retinopathy, the leading cause of blindness among working aged adults. Our goal is to build a machine learning model to speed up disease detection.  More information can be found <a href="https://www.kaggle.com/c/aptos2019-blindness-detection" target="_blank">here</a>

---



## Methodology

We would be working with 3 neural network architectures in order to predict blindness.

- AlexNet
- VggNet
- Deep FishNet



## Web application

We are building a web application which, given an X-ray image, would predict if the patient is in risk of diabetic retinopathy.

![Landing page](https://github.com/aswani15/Diabetic-Retinopathy-Detection/tree/master/data/landing_page.png)



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
