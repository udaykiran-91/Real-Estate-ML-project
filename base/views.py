from django.shortcuts import render,redirect
from django.http import HttpResponse
import pickle
import numpy as np
import json
# Create your views here.

def home(request):
    data = json.load(open('columns.json'))
    viva = data['data_columns']
    if request.method == 'POST':
        location=request.POST.get('location')
        sqft=request.POST.get('area')
        bath=request.POST.get('bath')
        bhk=request.POST.get('bhk')
        final = predict_price(location,sqft,bath,bhk)
        print(final)
        data = json.load(open('columns.json'))
        viva = data['data_columns']
        return render(request,'base/home.html',{'fin':final,'data_columns':viva})
    
    return render(request,'base/home.html',{'data_columns':viva})

def result(request):
    return render(request,'base/results.html')


def predict_price(location,sqft,bath,bhk):
    model = pickle.load(open('banglore_home_prices_model.pickle','rb'))
    data = json.load(open('columns.json'))
    loc_index = data['data_columns'].index(location)
    x = np.zeros(len(data['data_columns']))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index >= 0:
        x[loc_index]=1

    return model.predict([x])[0]

# data = json.load(open('columns.json'))
# print(data['data_columns'][0])
# print(data['data_columns'][0] == 'total_sqft')
# print(data['data_columns'].index('whitefield'))
# answer=predict_price('jp nagar',1000,3,2)
# print('answer:',answer)

# for topic in data['data_columns']:
#     print(topic)
    
    

