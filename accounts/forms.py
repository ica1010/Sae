from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={        
        'placeholder':'Enter Password',
        'class': 'form-control',}
    ))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={ 'placeholder':'Enter Password',}
    ))
    
    class Meta:
        model = Account
        fields = ["first_name","last_name","email","phone_number","password", "address"]

    def __init__(self, *args, **kwargs):
        super(RegistrationForm , self).__init__( *args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder']='Enter your first name'
        self.fields['last_name'].widget.attrs['placeholder']='Enter your last name'
        self.fields['phone_number'].widget.attrs['placeholder']='Enter your phone number'
        self.fields['address'].widget.attrs['placeholder']='Enter your address'
        self.fields['email'].widget.attrs['placeholder']='Enter your Email Address'

        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control border-dark '
            
    def clean(self):
        cleaned_data= super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password= cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError(
                'Password does not the same'
            )

