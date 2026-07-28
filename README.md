# Cardiovascular Disease Prediction🧡

## Overview

This project uses Machine Learning to predict whether an individual is at risk of cardiovascular disease based on demographic information, lifestyle habits, and medical history. The project includes extensive Exploratory Data Analysis (EDA), data preprocessing, model training, evaluation, and model serialization for deployment in a Streamlit web application.

---

## Features

* Comprehensive data cleaning and preprocessing
* Univariate and bivariate exploratory data analysis
* Feature encoding and scaling
* Multiple machine learning models for comparison
* Model evaluation and performance comparison
* Saved trained model and preprocessing objects for deployment
* Streamlit-ready prediction pipeline

---

## Dataset

The dataset contains **308,854** records with **19 features**, including:

### Demographic Information

* Sex
* Age Category
* Height (cm)
* Weight (kg)
* BMI

### Lifestyle Factors

* Exercise
* Smoking History
* Alcohol Consumption
* Fruit Consumption
* Green Vegetables Consumption
* Fried Potato Consumption

### Medical History

* General Health
* Checkup
* Skin Cancer
* Other Cancer
* Depression
* Diabetes
* Arthritis

### Target Variable

* Heart Disease

---

## Exploratory Data Analysis

The notebook includes detailed visualizations and insights such as:

* Distribution of categorical features
* Distribution of numerical features
* Health condition analysis
* Lifestyle habit analysis
* Age distribution
* BMI and weight analysis
* Relationship between each feature and heart disease
* Scatter plots and count plots for feature interactions

Key observations include:

* Heart disease is more common among older individuals.
* Lack of exercise increases cardiovascular risk.
* Diabetes and smoking show strong association with heart disease.
* Poor self-rated health is associated with higher disease prevalence.
* Males have a slightly higher prevalence of heart disease than females.

---

## Data Preprocessing

The following preprocessing steps were performed:

* Corrected inconsistent categorical values (e.g., `"Poo"` → `"Poor"`).
* Checked and handled missing values.
* Verified duplicate records.
* Applied **Label Encoding** to binary categorical features.
* Applied **Ordinal Encoding** to ordered categorical features.
* Applied **StandardScaler** to numerical features.

---

## Machine Learning Models

The following models were trained and compared:

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Decision Tree Classifier
* Random Forest Classifier

After evaluation, the best-performing model was saved for deployment.

---

## Saved Files

The notebook exports the following files using Joblib:

* `cardiovascular_model.pkl`
* `label_encoder.pkl`
* `ordinal_encoder.pkl`
* `scaler.pkl`

These files are used by the Streamlit application to preprocess user input and generate predictions.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Streamlit

---

## Project Structure

```text
├── CVD_Prediction.ipynb
├── app.py
├── CVD_cleaned.csv
├── cardiovascular_model.pkl
├── label_encoder.pkl
├── ordinal_encoder.pkl
├── scaler.pkl
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/CVD.git
cd CVD
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## Workflow

1. Load dataset
2. Perform data cleaning
3. Conduct exploratory data analysis
4. Encode categorical variables
5. Scale numerical features
6. Train machine learning models
7. Evaluate model performance
8. Save the best model
9. Deploy using Streamlit

---

## Future Improvements

* Hyperparameter tuning
* Cross-validation
* Feature selection
* Model explainability using SHAP or LIME
* Deep learning-based prediction
* Cloud deployment

---

## Author

**Madhu Shrivastava**

GitHub: https://github.com/MadhuShrivastava

---

## License

This project is intended for educational and research purposes.
