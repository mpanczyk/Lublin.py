from django.shortcuts import render
from django.http import HttpResponse
from orders import models as m

# Create your views here.


def home(request):
    return render(request, 'orders/hello.html')


def provider_list(request):
    providers = m.Provider.objects.all()
    context = {
      'providers': providers,
    }
    return render(
        template_name='orders/provider_list.html',
        context=context,
        request=request,
    )
