from django import forms
from User.models import UserData

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = "__all__"

    # def __init__(self, *args, **kwargs):
    #     super(RegistrationForm, self).__init__(*args, **kwargs)

    #     cleaned_data = super(RegistrationForm, self).clean()

    #     return cleaned_data
