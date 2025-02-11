from django.db import models
#
# # Create your models here.
# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#
#     def __str__(self):
#         return f'{self.name}'
#
# class Book(models.Model):
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     published_year = models.IntegerField()
#
#     def __str__(self):
#         return f'{self.title}'
#
# class Reader(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     books = models.ManyToManyField(Book, related_name='readers')
#     def __str__(self):
#         return f'{self.name}'
#
#
