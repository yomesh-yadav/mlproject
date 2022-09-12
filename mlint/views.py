from cgitb import html
from http.client import HTTPResponse
from django.shortcuts import render
import pickle
from sklearn.ensemble import RandomForestClassifier
import numpy as np
# from mlint import normalize_data_func_new as normalizer

#from mymlproject.normalize_data_func_new import *

# Create your views here.
std_new=  [0.36687788854745235, 0.17536537331327948, 0.2624715571716956, 0.29794212924884544, 0.17398037724752122, 5.506662936623941, 0.15588823288991666, 30.198828816982807, 0.2581941394549108]
mean_new= [0.43057836023390855, 0.5563526539625419, 0.522128712431504, 0.149320558659524, 0.20136456203484093, -10.668686513453832, 0.09767980698454241, 118.16749488836182, 0.5253000727897276]

clf=pickle.load(open('clefmodel.pkl','rb'))

def normalize_data_func_new(l3):
#   print(len(mean_new))
    val=l3/mean_new
#   for i in range(len(l3)):
    return val;
#         l3[i]=(l3[i]-mean_new[i])/(std_new[i]);
#   return l3

def get_dum(n):
    l1=[0,0,0]
    l1[n-1]=1
    return l1

def year_bin_func(element):
    if element <= 1960 : # very old category
        return 0
    elif element > 1960 and element <= 1985: # old
        return 1
    elif element > 1985 and element <= 2010: # new
        return 2
    elif element > 2010: #recent
        return 3

def month_bin_func(element):
    if element == 1 or element == 2 or element == 12 : # winter
        return 0
    elif element > 2 and element < 6 : # spring
        return 1
    elif element >= 6 and element < 9 : # summer
        return 2
    elif element >= 9 and element< 12: #autumn
        return 3

# normalizer = pickle.load(open('normalize_data_func_new.pkl', 'rb'))
# model=pickle.load(open('clefmodel.pkl','rb'))
# month_binner=pickle.load(open('month_bin_func.pkl','rb'))
# year_binner=pickle.load(open('year_bin_func.pkl','rb'))

def home(request):
    
    return render(request,"index.html")

def predict(request):
    if request.method=="POST":
        l1=[]
        for i in request.POST:
            val=str(i)
            # print(request.POST[val])
            l1.append(request.POST[val])
        # print(l1[1:12]) 
        new_list=[]

        for i in range(1,4):

        # return val;
            if not i ==0:
                # print((i))
                new_list.append((float(l1[i])-mean_new[i-1])/(std_new[i-1]));
        new_list.append(int(l1[4]))
        for i in range(5,8):
    
        # return val;
            if not i ==0:
                # print((i))
                new_list.append((float(l1[i])-mean_new[i-2])/(std_new[i-2]));
        # print(l/2)
        new_list.append(int(l1[8]))
        for i in range(9,12):
    
        # return val;
            if not i ==0:
                # print((i))
                new_list.append((float(l1[i])-mean_new[i-3])/(std_new[i-3]));
        # print(new_list)
        l1[12]=year_bin_func(int(l1[12]))
        l1[13]=month_bin_func((int(l1[13])))
        # print(((l1[12])))
        new_list=new_list+(get_dum(year_bin_func(int(l1[12]))))  
        print((get_dum(year_bin_func(int(l1[12])))) )
        print(int(l1[12]))
        new_list=new_list+(get_dum(month_bin_func((int(l1[13]))))) 
        print(new_list)
        predicted_val = clf.predict(np.array(new_list).reshape(1,-1))
        print(predicted_val)
        data={
            "pred_value":predicted_val,
        }
        return render(request,'index.html',data)
              

