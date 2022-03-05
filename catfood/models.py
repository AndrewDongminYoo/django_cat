from django.db import models
# Create your models here.


class Brand(models.Model):
    en_name = models.CharField(max_length=255, unique=True, verbose_name='브랜드명')
    ko_name = models.CharField(max_length=255, verbose_name='한글명')
    site = models.URLField(unique=True, verbose_name='사이트')
    description = models.TextField(null=True, blank=True, verbose_name='설명')

    def __str__(self):
        return self.en_name


class Formula(models.Model):
    title = models.CharField(max_length=255, verbose_name='상품명')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='브랜드')
    url = models.URLField(unique=True, verbose_name='상품 URL')
    image = models.TextField(null=True, verbose_name='이미지 URL')
    site = models.URLField(null=True, blank=True, verbose_name='상위 URL')
    key_benefits = models.TextField(null=True, blank=True, verbose_name='주요 장점')
    ingredients = models.TextField(null=True, blank=True, verbose_name='사용된 원료')
    analysis = models.TextField(null=True, blank=True, verbose_name='등록성분량')
    calorie = models.CharField(max_length=45, null=True, blank=True, verbose_name='열량')
    additives = models.TextField(null=True, blank=True, verbose_name='추가 성분')
    description = models.TextField(null=True, blank=True, verbose_name='설명')


class Market(models.Model):
    eng_name = models.CharField(max_length=255, unique=True, verbose_name='영문 마켓명')
    kor_name = models.CharField(max_length=255, unique=True, verbose_name='한글 마켓명')
    url = models.URLField(unique=True, verbose_name='마켓 URL')

    def __str__(self):
        return self.eng_name
