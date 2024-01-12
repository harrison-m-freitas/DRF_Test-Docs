# Generated by Django 5.0.1 on 2024-01-12 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('F', 'Film'), ('S', 'Series')], default='F', max_length=1)),
                ('realese_date', models.DateField()),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]