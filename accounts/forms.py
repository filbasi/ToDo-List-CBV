from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):

    # class Meta:
    #     model = get_user_model()
    #     fields = ('username', 'password1', 'password2',)
    #     # help_texts = {
    #     #     'username': None,
    #     #     'password1': None,
    #     #     'password2': None,
    #     #     }

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None