# Generated by Django 4.2.6 on 2023-10-20 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0003_libro_imagen'),
    ]

    operations = [
        migrations.AlterModelTableComment(
            name='usuario',
            table_comment='Complemento usuario',
        ),
        migrations.CreateModel(
            name='Pretamo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_prestamo', models.DateTimeField(auto_now_add=True)),
                ('fecha_devolucion', models.DateTimeField()),
                ('fecha_devolucion_real', models.DateTimeField()),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='library.libro')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
