import uuid

from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    """All application models should inherit from this model to have all common attributes implemented by it"""

    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()


class SingletonBaseModel(BaseModel):
    """Base model for models that required to have only and only one instance of them created"""

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonBaseModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
