from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {'insert_p2': 'This is from the Project Two index.html! And this is changing.'}
    return render(request, 'index.html', context = my_dict)

