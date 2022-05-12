# Generated by Django 4.0.4 on 2022-05-10 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='usermodels',
            name='posts',
        ),
        migrations.CreateModel(
            name='PostsModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Sem título', max_length=255, verbose_name='Título')),
                ('text', models.TextField(verbose_name='Texto')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='accounts.usermodels')),
                ('like', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.likemodels')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='likemodels',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.usermodels'),
        ),
    ]