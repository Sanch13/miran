from django import forms


class CreateSign(forms.Form):
    fio = forms.CharField()
    role = forms.CharField()
    tel_1 = forms.IntegerField()
    tel_2 = forms.IntegerField(required=False)

    def __init__(self, *args, **kwargs):
        super(CreateSign, self).__init__(*args, **kwargs)
        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control'
