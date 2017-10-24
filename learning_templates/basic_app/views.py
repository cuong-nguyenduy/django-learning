from django.shortcuts import render


# Create your views here.
def index(request):
    context_dict = {
        'text': 'Hello, world',
        'number': 123,
    }
    return render(request, 'basic_app/index.html', context=context_dict)


def other(request):
    return render(request, 'basic_app/other.html')


def relative_url_templates(request):
    return render(request, 'basic_app/relative_url_templates.html')
