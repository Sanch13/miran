from django.shortcuts import render
from django.conf import settings

from .forms import CreateSign
from .utils import create_signs


def change_signs(request):
    return render(request=request,
                  template_name="signs/change_sign.html")


def create_sign(request):
    request.session['sign'] = request.GET.get("sign")
    if request.method == "POST":
        form = CreateSign(data=request.POST)
        if form.is_valid():
            fio = form.cleaned_data.get("fio")
            role = form.cleaned_data.get("role")
            tel_1 = form.cleaned_data.get("tel_1")
            tel_2 = form.cleaned_data.get("tel_2")
            print(fio, role, tel_1, tel_2)
            # file =  if request.session['sign'] == "new"
            # sign = create_signs()
            # response = HttpResponse(sign, content_type='text/plain')
            # response['Content-Disposition'] = f'attachment; filename={file_name}'
            # return response

    form = CreateSign()
    context = {
        "form": form
    }
    return render(request=request,
                  template_name="signs/create_sign.html",
                  context=context)
