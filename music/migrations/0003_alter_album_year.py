from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_album_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]