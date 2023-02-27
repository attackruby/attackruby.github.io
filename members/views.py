from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Member,Memento


def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def main2(request):
    template = loader.get_template('main2.html')
    return HttpResponse(template.render())


def testing(request):
  mydata = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))


def search(request):
    query = request.GET.get('q')
    if query:
        results = Memento.objects.filter(title__icontains=query)
    else:
        results = None
    return render(request, 'search.html', {'results': results})

def handler404(request, exception):
    return render(request, '404.html', status=404)

def my_css_view(request):
    with open('static/css/style.css') as f:
        css = f.read()

    response = HttpResponse(css, content_type='text/css')
    return response
