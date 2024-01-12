from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    contents = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']