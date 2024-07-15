from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()

    def __str__(self):
        return self.title

# class Borrower(models.Model):
#     name = models.CharField(max_length=100)
#     books_borrowed = models.ManyToManyField(Book, through='Borrowing')

#     def __str__(self):
#         return self.name

# class Borrowing(models.Model):
#     borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     borrow_date = models.DateField()
#     return_date = models.DateField(blank=True, null=True)

#     def __str__(self):
#         return f'{self.borrower} - {self.book}'
