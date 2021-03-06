# Generated by Django 2.1.4 on 2019-01-03 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('connection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tunnel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('endpoint_ip', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('bind_address', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('bind_port', models.CharField(blank=True, default=None, max_length=5, null=True)),
                ('creation', models.DateField(auto_now_add=True)),
                ('authorized_access', models.TextField(blank=True, default=None, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='connection.Client')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tunnel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
