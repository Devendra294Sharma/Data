# Generated by Django 4.0.3 on 2022-03-10 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('City', models.CharField(max_length=40)),
                ('Country', models.CharField(max_length=40)),
                ('Roll', models.IntegerField()),
            ],
        ),
    ]
