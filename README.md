# AquaCheck

# Water Potability Prediction using Machine Learning
This project aims to develop a machine learning model to predict whether the water is potable or not. Potable water refers to water that is safe for human consumption. The model will take input parameters related to various water quality measures, and output a prediction of whether the water is potable or not.

# Dataset
The dataset used in this project is the Water Potability Dataset from Kaggle. The dataset contains 3276 records and 9 columns, including pH, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, and Potability.

# Methodology
The following steps were taken to develop the machine learning model:

Data Preprocessing: The dataset was cleaned by removing missing values and outliers.

Exploratory Data Analysis: The data was analyzed to understand the distribution of the variables and identify any patterns or correlations.

Feature Engineering: The features were selected based on their correlation with the target variable and their importance in the model.

Model Selection: Three different models were trained and compared based on their performance metrics, including Logistic Regression, Random Forest, and XGBoost.

Model Evaluation: The best model was evaluated using various metrics, including accuracy, precision, recall, F1 score, and ROC-AUC score.

# Results
After training and evaluating the three models, the XGBoost model was selected as the best model based on its performance metrics. The XGBoost model achieved an accuracy of 79%, precision of 76%, recall of 66%, F1 score of 70%, and ROC-AUC score of 81%.

# Conclusion
The developed machine learning model can predict whether the water is potable or not with reasonable accuracy. The model can be used by water treatment plants, governments, and individuals to ensure that the water they consume is safe for human consumption. However, further research is required to improve the model's performance and validate the results on different datasets.



