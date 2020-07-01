from django import forms
from .models import SequenceModel
from django.core.validators import RegexValidator

ACTG = RegexValidator(r'^[actgACTG\n\r\t ]*$', 'Only the characters A, C, T, and G are allowed.')

#name = models.CharField(max_length=50, blank=True, null=True, validators=[alphanumeric])

class SeqenceForm(forms.ModelForm):
    seq = forms.CharField(widget=forms.Textarea(
                                        attrs={'placeholder':'Enter a DNA Sequence...',
                                               'pattern':'[actgACTG]+'}), 
                          label='',
                          validators=[ACTG],
                         )
    class Meta:
        model = SequenceModel
        fields = ('seq',)