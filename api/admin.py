from django.contrib import admin
from .models import *

@admin.register(MainCategories)
class MainCategoriesAdmin(admin.ModelAdmin):
    list_display = ('name','id')
    
    
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name','ball_of_cate')
    
    
@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('question','id')
    
    
@admin.register(FileUpload)
class FileUploadAdmin(admin.ModelAdmin):
    list_display = ('question_id','id')
    

@admin.register(PutBall)
class PutBallAdmin(admin.ModelAdmin):
    list_display = ('question_id','id')
    

@admin.register(Repetition)
class PutBallAdmin(admin.ModelAdmin):
    list_display = ('question_id','id')