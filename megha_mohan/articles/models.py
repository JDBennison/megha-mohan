from django.db import models


CATEGORY = (
    (0, "Article"),
    (1, "Broadcast"),
    (2, "Public Speaking")
)


class Article(models.Model):
    headline = models.CharField(max_length=200, blank=False, null=False)
    url = models.URLField(max_length=1024, blank=False, null=False)
    image = models.ImageField(null=True, blank=True)
    category = models.IntegerField(choices=CATEGORY, default=0)
    date_published = models.DateField(null=False)

    class Meta:
        ordering = ['-date_published']

    def __str__(self):
        return self.headline
