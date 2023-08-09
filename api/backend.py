from django.conf import settings
from django.contrib.auth.backends import BaseBackend, UserModel


class SettingsBackend(BaseBackend):

    def authenticate(self, request, phone=None, password=None):

        phone_kwargs = {'phone': phone}
        email_kwargs = {'email': phone}
        try:
            user = UserModel.objects.get(**phone_kwargs)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            try:
                user = UserModel.objects.get(**email_kwargs)
                if user.check_password(password):
                    return user
            except UserModel.DoesNotExist:
                return None

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
