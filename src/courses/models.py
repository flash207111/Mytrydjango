from django.db import models
from django.urls import reverse


class Courses(models.Model):
    title = models.CharField(max_length=120)

    def get_absolute_url(self):
        return reverse("courses:courses-detail", kwargs={"id": self.id})
        # return f"/product/{self.id}"

