from django.core.exceptions import ObjectDoesNotExist
from autho.models import User


class AuthoBackend(object):

    def authenticate(self, username=None, password=None):
        user = self._get_user(username)
        if not user or user.is_obsolete:
            return None

        if not user.is_active:
            return None

        if user.check_password(password):
            return user
        else:
            return None

    def _get_user(self, key):
        try:
            return User.objects.get(username=key)
        except ObjectDoesNotExist:
            pass

        try:
            return User.objects.get(email=key)
        except ObjectDoesNotExist:
            pass

        return None

    def get_user(self, id):
        try:
            return User.objects.get(pk=id)
        except ObjectDoesNotExist:
            return None
