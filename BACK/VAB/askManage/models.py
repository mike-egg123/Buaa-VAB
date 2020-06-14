from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from Usergroup.models import Usergroup

# 申请
class Ask(models.Model):
    asker = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='Asker'
    )

    group = models.ForeignKey(
        Usergroup,
        on_delete=models.CASCADE,
        related_name='Group'
    )

    created = models.DateTimeField(default=timezone.now)

    state = models.IntegerField(default=0)

    def __str__(self):
        return self.asker.username