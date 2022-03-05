from django.db import models
# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='브랜드명')
    site = models.URLField(unique=True, verbose_name='사이트')
    description = models.TextField(null=True, blank=True, verbose_name='설명')

    def __str__(self):
        return self.name


class Formula(models.Model):
    # name = models.CharField(max_length=255, unique=True, verbose_name='상품명')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='브랜드')
    url = models.URLField(unique=True, verbose_name='상품 URL')
    key_benefits = models.TextField(null=True, blank=True, verbose_name='주요 장점')
    ingredients = models.TextField(null=True, blank=True, verbose_name='사용된 원료')
    analysis = models.TextField(null=True, blank=True, verbose_name='등록성분량')
    description = models.TextField(null=True, blank=True, verbose_name='설명')
