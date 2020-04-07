from django import forms
from app_two.models import States, Documents, Headings, SubHeadings, Texts, Relations

# Data entry form
class StateForm(forms.ModelForm):
    state = forms.CharField()

    class Meta():
        model = States
        fields = '__all__'

class DocumentForm(forms.ModelForm):
    title = forms.CharField()

    class Meta():
        model = Documents
        fields = ('title',)
        # widgets = {'document_id':forms.HiddenInput()}

class HeadingForm(forms.ModelForm):
    heading = forms.CharField()

    class Meta():
        model = Headings
        fields = ('heading',)

class SubHeadingForm(forms.ModelForm):
    subheading = forms.CharField()

    class Meta():
        model = SubHeadings
        fields = ('subheading',)

class TextForm(forms.ModelForm):
    keywords = forms.CharField()
    text = forms.CharField(widget=forms.Textarea(
            attrs={
                'placeholder': 'This is the placeholder'
            }
        ))

    class Meta():
        model = Texts
        fields = '__all__'

class UpdateTextForm(forms.ModelForm):
    keywords = forms.CharField()
    text = forms.CharField(widget=forms.Textarea(
            attrs={
                'placeholder': 'This is the placeholder'
            }
        ))

    class Meta():
        model = Texts
        exclude = ('id',)

class RelationsForm(forms.ModelForm):
    # state = forms.ModelChoiceField(queryset=States.objects.all())
    # document = forms.ModelChoiceField(queryset=Documents.objects.all())
    # heading = forms.ModelChoiceField(queryset=Headings.objects.all())
    # subheading = forms.ModelChoiceField(queryset=SubHeadings.objects.all())
    # text = forms.ModelChoiceField(queryset=Texts.objects.all())

    class Meta():
        model = Relations
        fields = 'state','document','heading','subheading','text'
        