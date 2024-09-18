from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from .models import Car

def home (request):
    features = Car.objects.all()
    return render(request, 'home.html', {'features': features})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username = username , password = password)
        if user is not None :
            auth.login(request,user)
            messages.info(request,'Login Successfully !!')
            return redirect('home')
        else:
            messages.info(request,'*Invalid Credentials')
            return render(request,'login.html')
    else:          
        return render(request,'login.html')
    
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email  = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('repeatpassword')

        if not username or not email or not password or not password2:
            messages.info(request, "*All fields are required")
            return redirect('register')

        if password != password2:
            messages.info(request, "*Passwords don't match")
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.info(request,"*Email already exists")
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.info(request,"*Username already exists")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')
    else:
        return render(request,'register.html')
 
def logout(request):
    auth_logout(request)
    messages.info(request,"Logout successfully !!! ")
    return redirect('login')
   


def add_car(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        model = request.POST.get('model')
        price = request.POST.get('price')
        car_image = request.FILES.get('car_image')

      
        if not name or not model or not price or not car_image:
            messages.error(request, "All fields are required!")
            return render(request, 'add_car.html')
        
        data = Car(name=name, model=model, price=price, car_image=car_image)
        data.save()  
        return redirect('home')

    return render(request, 'add_car.html')

def delete_car(request, id):
    if request.method == 'POST':
        car_to_delete = Car.objects.get(id=id)
        car_to_delete.delete()
        return redirect('home')


def edit(request, id):
    car = get_object_or_404(Car, id=id)  

    if request.method == 'POST':  
        name = request.POST.get('name')
        model = request.POST.get('model')
        price = request.POST.get('price')

        # Handle file upload
        if 'car_image' in request.FILES and request.FILES['car_image']:
            car.car_image = request.FILES['car_image']
        
        if not name or not model or not price:
            messages.error(request, "All fields are required!")
            return render(request, 'edit.html', {'car': car})
        
        car.name = name
        car.model = model
        car.price = price
        car.save() 
        return redirect('home') 
    
    return render(request, 'edit.html', {'car': car})
