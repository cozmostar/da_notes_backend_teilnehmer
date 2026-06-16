"""Django model for notes."""

import uuid

from django.db import models


class Note(models.Model):
    """Single note persisted in SQLite with Django ORM."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    marked = models.BooleanField(default=False)
    trash = models.BooleanField(default=False)

    def __str__(self) -> str:  # pragma: no cover
        return f"{self.title} ({self.id})"
