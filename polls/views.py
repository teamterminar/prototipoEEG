import csv
import json

import joblib
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse

from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import tensorflow as tf
from tensorflow import keras
import numpy as np


@csrf_exempt
def  index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    print("does not exist")

    #    print(request.body);
    #   data = {
    #      "name": request.POST.get("producto"),
    #     "age": 20,
    #    "hobbies": ["Coding", "Art", "Gaming", "Cricket", "Piano"]
    # }
    store_details = []
    json_array = json.loads(request.body)

    print(json_array)
    store_details.append(json_array['HIGH_ALPHA'])
    store_details.append(json_array['LOW_GAMMA'])
    store_details.append(json_array['LOW_ALPHA'])
    store_details.append(json_array['DELTA'])
    store_details.append(json_array['MID_GAMMA'])
    store_details.append(json_array['HIGH_BETA'])
    store_details.append(json_array['LOW_BETA'])
    store_details.append(json_array['THETA'])

    with open('wavesdata.csv', 'a+', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(store_details)

    with open('tipos.csv', 'a+', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([request.GET.get("tipo")])

    return JsonResponse(json.loads(request.body))
    # return Response(data={'error':"not-found",'status':"404"},status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def entrena(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    print("does not entrena")
    data = []
    with open('wavesdata.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:  # each row is a list
            data.append(row)

    print(data)

    result = []
    with open('tipos.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:  # each row is a list
            result.append(row)

    print(result)

    def enconder(digit):
        if digit == 0:
            return [0]
        else:
            return [1]

    train_labels_enc = np.array(list(map(enconder, result)))
    print(train_labels_enc)
    test = [16772230, 68543, 27557, 1514095, 78696, 146423, 72003, 394675]
    testRe = [0]
    test_labels_enc = np.array(list(map(enconder, testRe)))

    from sklearn.neural_network import MLPClassifier

    # Tres capas ocultas de 20-150-20 neuronas respectivamente
    clf = MLPClassifier(hidden_layer_sizes=(20,2))

    clf.fit(data, result)
    joblib.dump(clf, 'my_model.pkl', compress=9)
    #    print(request.body);
    data = {
          "score": clf.score(data, result),
         "age": 20,
        "hobbies": ["Coding", "Art", "Gaming", "Cricket", "Piano"]
    }



    return JsonResponse(data)
    # return Response(data={'error':"not-found",'status':"404"},status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def clasifica(request):
    clf = joblib.load('my_model.pkl')

    store_details = []
    json_array = json.loads(request.body)

    print(json_array)
    store_details.append(json_array['HIGH_ALPHA'])
    store_details.append(json_array['LOW_GAMMA'])
    store_details.append(json_array['LOW_ALPHA'])
    store_details.append(json_array['DELTA'])
    store_details.append(json_array['MID_GAMMA'])
    store_details.append(json_array['HIGH_BETA'])
    store_details.append(json_array['LOW_BETA'])
    store_details.append(json_array['THETA'])

    predict_label = clf.predict([store_details])[0]


    data = {
        "prediccion": str(predict_label),
    }
    return JsonResponse(data)
