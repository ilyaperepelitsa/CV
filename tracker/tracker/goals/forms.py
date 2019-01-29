from django import forms

class ValueForm(forms.Form):
    value_name = forms.CharField(widget = forms.TextInput())
    value_description = forms.CharField(widget = forms.Textarea(
                                    attrs = {"rows" : 5, "cols" : 40}))
    # country = forms.CharField(widget = forms.HiddenInput())

# class SearchForm(forms.Form):
#     query = forms.CharField(label = "Enter a keyword to search for:",
#                             widget = forms.TextInput(attrs = {
#                                                     "size" : 32,
#                                                     "class" : "form-control"
#                                                                 }))
