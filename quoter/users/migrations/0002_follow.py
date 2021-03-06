# Generated by Django 3.1.1 on 2020-12-03 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dst_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinations', to=settings.AUTH_USER_MODEL)),
                ('src_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sources', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('src_user', 'dst_user')},
            },
        ),
    ]
