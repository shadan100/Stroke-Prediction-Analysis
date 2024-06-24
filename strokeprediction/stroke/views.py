from django.shortcuts import render

# Create your views here.
import pickle
from django.shortcuts import render
import joblib
import os 
import numpy as np

# def index(request):
#     return render(request, "stroke/stroke.html")

def form(request):
    if request.method == 'GET':
        return render(request, "stroke/stroke.html")
    else:
        gender = int(request.POST['gender'])
        age = int(request.POST['age'])
        hypertension = int(request.POST['hypertension'])
        heart_disease = int(request.POST['heart_disease'])
        ever_married = int(request.POST['ever_married'])
        work_type = int(request.POST['work_type'])
        residence = int(request.POST['residence'])
        avg_glucose = float(request.POST['glucose'])
        bmi = float(request.POST['bmi'])
        smoking = int(request.POST['smoking'])

        x = np.array([gender,age,hypertension,heart_disease,ever_married,work_type,residence,avg_glucose,bmi,smoking]).reshape(1,-1)
        scaler_path = os.path.join('E:/MCA/MP2/Stroke Analysis/strokeprediction/scaler.pkl')
        scaler = None
        with open(scaler_path, 'rb') as scaler_file:
            scaler = pickle.load(scaler_file)
        x = scaler.transform(x)

        model_path = os.path.join('E:/MCA/MP2/Stroke Analysis/strokeprediction/dt.sav')     
        dt = joblib.load(model_path)
        Y_pred = dt.predict(x)

        # if their is no stroke
        if Y_pred == 0:
            return render(request,"stroke/stroke.html",{"message":"No Stroke Risk"})
        else:
            return render(request, "stroke/stroke.html",{"message": "Stroke Risk"})
        # return render(request, "stroke/stroke.html",{"predict":Y_pred})