from django import forms
from app.models import ExpensesRegistry

class ExpensesForm(forms.ModelForm):
    class Meta:
        model = ExpensesRegistry
        fields = "__all__"

    myForm = ExpensesForm()

    article = ExpensesRegistry.objects.get(pk=1)
    myForm = ExpensesRegistry(instance=article)

