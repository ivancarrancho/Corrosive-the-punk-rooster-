from django import forms
from cms.models import Team

class TeamUseradminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TeamUseradminForm, self).__init__(*args, **kwargs)
        self.args = args

    def clean(self):
        cleaned_data = super(TeamUseradminForm, self).clean()

        return cleaned_data

    class Meta:

        model = Team
        fields = [
            'name',
            'logo',
            'description',
        ]
