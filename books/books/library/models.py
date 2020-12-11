from django.db import models


class Book(models.Model):
    """
    Book
    """
    title = models.CharField(max_length=200)    
    def __str__(self):
        """Return string."""
        return self.title

    def is_available(self):
        try:
            self.request
            return False
        except:
            return True

class Request(models.Model):
    """
    Request
    """
    email = models.EmailField(max_length=200)
    timestamp = models.DateTimeField(auto_now=True)
    book = models.OneToOneField('Book', on_delete=models.CASCADE, related_name='request')

    def __str__(self):
        """Return string."""
        return self.email, self.book.title