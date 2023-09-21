from django.shortcuts import render


# Create your views here.
def home(request):
    context = {}
    return render(request=request,
                  template_name="users/base.html",
                  context=context)
