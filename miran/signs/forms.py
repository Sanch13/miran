from django import forms


class CreateSign(forms.Form):
    CHOICES = [('new', 'new'), ('old', 'old')]

    fio = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Иван Иванов'}))
    role = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Старший помошник младшего кочегара'}))
    tel_1 = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '297775533'}))
    tel_2 = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'placeholder': '447775533'}))
    sign = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        super(CreateSign, self).__init__(*args, **kwargs)
        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control'
