from django.shortcuts import render
from django.views.generic import View
from django.core import serializers
# from .models import Companies, Jobs, LabeledJobs
from .models import *
from .serializers import *

import json
from django.http import JsonResponse
from django.forms.models import model_to_dict
from datetime import date


from rest_framework.views import APIView
from rest_framework import generics

from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

from datetime import datetime,tzinfo,timedelta
from pytz import timezone

# from django.utils import simplejson
# import jsonpickle
# def to_dict(instance):
#   opts = instance._meta
#   data = {}
#   for f in opts.concrete_fields + opts.many_to_many:
#       data[f.name] = f.value_from_object(instance)
#   return data

# Create your views here.

class Index(View):
    def get(self, request):
        return render(request, "base.html")


class Index2(View):
   def get(self, request):
       params = {}
       # companies = Companies.objects.all()
       labeled_jobs = list(LabeledJobs.objects.all().values_list('job', flat=True))
       expired_jobs = list(ExpiredJobs.objects.all().values_list('job', flat=True))
       jobs = Jobs.objects.exclude(job_id__in=labeled_jobs).\
                            exclude(job_id__in=expired_jobs).\
                            select_related('company').\
                            select_related('title').\
                            select_related('url').\
                            select_related('external_url').\
                            select_related('location').\
                            select_related('country').\
                            select_related('source').\
                            select_related('display_company').\
                            select_related('display_title').\
                            all()
       # jobs = Jobs.objects.count()
       # jobs = jobs.company.company_name
       # Jobs.objects.select_related('company').select_related('title').all()


       # jobs = model_to_dict(jobs)
       # jobs = list(map(lambda x:model_to_dict(x), jobs))
       # jobs = list(map(lambda x: to_dict(x), jobs))





       jobs = list(map(lambda x:
###IDS
                {'job_id':               (lambda y: x.job_id)(x),
                'company_id':            (lambda y: x.company.company_id)(x),
                'title_id':              (lambda y: x.title.title_id)(x),
                'url_id':                (lambda y: x.url.url_id)(x),
                'external_url_id':       (lambda y: x.external_url.external_url_id if x.external_url is not None else None)(x),
                'location_id':           (lambda y: x.location.location_id)(x),
                'country_id':            (lambda y: x.country.country_id)(x),
                'source_id':             (lambda y: x.source.source_id)(x),
                'display_company_id':    (lambda y: x.display_company.display_company_id if x.display_company is not None else None)(x),
                'display_title_id':      (lambda y: x.display_title.display_title_id if x.display_title is not None else None)(x),
### ACTUAL FIELDS
                'company_name':          (lambda y: x.company.company_name)(x),
                'job_title':             (lambda y: x.title.job_title)(x),
                'url':                   (lambda y: x.url.url)(x),
                'external_url':          (lambda y: x.external_url.external_url if x.external_url is not None else None)(x),
                'location_name':         (lambda y: x.location.location_name)(x),
                'country_name':          (lambda y: x.country.country_name)(x),
                'source_name':           (lambda y: x.source.source_name)(x),
                'display_company_name':  (lambda y: x.display_company.display_company_name if x.display_company is not None else None)(x),
                'display_job_title':     (lambda y: x.display_title.display_job_title if x.display_title is not None else None)(x),
                'date_published':        (lambda y: x.date_published)(x).strftime("%B %d, %Y"),
                'date_scraped':          (lambda y: x.date_scraped)(x).strftime("%B %d, %Y")}, jobs))

                # (lambda x: x.date_scraped, if "date_published" in dir(x))


       # params["companies"] = jsonpickle.encode(jobs)
       params["companies"] = jobs
       # json_data = params

       ###### WORKING ID SERIALIZER
       # JSON_Serializer = serializers.get_serializer("json")
       # json_serializer = JSON_Serializer()
       # json_serializer.serialize(jobs)
       # data = json_serializer.getvalue()
       #######


       # data = serializers.serialize('json', jobs)
       # return render(request, 'base.html', json.dumps(jobs))
       # return render(request, 'base.html', params)
       return render(request, 'base.html', {"json_data": json.dumps(jobs)})
       # return JsonResponse({'json_data': data })
       # return JsonResponse(jobs, safe = False)


class AllJobs(APIView):
    def get(self, request):
        labeled_jobs = list(LabeledJobs.objects.all().values_list('job', flat=True))
        expired_jobs = list(ExpiredJobs.objects.all().values_list('job', flat=True))
        jobs = Jobs.objects.exclude(job_id__in=labeled_jobs).\
                             exclude(job_id__in=expired_jobs).\
                             select_related('company').\
                             select_related('title').\
                             select_related('url').\
                             select_related('external_url').\
                             select_related('location').\
                             select_related('country').\
                             select_related('source').\
                             select_related('display_company').\
                             select_related('display_title').\
                             all()

        jobs = list(map(lambda x:
  ###IDS
                  {'job_id':               (lambda y: x.job_id)(x),
                  'company_id':            (lambda y: x.company.company_id)(x),
                  'title_id':              (lambda y: x.title.title_id)(x),
                  'url_id':                (lambda y: x.url.url_id)(x),
                  'external_url_id':       (lambda y: x.external_url.external_url_id if x.external_url is not None else None)(x),
                  'location_id':           (lambda y: x.location.location_id)(x),
                  'country_id':            (lambda y: x.country.country_id)(x),
                  'source_id':             (lambda y: x.source.source_id)(x),
                  'display_company_id':    (lambda y: x.display_company.display_company_id if x.display_company is not None else None)(x),
                  'display_title_id':      (lambda y: x.display_title.display_title_id if x.display_title is not None else None)(x),
  ### ACTUAL FIELDS
                  'company_name':          (lambda y: x.company.company_name)(x),
                  'job_title':             (lambda y: x.title.job_title)(x),
                  'url':                   (lambda y: x.url.url)(x),
                  'external_url':          (lambda y: x.external_url.external_url if x.external_url is not None else None)(x),
                  'location_name':         (lambda y: x.location.location_name)(x),
                  'country_name':          (lambda y: x.country.country_name)(x),
                  'source_name':           (lambda y: x.source.source_name)(x),
                  'display_company_name':  (lambda y: x.display_company.display_company_name if x.display_company is not None else None)(x),
                  'display_job_title':     (lambda y: x.display_title.display_job_title if x.display_title is not None else None)(x),
                  'date_published':        (lambda y: x.date_published)(x).strftime("%B %d, %Y"),
                  'date_scraped':          (lambda y: x.date_scraped)(x).strftime("%B %d, %Y")}, jobs))

        return Response(jobs)
        # return Response(json.dumps(jobs))


class Index(View):
    def get(self, request):
        return render(request, "base.html")


class TitleLabelGetCreate(APIView):
    def get_object(self, request):
        try:
            return DisplayTitles.objects.get(display_job_title=request.data["display_job_title"])
        except DisplayTitles.DoesNotExist:
            raise Http404
    def post(self, request):
        item = self.get_object(request)
        serializer = DisplayTitlesSerializer(item)
        return Response(serializer.data)




    # def get(self, request, format=None):
    #     queryset = DisplayTitles.objects.all()
    #     serializer = DisplayTitlesSerializer(queryset, many=True)
    #     return Response(serializer.data)

class CompanyLabelGetCreate(APIView):
    def get_object(self, request):
        try:
            return DisplayCompanies.objects.get(display_company_name=request.data["display_company_name"])
        except DisplayCompanies.DoesNotExist:
            raise Http404
    def post(self, request):
        item = self.get_object(request)
        serializer = DisplayCompaniesSerializer(item)
        return Response(serializer.data)



class SkillsGet(APIView):
    def get(self, request, format=None):
        queryset = SkillFocuses.objects.all()
        serializer = SkillFocusesSerializer(queryset, many=True)
        return Response(serializer.data)


    # def get(self, request, format=None):
    #     queryset = DisplayTitles.objects.all()
    #     serializer = DisplayTitlesSerializer(queryset, many=True)
    #     return Response(serializer.data)

class ExpireJob(APIView):
    def post(self, request):
        request.data["expired_timestamp"] = datetime.now(timezone('US/Eastern'))
        serializer = ExpiredJobsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LabelJob(APIView):
    def post(self, request):
        request.data["apply_timestamp"] = datetime.now(timezone('US/Eastern'))
        serializer = LabeledJobsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#
class TitleGet(APIView):
    def get(self, request, format=None):
        queryset = Titles.objects.all()
        serializer = TitlesSerializer(queryset, many=True)
        return Response(serializer.data)


class CompanyGet(APIView):
    def get(self, request, format=None):
        queryset = Companies.objects.all()
        serializer = CompaniesSerializer(queryset, many=True)
        return Response(serializer.data)
#
#
# class ValidateEntry(APIView):
#     def post(self, request, format=None):
#         entry = request.data
#         # company_label_entry = Entry.objects.get(pk=123)
#         if DisplayCompanies.objects.filter(display_company_name = entry["display_company_name"]).exists():
#             display_company_id = DisplayCompanies.objects.\
#                                         get(display_company_name=entry["display_company_name"]).\
#                                         display_company_id
#         else:
#             new_display_company_entry = DisplayCompanies(display_company_name=entry["display_company_name"])
#             new_display_company_entry.save()
#             display_company_id = new_display_company_entry.display_company_id
#
#         Jobs.objects.filter(company=request.data["company_name"]).\
#                         update(display_company=display_company_id)
#
#         if DisplayTitles.objects.filter(display_job_title = entry["display_job_title"]).exists():
#             display_title_id = DisplayTitles.objects.\
#                                         get(display_job_title=entry["display_job_title"]).\
#                                         display_title_id
#         else:
#             new_display_title_entry = DisplayTitles(display_job_title=entry["display_job_title"])
#             new_display_title_entry.save()
#             display_title_id = new_display_title_entry.display_title_id
#
#         Jobs.objects.filter(title=request.data["job_title46"]).\
#                         update(display_company=display_company_id)
