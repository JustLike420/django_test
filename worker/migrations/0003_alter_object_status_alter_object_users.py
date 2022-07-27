# Generated by Django 4.0.6 on 2022-07-27 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0002_alter_user_options_alter_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='status',
            field=models.TextField(choices=[('Создан', 'Создан'), ('Запущен', 'Запущен'), ('Остановлен', 'Остановлен')], default='created', max_length=20, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='object',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, related_name='objects', to='worker.user', verbose_name='Исполнитель'),
        ),
    ]