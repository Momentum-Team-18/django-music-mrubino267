from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='year',
            field=models.IntegerField(blank=True, max_length=4, null=True),
        ),
    ]
