from django import forms
from django.core import validators


def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Name must start with "Z"')


class FormName(forms.Form):
    name = forms.CharField(max_length=64,)
    email = forms.EmailField()
    vmail = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)

    botcatcher = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        validators=[validators.MaxLengthValidator(0)]
    )

    def clean(self):
        form = super().clean()
        if form['email'] != form['vmail']:
            raise forms.ValidationError('Emails not matched!')

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError('GOTCHA BOT!')
    #     return botcatcher
