from django.shortcuts import render
from djqscsv import render_to_csv_response
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from . models import Datas , Doctor


def home(request):
    return render(request, 'home.html')


def predict(request):
    return render(request, 'predict.html')


def Database(request):
    return render(request, 'Database.html')


def result(request):

    heart_data = pd.read_csv(r'C:\Users\HP\heart_disease_data.csv')

    X = heart_data.drop(columns='target', axis=1)
    Y = heart_data['target']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

    model = LogisticRegression()
    model.fit(X_train, Y_train)

    age = float(request.GET['n1'])
    sex = float(request.GET['n2'])
    cp = float(request.GET['n3'])
    trestbps = float(request.GET['n4'])
    chol = float(request.GET['n5'])
    fbs = float(request.GET['n6'])
    restecg = float(request.GET['n7'])
    thalach = float(request.GET['n8'])
    exang = float(request.GET['n9'])
    oldpeak = float(request.GET['n10'])
    slope = float(request.GET['n11'])
    ca = float(request.GET['n12'])
    thal = float(request.GET['n13'])

    pred = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    result1 = ""
    if pred == 1:
        result1 ="Positive - Stay Strong"
        target = pred
    else:
        result1 = "Negative"
        target = 0



    Datas.objects.create(age=age, sex= sex, cp=cp, trestbps=trestbps, chol=chol, fbs=fbs, restecg=restecg, thalach=thalach, exang=exang, oldpeak=oldpeak, slope=slope, ca=ca, thal=thal, target=target)

    return render(request, 'results.html', {"result2" : result1})


def view_results(request):
    datas={"dataset": Datas.objects.all()}
    return render(request, "Database.html", datas)


def doctor(request):
    datas = {"dataset": Doctor.objects.all()}
    return render(request, "doctors.html", datas)