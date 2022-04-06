from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

class TeamData(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        labels = ["DIST", "HR90"]
        teamData = [5000, 15]
        data = {
            "labels": labels,
            "default": teamData,
        }
        return Response(data)