from django.db import models

class Book(models.Model):
    """
    Book
    """
    title = models.CharField(max_length=200)
    available = models.BooleanField(default=False)
    

    class Meta:

        def __str__(self):
            """Return string."""
            return self.title

class Request(models.Model):
    """
    Request
    """
    email = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)

    class Meta:

        def __str__(self):
            """Return string."""
            return self.email