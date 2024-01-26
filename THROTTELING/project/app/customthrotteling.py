from rest_framework.throttling import UserRateThrottle

class StudentUserRateThrottle(UserRateThrottle):
    scope = 'student'