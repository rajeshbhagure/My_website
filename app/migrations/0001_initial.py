# Generated by Django 3.0.7 on 2020-10-24 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog/')),
                ('name', models.CharField(max_length=15)),
                ('short_title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('profile', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.IntegerField()),
                ('Education', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='portfolio')),
                ('name', models.CharField(max_length=30)),
                ('technology', models.CharField(max_length=30)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SkillModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=30)),
                ('percentage', models.IntegerField()),
            ],
        ),
    ]
