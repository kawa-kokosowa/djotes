from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from djotes.rest.models import Note
from djotes.rest.permissions import IsOwner
from djotes.rest.serializers import NoteSerializer, UserSerializer


class NoteViewSet(viewsets.ModelViewSet):
    """This endpoint presents notes.

    The owner of the note may update or delete existing notes,
    or create a new one.

    """

    #queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(owner=user)


# should just be for only a user in the system,
# create new user, get user info, update user info
#
# use modelview not modelviewset...?
class UserViewSet(viewsets.ModelViewSet):
    """This endpoint presents the users in the system.

    This is mainly for creating new users (anonymously)
    and performing 
    Notes belonging to a user are serialized using
    hyperlinked representation.

    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    # TODO: permissions IsMatchUsername

    def get_queryset(self):
        user = self.request.user

        # if admin get all else get only the user
        if isadmin...
            return User.objects.all()
        else:
            return User.objects.filter(username=user.username)
