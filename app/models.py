# models.py
from unittest.util import _MAX_LENGTH
from django.db import models
from jsignature.mixins import JSignatureFieldsMixin


class ExampleModel(JSignatureFieldsMixin):
    employee_name = models.CharField(max_length=120,null=False,blank=False)
    topic = models.CharField(max_length=200,null=False,blank=False)
    