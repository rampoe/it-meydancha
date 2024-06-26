from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="projects/", null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
