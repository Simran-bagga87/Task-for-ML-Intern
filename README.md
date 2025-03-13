# Task-for-ML-Intern
Task Assignment for imageAI to predict the DON concentration 

## Objective 
 Our objextive is to process hyperspectral imaging data and develop a machine learning model to predict mycotoxin levels (e.g., DON concentration) in corn samples.The data contain 500 rows and 450 features including label whih is vomitoxin_ppb. The Label is continuous data so we perform regression models. Other features include spectral Reflectance and HMI id for corn identification.

 ### Install dependencies
 #### Instructions
 1. create virtual environment
    >> python -m venv venv
 2. change directory move to Scripts
    >> venv/Scripts
 3. acticate the virtual environment using command
     >> Activate.bat
 4. install dependencies
    >> pip install -r requirement.txt

### Run streamlit Application
    command >> streamlit run ML_task_app.py

### Conclusion
The project include processing of the features, outlier detection and removal , PCA for reducing dimentionality ,scaling data and regression models such as RandomForestRegression, XGBoost, CNN also for hyper parameter tuning the Gridsearch is used.

    

