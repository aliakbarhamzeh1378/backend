import jwt
from django.conf.global_settings import SECRET_KEY
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponseForbidden

from api.base.Models.UserModels import UserModel


class AccountAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.META.get('HTTP_AUTHORIZATION') is not None:
            if len(request.META.get('HTTP_AUTHORIZATION')) != 0:
                try:

                    token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
                    Credentials = jwt.decode(token, SECRET_KEY)
                    request._force_auth_user = UserModel.objects.get(id=Credentials['user_id'])

                except Exception as e:
                    return HttpResponseForbidden()

        else:
            request._force_auth_user = AnonymousUser()

        response = self.get_response(request)
        return response
