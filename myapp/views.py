from django import http
from django.shortcuts import render
from django.http import HttpResponse


def postinput(request):

    return render(request,'postinput.html')


def getinput(request):

    return render(request,'getinput.html') 


def add(request):
    if request.method == "GET": 
        if request.GET['add'] == "add": 
            try:   
                a = int(request.GET['first'])
                b = int(request.GET['second'])
                c = a+b 
                data = {'res' : c}
                return render(request,'res.html', data )
            except: 
                return HttpResponse("There is some error")
        elif request.GET['add'] == "sub": 
            try: 
                a = int(request.GET['first'])
                b = int(request.GET['second'])
                c = a - b  
                data = {'res' : c}
                return render(request, 'res.html',  data)

            except: 
                return HttpResponse("There is some error")

        elif request.GET['add'] == "mul":  
            try: 
                a = int(request.GET['first'])
                b = int(request.GET['second'])
                c = a*b  
                data = {'res' : c}
                return render(request, 'res.html',  data) 

            except: 
                return HttpResponse("There is some error")


        elif request.GET['add'] == "div":  
            try: 
                a = int(request.GET['first'])
                b = int(request.GET['second'])
                c = a/b  
                data = {'res' : c}
                return render(request, 'res.html',  data)
            except: 
                return HttpResponse("zero division error")
    else: 
        if request.GET['add'] == "add":   
            a = int(request.GET['first'])
            b = int(request.GET['second'])
            c = a+b 
            data = {'res' : c}
            return render(request,'res.html', data )
        elif request.GET['add'] == "sub":  
            a = int(request.GET['first'])
            b = int(request.GET['second'])
            c = a - b  
            data = {'res' : c}
            return render(request, 'res.html',  data)

        elif request.GET['add'] == "mul":  
            a = int(request.GET['first'])
            b = int(request.GET['second'])
            c = a*b  
            data = {'res' : c}
            return render(request, 'res.html',  data) 


        elif request.GET['add'] == "div":  
            a = int(request.GET['first'])
            b = int(request.GET['second'])
            c = a/b  
            data = {'res' : c}
            return render(request, 'res.html',  data)  