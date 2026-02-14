from django.shortcuts import render

# Create your views here.
def show_auth_page(request):
    return render(request, 'users/auth.html')