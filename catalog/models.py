from django.db import models
from django.urls import reverse #Used to generate urls by reversing the URL patterns
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
class Genre(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name




class Book(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
      # Foreign Key used because book can only have one author, but authors can have multiple books
      # Author as a string rather than object because it hasn't been declared yet in file.
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
      # ManyToManyField used because a genre can contain many books and a Book can cover many genres.
      # Genre class has already been defined so we can specify the object above.

    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
        display_genre.short_description = 'Genre'


    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title


import uuid # Required for unique book instances
from datetime import date

from django.contrib.auth.models import User #Required to assign User as a borrower

class BookInstance(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False


    LOAN_STATUS = (
        ('d', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status= models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='d', help_text='Book availability')

    class Meta:
        ordering = ["due_back"]
        permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self):
        """
        String for representing the Model object.
        """
        #return '%s (%s)' % (self.id,self.book.title)
        return '{0} ({1})'.format(self.id,self.book.title)

class Author(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('died', null=True, blank=True)

    class Meta:
        ordering = ["last_name","first_name"]

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])


    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {1}'.format(self.last_name,self.first_name)

import os
class ITOperation(models.Model):
    """docstring for ITOperation."""
    utilitiesName = models.CharField(default='Utilidades',max_length=100)
    utilitiesFile = models.FileField(upload_to='documents/%Y/%m/%d')
    humanCapitalName = models.CharField(default='Personal',max_length=100)
    humanCapitalFile = models.FileField(upload_to='documents/%Y/%m/%d')
    assetsName = models.CharField(default='Activos',max_length=100)
    assetsFile = models.FileField(upload_to='documents/%Y/%m/%d')

    class Meta:
            permissions = (("see_itoperation", "Ver la capa de operación"),)


    def save(self, *args, **kwargs):
        if ITOperation.objects.exists() and not self.pk:
        # if you'll not check for self.pk
        # then error will also raised in update of exists model
            raise ValidationError('There is can be only one ITOperation instance')
        return super(ITOperation, self).save(*args, **kwargs)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return 'ITOperation'


class ITManagement(models.Model):
    """docstring for ITManagement."""
    projectsName = models.CharField(default='Proyectos',max_length=100)
    projectsFile = models.FileField(upload_to='documents/%Y/%m/%d')
    businessProcessesName = models.CharField(default='Procesos de negocio',max_length=100)
    businessProcessesFile = models.FileField(upload_to='documents/%Y/%m/%d')
    servicesName = models.CharField(default='Servicios',max_length=100)
    servicesFile = models.FileField(upload_to='documents/%Y/%m/%d', blank=True)

    class Meta:
            permissions = (("see_itmanagement", "Ver la capa de gestión"),)

    def save(self, *args, **kwargs):
        if ITManagement.objects.exists() and not self.pk:
        # if you'll not check for self.pk
        # then error will also raised in update of exists model
            raise ValidationError('There is can be only one ITManagement instance')
        return super(ITManagement, self).save(*args, **kwargs)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return 'ITManagement'

class ITGovernance(models.Model):
    """docstring for ITGovernance."""
    directionName = models.CharField(default='Dirección',max_length=100)
    directionFile = models.FileField(upload_to='documents/%Y/%m/%d')
    evaluationName = models.CharField(default='Evaluación',max_length=100)
    evaluationFile = models.FileField(upload_to='documents/%Y/%m/%d')
    monitorizationName = models.CharField(default='Monitorización',max_length=100)
    monitorizationFile = models.FileField(upload_to='documents/%Y/%m/%d', blank=True)

    class Meta:
            permissions = (("see_itgovernance", "Ver la capa de governanza"),)



    def save(self, *args, **kwargs):
        if ITGovernance.objects.exists() and not self.pk:
        # if you'll not check for self.pk
        # then error will also raised in update of exists model
            raise ValidationError('There is can be only one ITGovernance instance')
        return super(ITGovernance, self).save(*args, **kwargs)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return 'ITGovernance'

class CorpGovernance(models.Model):
    """docstring for CorpGovernance."""
    structuresName = models.CharField(max_length=100)
    structuresFile = models.FileField(upload_to='documents/%Y/%m/%d')
    applicationsName = models.CharField(default='Aplicaciones',max_length=100)
    applicationsFile = models.FileField(upload_to='documents/%Y/%m/%d')
    valueFile = models.FileField(upload_to='documents/%Y/%m/%d', blank=True)
    valueName = models.CharField(default='Valor',max_length=100)
    class Meta:
            permissions = (("see_corpgovernance", "Ver la capa de el gobierno corporativo"),)


    def save(self, *args, **kwargs):
        if CorpGovernance.objects.exists() and not self.pk:
        # if you'll not check for self.pk
        # then error will also raised in update of exists model
            raise ValidationError('There is can be only one CorpGovernance instance')
        return super(CorpGovernance, self).save(*args, **kwargs)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return 'CorpGovernance'



class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
