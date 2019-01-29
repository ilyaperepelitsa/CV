from rest_framework import serializers
from jobs.models import *

class AppliedJobsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'applied_id',
            'job',
            'applied_timestamp'
        )
        model = AppliedJobs


class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'company_id',
            'company_name'
        )
        model = Companies

class TitlesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'title_id',
            'job_title'
        )
        model = Titles


class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'country_id',
            'country_name'
        )
        model = Countries

class DisplayCompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'display_company_id',
            'display_company_name'
        )
        model = DisplayCompanies


class DisplayTitlesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'display_title_id',
            'display_job_title'
        )
        model = DisplayTitles


class ExpiredJobsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'expired_id',
            'job',
            'expired_timestamp'
        )
        model = ExpiredJobs


class ExternalSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'external_url_id',
            'external_url'
        )
        model = ExternalUrls


class JobDescriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'job_description_id',
            'job_description'
        )
        model = JobDescriptions



class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'job_id',
            'url',
            'external_url',
            'company',
            'title',
            'job_description',
            'location',
            'country',
            'date_published',
            'date_scraped',
            'source',
            'display_company',
            'display_title',
        )
        model = Jobs



class LabeledJobsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'label_id',
            'job',
            'apply_label',
            'apply_timestamp',
            'skill_focus'
        )
        model = LabeledJobs


class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'location_id',
            'location_name'
        )
        model = Locations


class SkillFocusesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'skill_id',
            'skill_label'
        )
        model = SkillFocuses



class SkillParagraphsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'paragraph_id',
            'skill',
            'skill_paragraph_text',
            'skill_paragraph_added',
        )
        model = SkillParagraphs


class SourcesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'source_id',
            'source_name'
        )
        model = Sources

class UrlsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'url_id',
            'url'
        )
        model = Urls
