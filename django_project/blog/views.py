from django.shortcuts import render
from django.http import HttpResponse


posts=[
    {
        'author':'vanshika',
        'title':'Blog post 1',
        'content':'First Blog content',
        'date_posted':'30th March, 2024'
    },
      {
        'author':'anshika',
        'title':'Blog post 2',
        'content':'Second Blog content',
        'date_posted':'24th August, 2024'
    }
]

def home(request):
    context={
        'posts':posts
    }
    
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About Page'})
