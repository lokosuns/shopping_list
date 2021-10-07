from django import forms
from todo_item.models import ItemModel

class ItemForm(forms.ModelForm):

    expare_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )

    class Meta:
        model = ItemModel
        fields = ('name', 'list_model', 'expare_date')

