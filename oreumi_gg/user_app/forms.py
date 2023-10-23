from django import forms
from .models import User



class loginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }
class SignupForm(forms.ModelForm):
    class Meta:  # 메타 클래스에 사용할 모델과 필드를 설정
        model = User
        fields = ["nickname"]

    def signup(self, request, user):
        user.nickname = self.cleaned_data["nickname"] # form에 기입된 데이터를 가져오기 위해 cleaned_data 사용
        user.save()