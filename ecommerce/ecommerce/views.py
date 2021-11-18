from django.shortcuts import render 
#funcion render sirve para mostrar mi vista
def home(reguest):
    return render(reguest, 'home.html')