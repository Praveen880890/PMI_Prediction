# PMI Prediction

This Python script is a Streamlit web application designed for predicting Postmortem Interval (PMI) using blood biomarker data. It utilizes a Logistic Regression model to make predictions based on input features such as LDH, AST, triglycerides, and pH level.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [Application Features](#application-features)
- [Adding Data](#adding-data)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The "PMI Prediction" application is a tool for estimating the postmortem interval of a deceased person by analyzing blood biomarker data. It offers a user-friendly interface for entering biomarker values and a patient's name and then displays the predicted PMI.

## Requirements

Before running the application, make sure you have the following dependencies installed:

- Python 3.x
- Streamlit
- Pandas
- Scikit-learn (sklearn)

You can install these dependencies using `pip`:

```bash
pip install streamlit pandas scikit-learn
```

## Usage

To run the application, execute the following command in your terminal:

```bash
streamlit run app.py
```

## Application Features

The "PMI Prediction" application provides the following features:

- **Input Fields**: Users can input the following data for PMI prediction:
  - LDH (Lactate Dehydrogenase) level
  - AST (Aspartate Aminotransferase) level
  - Triglycerides level
  - pH Level
  - Patient's name (optional)

- **Prediction**: Clicking the "Predict" button will display the estimated PMI based on the input data using a Logistic Regression model.

- **Add Data**: Users can choose to add the input data along with the predicted PMI to the dataset for future reference.

## Adding Data

If you wish to add the input data and predicted PMI to the dataset, follow these steps:

1. Enter the input data and click the "Predict" button.

2. The application will display the predicted PMI and a summary of the input data.

3. Click the "ADD" button to add the data to the dataset.
