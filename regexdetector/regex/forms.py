from django import forms

class RegexForm(forms.Form):
    user_regex = forms.CharField(label="Regex")
    test_text = forms.CharField(label="Text", 
                                widget=forms.Textarea(
                                        attrs={'placeholder': 'Enter the text you want the regex to be tested upon here..'}))