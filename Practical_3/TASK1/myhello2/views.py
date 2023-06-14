from django.shortcuts import render
def hello(request):
    return render(request, 'savedhtmlpage.html')

# Create your views here.
