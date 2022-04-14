# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Mascots(models.Model):
    id = models.AutoField(primary_key=True)
    color = models.CharField(max_length=200, blank=True, null=True)
    signature_move = models.CharField(max_length=200)

class Schools(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=200)
    distance_fr_dt = models.IntegerField(blank=True, null=True)

class MascotsSchools(models.Model):
    user_school_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Mascots, on_delete=models.CASCADE)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE)

class Students(models.Model):
    id = models.AutoField(primary_key=True)
    date_of_birth = models.IntegerField()
    grade_level = models.IntegerField()
    catch_phrase = models.CharField(max_length=200, blank=True, null=True)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE)

class StudentEids(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=200)
    pwd_reset_q = models.CharField(max_length=200, blank=True, null=True)
    correct_answer = models.CharField(max_length=200)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)

class Teachers(models.Model):
    id = models.AutoField(primary_key=True)
    salary = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=200)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE)

class TeachersStudents(models.Model):
    user_student_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    
