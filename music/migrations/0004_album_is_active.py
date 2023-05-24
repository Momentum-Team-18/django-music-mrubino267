from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_alter_album_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]