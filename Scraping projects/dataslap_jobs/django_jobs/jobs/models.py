# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.postgres.fields import ArrayField

#
class AppliedJobs(models.Model):
    applied_id = models.AutoField(primary_key=True)
    job = models.ForeignKey('Jobs', models.DO_NOTHING)
    applied_timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applied_jobs'
#
#
class Companies(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companies'

class Titles(models.Model):
    title_id = models.AutoField(primary_key=True)
    job_title = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titles'
#
#
class Countries(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(unique=True, max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'


class DisplayCompanies(models.Model):
    display_company_id = models.AutoField(primary_key=True)
    display_company_name = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'display_companies'


class DisplayTitles(models.Model):
    display_title_id = models.AutoField(primary_key=True)
    display_job_title = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'display_titles'
#
#
class ExpiredJobs(models.Model):
    expired_id = models.AutoField(primary_key=True)
    job = models.ForeignKey('Jobs', models.DO_NOTHING)
    expired_timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expired_jobs'
#
#
class ExternalUrls(models.Model):
    external_url_id = models.AutoField(primary_key=True)
    external_url = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'external_urls'


class JobDescriptions(models.Model):
    job_description_id = models.AutoField(primary_key=True)
    job_description = models.TextField()

    class Meta:
        managed = False
        db_table = 'job_descriptions'


class Jobs(models.Model):
    job_id = models.AutoField(primary_key=True)
    url = models.ForeignKey('Urls', models.DO_NOTHING)
    external_url = models.ForeignKey(ExternalUrls, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(Companies, models.DO_NOTHING)
    title = models.ForeignKey(Titles, models.DO_NOTHING)
    job_description = models.ForeignKey(JobDescriptions, models.DO_NOTHING)
    location = models.ForeignKey('Locations', models.DO_NOTHING)
    country = models.ForeignKey(Countries, models.DO_NOTHING)
    date_published = models.DateTimeField()
    date_scraped = models.DateTimeField()
    source = models.ForeignKey('Sources', models.DO_NOTHING)
    # # page_source = models.ForeignKey('PageSources', models.DO_NOTHING)
    # # page_external_source = models.ForeignKey('PageExternalSources', models.DO_NOTHING, blank=True, null=True)
    display_company = models.ForeignKey(DisplayCompanies, models.DO_NOTHING, blank=True, null=True)
    display_title = models.ForeignKey(DisplayTitles, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobs'
#
#
class LabeledJobs(models.Model):
    label_id = models.AutoField(primary_key=True)
    job = models.ForeignKey(Jobs, models.DO_NOTHING)
    apply_label = models.NullBooleanField()
    apply_timestamp = models.DateTimeField(blank=True, null=True)
    skill_focus = ArrayField(models.IntegerField(), blank=True, null=True)
    # skill_focus = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'labeled_jobs'
#
#
class Locations(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(unique=True, max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locations'


# class PageExternalSources(models.Model):
#     page_external_source_id = models.AutoField(primary_key=True)
#     page_external_source_text = models.TextField()
#
#     class Meta:
#         managed = False
#         db_table = 'page_external_sources'
#
#
# class PageSources(models.Model):
#     page_source_id = models.AutoField(primary_key=True)
#     page_source_text = models.TextField()
#
#     class Meta:
#         managed = False
#         db_table = 'page_sources'


class SkillFocuses(models.Model):
    skill_id = models.AutoField(primary_key=True)
    skill_label = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'skill_focuses'


class SkillParagraphs(models.Model):
    paragraph_id = models.AutoField(primary_key=True)
    skill = models.ForeignKey(SkillFocuses, models.DO_NOTHING)
    skill_paragraph_text = models.TextField()
    skill_paragraph_added = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skill_paragraphs'


class Sources(models.Model):
    source_id = models.AutoField(primary_key=True)
    source_name = models.CharField(unique=True, max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sources'





class Urls(models.Model):
    url_id = models.AutoField(primary_key=True)
    url = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'urls'
