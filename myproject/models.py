# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class QzServersCpuUsageLogs(models.Model):
    id_no = models.CharField(max_length=4, blank=True,
                             null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    avg_cpu_usage = models.CharField(max_length=13, blank=True,
                                     null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    qz_server = models.CharField(max_length=24, blank=True,
                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    create_time = models.CharField(max_length=19, blank=True,
                                   null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'qz_servers_cpu_usage_logs'

    def __str__(self):
        return u'%s %s %s %s' % (self.id_no, self.avg_cpu_usage, self.qz_server, self.create_time)


class QzServersGpuUsageLogs(models.Model):
    id_no = models.CharField(max_length=5, blank=True, null=True)
    col_2 = models.CharField(db_column='COL 2', max_length=12, blank=True,
                             null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_3 = models.CharField(db_column='COL 3', max_length=16, blank=True,
                             null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_4 = models.CharField(db_column='COL 4', max_length=14, blank=True,
                             null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_5 = models.CharField(db_column='COL 5', max_length=6, blank=True,
                             null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_6 = models.CharField(db_column='COL 6', max_length=17, blank=True,
                             null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_7 = models.CharField(db_column='COL 7', max_length=21, blank=True,
                             null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_8 = models.CharField(db_column='COL 8', max_length=15, blank=True,
                             null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    utilization_gpu = models.CharField(max_length=15, blank=True, null=True)
    col_10 = models.CharField(db_column='COL 10', max_length=18, blank=True,
                              null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_11 = models.CharField(db_column='COL 11', max_length=19, blank=True,
                              null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_12 = models.CharField(db_column='COL 12', max_length=11, blank=True,
                              null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_13 = models.CharField(db_column='COL 13', max_length=11, blank=True,
                              null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    server_name = models.CharField(max_length=24, blank=True, null=True)
    created_timestamp = models.CharField(max_length=19, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qz_servers_gpu_usage_logs'

    def __str__(self):
        return u'%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (
        self.id_no, self.col_2, self.col_3, self.col_4, self.col_5, self.col_6, self.col_7, self.col_8,
        self.utilization_gpu, self.col_10, self.col_11, self.col_12, self.col_13, self.server_name,
        self.created_timestamp)
