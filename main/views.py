from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import UserRegisterForm
from .serializer import *

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Cars
from .serializer import CarsSerializers


# @login_required(login_url='login')
def home(request):
    return render(request, 'main/home.html')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'main/login.html')
#
#
def logoutUser(request):
    logout(request)
    return redirect('login')


def registerUser(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return redirect('home')
    return render(request, 'main/register.html', {
        'form': form
    })


@api_view(['GET'])
def carList(request):
    car = Cars.objects.all()
    serializer = CarsSerializers(car, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def createCar(request):
    serializer = CarsSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteCar(request, pk):
    car = Cars.objects.get(id=pk)
    car.delete()
    return Response('car removed')


