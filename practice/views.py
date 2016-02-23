from django.shortcuts import render

# Create your views here.
from practice.forms import MessageForm
from practice.models import Message


def index(request):
    form = MessageForm()
    return render(request, 'index.html', locals())


def forms(request):
    print('mmmmmmmmmmmmmmmmmmmmmmmmmmm')
    if request.method == 'POST':
        print('=========================')
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            # print(dir(form))
            # print('---------- name: ', form.name)
            # print('---------- title: ', form.title)
            # print('---------- text: ', form.content)
            data = Message.objects.all()
            return render(request, 'formcontent.html', locals())
        else:
            form = MessageForm()
            return render(request, 'index.html', locals())
