from django.db import models
from django.contrib.auth.models import *

verbose_name=''
class MainCategories(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Asosiy kategoriya nomi')
    ball_of_cate = models.IntegerField(default=0, null=True, blank=True, verbose_name='Unga quyiladigan ball')    
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bosh kategoriya"
        verbose_name_plural = "1 Bosh kategoriya"
        

class Categories(models.Model):
    name = models.CharField(max_length=150, verbose_name='Kategoriya nomi')
    main_categories_id = models.ForeignKey(MainCategories, on_delete=models.CASCADE, verbose_name='Asosiy Kategotiya nomi va idsi')
    ball_of_cate = models.IntegerField(default=0, null=True, blank=True, verbose_name='Unga quyilgan ball')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bosh kategoriyaga tegishli Kategoriyalar"
        verbose_name_plural = "2 Bosh kategoriyaga tegishli Kategoriyalar"
        
        
class Questions(models.Model):
    question = models.TextField("Амалга ошириладиган ишлар")
    date_of_calculation_ball = models.CharField("Натижаларни ҳисоблаб бориш муддати",max_length=50)
    ball_of_question = models.IntegerField("Балл",default=0)
    description = models.TextField("Балларни ҳисоблаш методикаси",)
    categories_id = models.ForeignKey(Categories, on_delete=models.CASCADE,verbose_name='Kategoriyaning IDsi')
    description1 = models.TextField("Jarima ballari",)
    put_ball = models.ManyToManyField(User, related_name='ball_user', verbose_name='Baholovchilar')
    add_user = models.ManyToManyField(User, related_name='user',null=True, blank=True, verbose_name='Tegilmasin')
    
    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = "Kategoriyaning Savollari"
        verbose_name_plural = "3 Kategoriyaning Savollari"
        
        
class FileUpload(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Avtor')
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE,verbose_name='Savol IDsi')
    files = models.FileField(upload_to='file',verbose_name='Yuborilgan faylar')
    is_activte = models.BooleanField(default=False, verbose_name='Tegilmasin')
    add_ball = models.ManyToManyField(User, related_name='balls',null=True, blank=True)
    repition_ball = models.ManyToManyField(User, related_name='repition',null=True, blank=True)
    created_date = models.DateField(auto_now=False,auto_now_add=True,verbose_name='Kiritilgan sana')
    
    def __str__(self):
        return f'{self.question_id.question}'
    
    class Meta:
        verbose_name = "Yuklangan faylar"
        verbose_name_plural = "4 Yuklangan fayllar"
        
        
class PutBall(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Avtor', related_name='author')
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='User')
    question_id = models.ForeignKey(FileUpload, on_delete=models.CASCADE,verbose_name='Savol IDsi')
    ball = models.IntegerField("Балл",default=0, null=True, blank=True)
    created_date = models.DateField(auto_now=False,auto_now_add=True,verbose_name='Kiritilgan sana')
    
    
    class Meta:
        verbose_name = "Qo'yilgan ballar"
        verbose_name_plural = "5 Qo'yilgan ballar"

class Repetition(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Avtor', related_name='authors')
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='User', related_name='us')
    question_id = models.ForeignKey(FileUpload, on_delete=models.CASCADE,verbose_name='Savol IDsi')
    files = models.FileField(upload_to='file',verbose_name='Yuborilgan faylar')
    ball = models.IntegerField("Балл",default=0, null=True, blank=True)
    created_date = models.DateField(auto_now=False,auto_now_add=True,verbose_name='Kiritilgan sana')
    
    
    class Meta:
        verbose_name = "Qaytarilgan ballar"
        verbose_name_plural = "6 Qaytarilgan ballar"