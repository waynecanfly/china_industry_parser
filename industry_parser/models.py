# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 2
    max_page_size = 5
    page_size_query_param = 'size'
    page_query_param = 'page'


class Industry(models.Model):
    industry = models.CharField(max_length=128)
    security_code = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'industry'
