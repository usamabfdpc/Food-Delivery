from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Users

# Forms
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Users
        fields = UserCreationForm.Meta.fields + ('email','role','phone')
        exclude = ('username',)
    def __init__(self,*args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        # self.fields['phone'].widget.attrs['class']='form-control mt-3'
        self.fields['role'].widget.attrs['class']='form-select form-control mt-3'        
        self.fields['email'].widget.attrs['class']='form-control  mt-3'
        self.fields['password1'].widget.attrs['class']='form-control  mt-3'
        self.fields['password2'].widget.attrs['class']='form-control  mt-3'