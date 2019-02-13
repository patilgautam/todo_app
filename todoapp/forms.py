from django import forms

class TodoForm(forms.Form):
    text=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter todo item e.g Project meeting',
                                                                     'aria-label':'Todo'}))
    # attrs={'class' : 'form-control', 'placeholder' : 'Enter todo e.g. Delete junk files',
    # 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}