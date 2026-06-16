from rest_framework import mixins, viewsets

from .models import Note
from .serializers import NoteSerializer


class NoteViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """CRUD API for notes.

    Provides:
    - GET /notes/
    - POST /notes/
    - GET /notes/{id}/
    - PUT /notes/{id}/
    - DELETE /notes/{id}/
    """

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
