# Stroke-Prediction-Analysis
A web based application to predict whether a patient is likely to get stroke based on the input parameters like gender, age, various diseases, and smoking status. Each row in the data provides relevant information about the patient.
A perfect project to learn Data Analytics and apply Machine Learning algorithms (Logistic Regression, Random Forest, Decision Tree, KNN and SVM) to predict stroke.

**Dataset Link**: https://www.kaggle.com/fedesoriano/stroke-prediction-dataset

### Stages:
#### 1. Data Cleaning: - 
Data cleaning is the process of fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset. When combining multiple data sources, there are many opportunities for data to be
Dataset
Data Cleaning
Test Data
Train Data
Choose Model
Algorithm
Input
Output
16
duplicated or mis
-labelled. If data is incorrect, outcomes and algorithms are unreliable, even though they may look correct.
#### 2. Data analysis: - 
It involves the exploration of data. We explore the data and analyze it thoroughly in order to identify some patterns or new outcomes from the data set. In this stage, we discover useful information and conclude by identifying some patterns or trends. • Label Encoding: -Label Encoding refers to converting the labels into a numeric form so as to convert them into the machine-readable form. Machine learning algorithms can then decide in a better way how those labels must be operated. It is an important pre-processing step for the structured dataset in supervised learning.
#### 3. Sampling: -
This technique is mainly used to select, manipulate and analyse a subset of data points in order to identify patterns and trends in the dataset. The traditional method of data sampling is to split the data into training and test sets. The larger amount of data is directed to the training set to build the required model and the rest of the data are implied as the test set in order to verify the outcome of the model. It helps in building and executing the outcome of a model in an efficient and quicker way.
#### 4. Normalization: -
Data normalization is the organization of data to appear similar across all records and fields. It increases the cohesion of entry types leading to cleansing, lead generation, segmentation, and higher quality data. • Modelling: - In order to build a robust model, a data scientist should just not stop by implying one or two algorithms, rather it should run as many algorithms that are possible for the model. Then the outcome of the overall results of the models should be chosen in order to get efficient outcomes in an organisation.
#### 5. Building Model: - 
Different types of machine learning algorithms as well as techniques have been developed which can easily identify complex patterns in the data which will be a very tedious task to be done by a human.
#### 6. Model Deployment: – 
After a model is developed and gives better results on the holdout or the real-world dataset then we deploy it and monitor its performance. This is the main part where we use our learning from the data to be applied in real-world applications and use cases.

### Setup

#### Step 1: Install Python

Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/). It's recommended to use Python 3.x (e.g., Python 3.8 or Python 3.9).


#### Step 2: Create and Activate Virtual Environment

1. Navigate to your project directory in the terminal:
   ```
   cd path/to/your/project
   ```

2. Create a new virtual environment (replace `myenv` with your preferred name):
   ```
   virtualenv myenv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     myenv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source myenv/bin/activate
     ```

#### Step 3: Install requirement.txt

1. It will install all the packages that are required for this project:
   ```
   pip install -r requirements.txt
   ```

#### Step 4: Apply Migration 
1. Make initial migrations for the Django project:
   ```
   python manage.py makemigrations
   ```

2. Apply migrations to set up your database:
   ```
   python manage.py migrate
   ```

#### Step 5: Change model location 
1. The machine learning model (scaler.pkl and dt.sav) location inside django views.py need to be change according to your file system.
   
#### Step 6: Run Django Development Server

1. Start the Django development server:
   ```
   python manage.py runserver
   ```

2. Open your web browser and go to `http://127.0.0.1:8000/` or `http://localhost:8000/` to see your Django project running locally.

### Additional Notes

- **Project Structure**: Ensure your project files are organized appropriately for a Django project. You may need to create apps (`python manage.py startapp appname`) within your project for specific functionalities like the stroke prediction analysis.
  
- **Database Configuration**: Django uses SQLite by default. Modify `settings.py` if you want to use a different database like PostgreSQL or MySQL.

