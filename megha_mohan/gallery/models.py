from django.db import models


class Image(models.Model):
    image = models.ImageField(null=True, blank=True)
    caption = models.CharField(max_length=180, blank=False, null=False)
    added_on = models.DateTimeField(auto_now_add=True, null=False)

    class Meta:
        ordering = ['-added_on']

    def __str__(self):
        return self.caption
