from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from api.base.Models.UserModels import UserModel


class userModelCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = UserModel
        fields = ('email',)


class userModelChangeForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('email',)
