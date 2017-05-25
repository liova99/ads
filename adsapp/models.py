from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
import datetime


# Create your models here.

class AutoDateTimeField(models.DateTimeField):
    """Make auto date time editable
    created_at = models.DateField(default=timezone.now)
    updated_at = models.AutoDateTimeField(default=timezone.now)"""
    def pre_save(self, model_instance, add):
        return datetime.datetime.now()


class Adds(models.Model):
    article_name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits = 12, decimal_places=2)
    city = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    details = models.TextField()
    # after creation add manualy to database default id
    id_number = models.AutoField(primary_key=True)
    # TODO make update time field
    date = models.DateTimeField(default=timezone.now)
    photo = models.FileField()

    def get_absolute_url(self):
        return reverse('adsapp:detail', kwargs = {'pk': self.pk})

    def __str__(self):
        return self.article_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days = 1) <= self.date <= now

    was_published_recently.admin_order_field = 'date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
