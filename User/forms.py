from django import forms
from User.models import UserDataComplete

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserDataComplete
        fields = "__all__"

    # def __init__(self, *args, **kwargs):
    #     super(RegistrationForm, self).__init__(*args, **kwargs)

    #     cleaned_data = super(RegistrationForm, self).clean()

    #     return cleaned_data