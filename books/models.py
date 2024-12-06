from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn_number = models.CharField(max_length=13)
    pages = models.IntegerField()

    def __str__(self):
        book_name = self.title
        author_name = self.author
        return f"{book_name} by {author_name}"


        