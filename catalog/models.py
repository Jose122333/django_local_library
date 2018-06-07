from django.db import models
from django.urls import reverse #Used to generate urls by reversing the URL patterns
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import uuid # Required for unique book instances
from datetime import date
from django.contrib.auth.models import User #Required to assign User as a borrower
import os
class ITOperation(models.Model):
    """docstring for ITOperation."""
    arrow1Name = models.CharField(max_length=100, blank=True)
    arrow1File = models.FileField(upload_to='documents/%Y/%m/%d',blank=True)
    arrow2Name = models.CharField(max_length=100, blank=True)
    arrow2File = models.FileField(upload_to='documents/%Y/%m/%d',blank=True)
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
    arrow1Name = models.CharField(max_length=100, blank=True)
    arrow1File = models.FileField(upload_to='documents/%Y/%m/%d',blank=True)
    arrow2Name = models.CharField(max_length=100, blank=True)
    arrow2File = models.FileField(upload_to='documents/%Y/%m/%d',blank=True)
    arrow3Name = models.CharField(max_length=100, blank=True)
    arrow3File = models.FileField(upload_to='documents/%Y/%m/%d',blank=True)
    arrow4Name = models.CharField(max_length=100, blank=True)
    arrow4File = models.FileField(upload_to='documents/%Y/%m/%d',blank=True)
    arrow5Name = models.CharField(max_length=100, blank=True)
    arrow5File = models.FileField(upload_to='documents/%Y/%m/%d',blank=True)
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
    arrow1Name = models.CharField(max_length=100, blank=True)
    arrow1File = models.FileField(upload_to='documents/%Y/%m/%d',blank=True)
    arrow2Name = models.CharField(max_length=100, blank=True)
    arrow2File = models.FileField(upload_to='documents/%Y/%m/%d',blank=True)
    arrow3Name = models.CharField(max_length=100, blank=True)
    arrow3File = models.FileField(upload_to='documents/%Y/%m/%d',blank=True)
    arrow4Name = models.CharField(max_length=100, blank=True)
    arrow4File = models.FileField(upload_to='documents/%Y/%m/%d',blank=True)
    arrow5Name = models.CharField(max_length=100, blank=True)
    arrow5File = models.FileField(upload_to='documents/%Y/%m/%d',blank=True)
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
    arrow1Name = models.CharField(max_length=100, blank=True)
    arrow1File = models.FileField(upload_to='documents/%Y/%m/%d',blank=True)
    arrow2Name = models.CharField(max_length=100, blank=True)
    arrow2File = models.FileField(upload_to='documents/%Y/%m/%d',blank=True)
    arrow3Name = models.CharField(max_length=100, blank=True)
    arrow3File = models.FileField(upload_to='documents/%Y/%m/%d',blank=True)
    arrow4Name = models.CharField(max_length=100, blank=True)
    arrow4File = models.FileField(upload_to='documents/%Y/%m/%d',blank=True)
    arrow5Name = models.CharField(max_length=100, blank=True)
    arrow5File = models.FileField(upload_to='documents/%Y/%m/%d',blank=True)
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
