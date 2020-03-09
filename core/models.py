from ckeditor.fields import RichTextField
from django.db import models


class HeaderCategory(models.Model):
    name = models.CharField('Name', max_length=100)
    class_name = models.CharField('Class_name', max_length=200)
    url = models.CharField('Url', max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Header Category"
        verbose_name_plural = "Header Categories"


class WebsiteSetting(models.Model):
    site_purpose = RichTextField('Saytın məqsədi', null=True, blank=True)
    technical_glance = RichTextField('Texniki baxış', null=True, blank=True)
    glass_tinting = RichTextField('Şüşələrinin tündləşdirilməsi', null=True, blank=True)
    fees_and_taxes = RichTextField('Rüsumlar və vergilər', null=True, blank=True)
    fines = RichTextField('Cərimələr', null=True, blank=True)
    contact_us = RichTextField('Əlaqə', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Text modeli"
        verbose_name_plural = "Text modelleri"

#---------------------------Test--------------------------


class TestCategory(models.Model):
    name = models.CharField('Category name', max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Test Category'
        verbose_name_plural = 'Test Categorys'


class QuestionAnswer(models.Model):
    category_name = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=200)
    options1 = models.CharField('Options 1', max_length=100)
    options2 = models.CharField('Options 2', max_length=100)
    options3 = models.CharField('Options 3', max_length=100)
    options4 = models.CharField('Options 4', max_length=100)
    answer = models.CharField('Answer', max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Question and Answer'
        verbose_name_plural = 'Question and Answers'