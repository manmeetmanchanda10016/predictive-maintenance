# Predictive Maintenance using Machine Learning

A machine learning project that predicts potential machine failures using sensor data. It includes model training, evaluation, and an interactive Streamlit application.

## Features
- Machine failure prediction
- Comparison of five machine learning algorithms
- Feature scaling and one-hot encoding
- Model tuning using GridSearchCV
- Interactive Streamlit application

## Dataset
AI4I 2020 Predictive Maintenance Dataset.

Features used:
- Machine Type
- Air Temperature
- Process Temperature
- Rotational Speed
- Torque
- Tool Wear

## Machine Learning Models
- Logistic Regression
- Decision Tree
- Gradient Boosting
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)

## Best Model: Decision Tree
- Accuracy: 98.55%
- Precision: 80.00%
- Recall: 76.47%
- F1-score: 78.20%

The model detected 52 out of 68 machine failures in the test set.

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

## Run the Project Locally

Clone the repository:

    git clone https://github.com/manmeetmanchanda10016/predictive-maintenance.git
    cd predictive-maintenance

Install the dependencies:

    pip install -r requirements.txt

Run the Streamlit application:

    streamlit run app.py

## Limitations
The dataset is imbalanced because machine failures are rare. Predictions may not always be correct and should not be used as the sole basis for real-world safety decisions.


<img width="1916" height="1017" alt="image" src="https://github.com/user-attachments/assets/f9adf72c-1928-4740-ab6f-6beb0e355838" />
<img width="1917" height="1016" alt="image" src="https://github.com/user-attachments/assets/f6c713be-35fa-43ea-9452-8b3609b8894c" />
<img width="1917" height="1032" alt="image" src="https://github.com/user-attachments/assets/cce66cc5-b308-47b0-b836-9b0eec50b2a1" />
<img width="1917" height="1022" alt="image" src="https://github.com/user-attachments/assets/23d9aee0-8cdb-4cda-921f-1bd93a197d09" />





## Author
CSE Student | Machine Learning Enthusiast
