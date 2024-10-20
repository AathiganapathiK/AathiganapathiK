# homepage/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'homepage/home.html')

def signup_view(request):
    return render(request, 'homepage/signup.html')  # Correct template path

def create_account_view(request):
    return render(request, 'homepage/create_account.html')  # Correct template path

def mainpage_view(request):
    return render(request, 'homepage/main_page.html')

def userdetails_view(request):
    return render(request, 'homepage/user_details.html')

def apple_view(request):
    return render(request, 'homepage/apple.html')

def signup(request):
    if request.method == "POST":
        # Handle the form submission and account creation logic here
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password == confirm_password:
            # Example of account creation logic (you'd likely use Django's User model)
            # user = User.objects.create_user(username=name, email=email, password=password)
            # user.save()

            # Success message to be shown after account creation
            return render(request, 'signup.html', {'message': 'Account created successfully! Please log in.'})
        else:
            return render(request, 'create_account.html', {'error': 'Passwords do not match'})

    return render(request, 'signup.html')