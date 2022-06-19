from django.db import models

# Create your models here.


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    tag = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=200, null=True)
    reading_time = models.DecimalField(
        max_digits=5, decimal_places=0, null=True)
    content = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to='post/')

    def __str__(self):
        return self.title
