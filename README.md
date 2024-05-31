# Stroke Risk Prediction Using Different Machine Learning Models.
## Aim:
Since advancement in artificial intelligence (AI) and machine learning (ML) have become critical for early disease prediction in healthcare. This project aims to develop and evaluate various machine learning (ML) models, including Logistic Regression, Support Vector Machine (SVM), Random Forest, KNN, Naïve Bayes, XGBoost, AdaBoost, Gradient Boost, and Decision Tree, to create an accurate framework for predicting stroke occurrence over time.
## Methodology:
### Data Preprocessing:
Data preprocessing is an essential phase in the success of any project, as it guarantees that the dataset is of sufficient quality for subsequent analysis. This process encompasses several key steps, including addressing missing or null values, managing duplicated entries, handling outliers, and performing data scaling and normalization.
### Exploratory Data Analysis (EDA):
Exploratory Data Analysis (EDA) is a vital step for machine learning algorithms, as it allows us to understand the dataset, its features, and the distribution of values. Typically, this step involves creating various plots to explore the data.
### Feature Engineering:
Label encoding and feature scaling were performed to convert categorical values to numerical ones and scale the values to a comparable range.
### Model Development and Evaluation:
Nine machine learning models were then trained using the training set: Logistic Regression, Support Vector Machine, Random Forest, KNN, Naïve Bayes, XGBoost, AdaBoost, Gradient Boost, and Decision Tree. The accuracy scores and other evalutaion metrics like, precision, recall and f1-score, of these models were calculated, and the model with the highest performance was chosen.
### Hyperparameter Tuning:
A dictionary of hyperparameters (max_depth, min_samples_leaf, min_samples_split, and criterion) was created, and the Decision Tree model was fine-tuned using a grid search cross-validation object fitted to the training set to identify the best estimator and determine its accuracy score. Subsequently, all models were retrained using the most important features, and their accuracies were calculated.
### Model Deployment:
Performed to ensure that the Python classifier model is readily available for use.
## Results:
The Decision Tree model performed best with an accuracy of 97.205% after re-training, and was used for model deployment.
## Limitations:
1. Dataset imbalance.
2. Limited number of features (12). 
3. Considerable number of null values and outliers.
4. Higher model susceptibility to overfitting.
## Recommendations:
Employing a variety of models and incorporating regularization techniques that would help avoid overfitting.
## Authors:
Sondos Ameen Awad.



