from django.shortcuts import render

def home(request):
    return render(request, "dashboard.html")  # If in templates/analyzer/
