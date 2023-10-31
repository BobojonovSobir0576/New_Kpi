# Generated by Django 4.2.6 on 2023-10-30 12:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('ball_of_cate', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'verbose_name': 'Bosh kategoriyaga tegishli Kategoriyalar',
                'verbose_name_plural': '2 Bosh kategoriyaga tegishli Kategoriyalar',
            },
        ),
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(upload_to='file', verbose_name='Yuborilgan faylar')),
                ('is_activte', models.BooleanField(default=False)),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Kiritilgan sana')),
                ('add_ball', models.ManyToManyField(blank=True, null=True, related_name='balls', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Avtor')),
            ],
            options={
                'verbose_name': 'Yuklangan faylar',
                'verbose_name_plural': '4 Yuklangan fayllar',
            },
        ),
        migrations.CreateModel(
            name='MainCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('ball_of_cate', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'verbose_name': 'Bosh kategoriya',
                'verbose_name_plural': '1 Bosh kategoriya',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Амалга ошириладиган ишлар')),
                ('date_of_calculation_ball', models.CharField(max_length=50, verbose_name='Натижаларни ҳисоблаб бориш муддати')),
                ('ball_of_question', models.IntegerField(default=0, verbose_name='Балл')),
                ('description', models.TextField(verbose_name='Балларни ҳисоблаш методикаси')),
                ('description1', models.TextField(verbose_name='Jarima ballari')),
                ('add_user', models.ManyToManyField(blank=True, null=True, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('categories_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categories', verbose_name='Kategoriyaning IDsi')),
                ('put_ball', models.ManyToManyField(related_name='ball_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Kategoriyaning Savollari',
                'verbose_name_plural': '3 Kategoriyaning Savollari',
            },
        ),
        migrations.CreateModel(
            name='PutBall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ball', models.IntegerField(blank=True, default=0, null=True, verbose_name='Балл')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Kiritilgan sana')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL, verbose_name='Avtor')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.fileupload', verbose_name='Savol IDsi')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': "Qo'yilgan ballar",
                'verbose_name_plural': "5 Qo'yilgan ballar",
            },
        ),
        migrations.AddField(
            model_name='fileupload',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.questions', verbose_name='Savol IDsi'),
        ),
        migrations.AddField(
            model_name='categories',
            name='main_categories_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.maincategories'),
        ),
    ]