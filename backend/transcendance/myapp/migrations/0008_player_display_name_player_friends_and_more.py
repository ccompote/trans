# Generated by Django 5.0.4 on 2024-05-03 21:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_ensure_user_integrity'),
        ('authtoken', '0004_alter_tokenproxy_options'), 
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='display_name',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='player',
            name='friends',
            field=models.ManyToManyField(blank=True, to='myapp.player'),
        ),
        migrations.AddField(
            model_name='player',
            name='online_status',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_requests_sent', to='myapp.player')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_requests_received', to='myapp.player')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('played_on', models.DateTimeField(auto_now_add=True)),
                ('details', models.TextField()),
                ('players', models.ManyToManyField(related_name='matches', to='myapp.player')),
                ('winner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='won_matches', to='myapp.player')),
            ],
        ),
        migrations.DeleteModel(
            name='Game',
        ),
    ]
