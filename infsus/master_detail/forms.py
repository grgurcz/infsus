from django import forms
from .models import Computer, Desk, ComputerComponent


class DeskForm(forms.ModelForm):
    class Meta:
        model = Desk
        fields = ('name', 'location')


class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ('name', 'category', 'desk')

class ComputerComponentForm(forms.ModelForm):
    class Meta:
        model = ComputerComponent
        fields = ('name', 'component_type')

ComputerComponentFormSet = forms.inlineformset_factory(Computer, ComputerComponent, form=ComputerComponentForm, extra=1)
