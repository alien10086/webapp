
from django.forms import ModelForm
from django.db import models







class Author(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name

class Entry(models.Model):
    author = models.ForeignKey(Author)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()


    def __str__(self):
        return self.headline


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['author', 'headline', 'body_text', 'pub_date']

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name']
