# Generated by Django 4.2.1 on 2023-06-01 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_album_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='album',
            name='is_active',
        ),
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='album',
            name='label',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.label'),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.artist'),
        ),
    ]