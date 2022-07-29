# Generated by Django 4.0.3 on 2022-07-29 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scraper_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('current_price', models.FloatField(blank=True)),
                ('old_price', models.FloatField(default=0)),
                ('price_difference', models.FloatField(default=0)),
                ('rating', models.CharField(max_length=30)),
                ('rating_count', models.IntegerField()),
                ('url', models.URLField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('indices', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraper_app.indice')),
            ],
            options={
                'ordering': ('-created', 'current_price'),
            },
        ),
    ]
