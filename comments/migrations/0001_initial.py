# Generated by Django 2.1.1 on 2018-09-09 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('ip', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=200)),
            ],
        ),
    ]
