import os
from social.backends.oauth import BaseOAuth2
from django.conf import settings
from messenger.models import Messenger


class drchronoOAuth2(BaseOAuth2):
    """
    drchrono OAuth authentication backend
    """

    name = 'drchrono'
    AUTHORIZATION_URL = 'https://drchrono.com/o/authorize/'
    ACCESS_TOKEN_URL = 'https://drchrono.com/o/token/'
    ACCESS_TOKEN_METHOD = 'POST'
    REDIRECT_STATE = False
    USER_DATA_URL = 'https://drchrono.com/api/users/current'
    EXTRA_DATA = [
        ('refresh_token', 'refresh_token'),
        ('expires_in', 'expires_in')
    ]
    # TODO: setup proper token refreshing

    def get_user_details(self, response):
        print '1'
        """
        Return user details from drchrono account
        """
        return {'username': response.get('username'),}

    def user_data(self, access_token, *args, **kwargs):
        print '2'
        """
        Load user data from the service
        """
        return self.get_json(
            self.USER_DATA_URL,
            headers=self.get_auth_header(access_token)
        )

    def get_auth_header(self, access_token):
        print '3'
        if len(Messenger.objects.all()) == 0:
            m = Messenger()
            m.name = str(access_token)
            m.save()
        else:
            m = Messenger.objects.first()
            m.name = str(access_token)
            m.save()
        print m.name
        return {'Authorization': 'Bearer {0}'.format(access_token)}
