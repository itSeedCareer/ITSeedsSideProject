# Generated by Django 2.1.7 on 2019-03-11 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('passwordConfirmation', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('age', models.PositiveSmallIntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('ducation', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
