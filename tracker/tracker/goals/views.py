from django.shortcuts import render
from .models import Value, Goal, Task
from .forms import ValueForm
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework import generics

# from django.core.urlresolvers import reverse
from django.views.generic import RedirectView
from django.urls import reverse

from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

from . import models
from . import serializers
from rest_framework import generics

# Create your views here.

# @method_decorator(ensure_csrf_cookie, name = "post")
class ValueValue(View):
    def get(self, request):
        # params = dict()
        #
        # form = ValueForm()
        # params["form"] = form
        #
        # values = Value.objects.all()
        # params["values"] = values

        return render(request, "base.html")

    # def post(self, request):
    #     form = ValueForm(self.request.POST)
    #     if form.is_valid():
    #         if not Value.objects.filter(value_name=form.cleaned_data["value_name"]).exists():
    #             value = Value(value_name = form.cleaned_data["value_name"],
    #                             value_description = form.cleaned_data["value_description"])
    #             value.save()
    #
    #     return HttpResponseRedirect("/")


class ListValue(generics.ListAPIView):
    queryset = models.Value.objects.all()
    serializer_class = serializers.ValueSerializer

class ValueDetail(APIView):
    def get_object(self, pk):
        try:
            return Value.objects.get(pk=pk)
        except Value.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = serializers.ValueSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = serializers.ValueSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        # print(request.data)
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ValueAdd(APIView):
    def get_object(self, pk):
        try:
            return Value.objects.get(pk=pk)
        except Value.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        serializer = serializers.ValueSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class BatchEdit(APIView):
    def post(self, request, format=None):
        Value.objects.filter(value_name=request.data["value_name"]).\
                        update(value_name=request.data["edit_entry"])
        # serializer = serializers.ValueSerializer(values, many=True)
        # return Response(serializer.data)

        # serializer = serializers.ValueSerializer(pew, data=request.data)
        # if serializer.is_valid():
        #     return Response(serializer.data)
        # print(request.data["value_name"])
        # pew = Value.objects.filter(value_name=request.data.value_name)
        # serializer = serializers.ValueSerializer(pew, data=request.data)
        # # .update(name="foo")
        #
        # return Response(serializer.data)
        # {"value_name": "PEW", "edit_entry" : "PEWPEW"}



class RedirectToHome(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('home')
#
# from django.views.decorators.csrf import csrf_exempt
# @method_decorator(csrf_exempt, name='dispatch')
class ListGoal(generics.ListCreateAPIView):
    queryset = models.Goal.objects.all()
    serializer_class = serializers.ListGoalSerializer
    filter_fields = ('values__id',)

class AddGoal(generics.ListCreateAPIView):
    queryset = models.Goal.objects.all()
    serializer_class = serializers.AddGoalSerializer

class DetailGoal(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Goal.objects.all()
    serializer_class = serializers.AddGoalSerializer

###########
# from django_filters.rest_framework import SearchFilter

class ListTask(generics.ListCreateAPIView):
    queryset = models.Task.objects.all()
    serializer_class = serializers.ListTaskSerializer
    filter_fields = ('goal__id',)
    # def get_queryset(self):
    #     goal_id = self.kwargs['goal']
    #     return models.Task.objects.filter(goal__id=goal_id)

class AddTask(generics.ListCreateAPIView):
    queryset = models.Task.objects.all()
    serializer_class = serializers.AddTaskSerializer

class DetailTask(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Task.objects.all()
    serializer_class = serializers.AddTaskSerializer

###########

class ListTracker(generics.ListCreateAPIView):
    queryset = models.Tracker.objects.all()
    serializer_class = serializers.ListTrackerSerializer
    filter_fields = ('task__id',)

class AddTracker(generics.ListCreateAPIView):
    queryset = models.Tracker.objects.all()
    serializer_class = serializers.AddTrackerSerializer

class DetailTracker(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Tracker.objects.all()
    serializer_class = serializers.AddTrackerSerializer
