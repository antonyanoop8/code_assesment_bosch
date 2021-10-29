from django.db import models
from django.db.models import query
from django.utils.translation import ugettext_lazy as _

from accounts.models import User


class Query(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messager")
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    message = models.TextField(blank=True, null=True)
    upload = models.FileField(upload_to ='uploads/')

    class Meta:
        verbose_name = _('Query')
        verbose_name_plural = _('Queries')


class Reply(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="query_replier")
    message = models.TextField(blank=True, null=True)
    upload = models.FileField(upload_to ='uploads/')

    class Meta:
        verbose_name = _('Query')
        verbose_name_plural = _('Queries')