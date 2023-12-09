from django.http import HttpResponse
from django.shortcuts import render

from .forms import CreateSign
from .utils import create_signs


def change_signs(request):
    return render(request=request,
                  template_name="signs/change_sign.html")


def create_sign(request):
    if request.method == "POST":
        form = CreateSign(data=request.POST)
        if form.is_valid():
            fio = form.cleaned_data.get("fio")
            role = form.cleaned_data.get("role")
            tel_1 = form.cleaned_data.get("tel_1")
            tel_2 = form.cleaned_data.get("tel_2")
            sign = form.cleaned_data.get("sign")
            sign_user = create_signs(fio=fio,
                                     role=role,
                                     tel_1=tel_1,
                                     tel_2=tel_2,
                                     sign=sign)
            response = HttpResponse(content_type='text/html')
            response['Content-Disposition'] = f'attachment; filename="my_sign.html"'
            response.write(content=sign_user)
            return response

    else:
        form = CreateSign()
        context = {
            "form": form
        }
    return render(request=request,
                  template_name="signs/create_sign.html",
                  context=context)
