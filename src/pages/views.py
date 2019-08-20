from django.shortcuts import render
# from django.http import HttpResponse


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World!</h1>")
    return render(request, 'home.html', {})


def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})

def about_view(request, *args, **kwargs):
    my_context = {
        'title': "this is about us",
        'my_number': 123,
        'my_list': [123, 456, 678, "abc"]
    }
    return render(request, 'about.html', my_context)