from rest_framework.throttling import UserRateThrottle
from rest_framework.throttling import AnonRateThrottle


class MovieRateThrottle(UserRateThrottle):
    scope = 'movie'

class PlatformRateThrottle(UserRateThrottle):
    scope = 'platform'