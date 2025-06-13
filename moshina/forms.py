from  django import forms
from  .models import Moshina


class MoshinaForm(forms.ModelForm):
    class Meta:
        model = Moshina
        fields = '__all__'