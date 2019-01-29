from rest_framework import serializers
from goals.models import Value ,Goal, Task, Tracker


class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'value_name',
            'value_description',
            'created_date',
        )
        model = Value


class SmallValueSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'value_name'
        )
        model = Value

class MinimalValueSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
        )
        model = Value

class SmallGoalSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'goal_name'
        )
        model = Goal

class MinimalGoalSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
        )
        model = Goal

class AddGoalSerializer(serializers.ModelSerializer):
    # values = MinimalValueSerializer(many=True)
    values = serializers.PrimaryKeyRelatedField(queryset=Value.objects.all(), many=True)
    # values = MinimalValueSerializer(many=True)
    class Meta:
        fields = (
            'id',
            'goal_name',
            'values',
            'goal_description',
            'created_date',
        )
        model = Goal

class ListGoalSerializer(serializers.ModelSerializer):
    values = SmallValueSerializer(many=True)
    class Meta:
        fields = (
            'id',
            'goal_name',
            'values',
            'goal_description',
            'created_date',
        )
        model = Goal


class NewGoalSerializer(serializers.ModelSerializer):
    values = SmallValueSerializer(many=False)
    class Meta:
        fields = (
            'id',
            'goal_name',
            'values',
            'goal_description',
            'goal_achieved',
            'created_date',
        )
        model = Goal

##############################################

class SmallTaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'goal_name'
        )
        model = Task

class MinimalTaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
        )
        model = Task

class AddTaskSerializer(serializers.ModelSerializer):
    # values = MinimalValueSerializer(many=True)
    goal = serializers.PrimaryKeyRelatedField(queryset=Goal.objects.all())
    # goal = MinimalTaskSerializer()
    class Meta:
        fields = (
            'id',
            'task_name',
            'goal',
            'task_complete',
            'created_date',
        )
        model = Task

class ListTaskSerializer(serializers.ModelSerializer):
    goal = SmallGoalSerializer()
    class Meta:
        fields = (
            'id',
            'task_name',
            'goal',
            'task_complete',
            'created_date',
        )
        model = Task


class NewTaskSerializer(serializers.ModelSerializer):
    goal = SmallGoalSerializer()
    class Meta:
        fields = (
            'id',
            'task_name',
            'goal',
            'task_complete',
            'created_date',
        )
        model = Task


##############################################

class AddTrackerSerializer(serializers.ModelSerializer):
    # values = MinimalValueSerializer(many=True)
    task = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all())
    # goal = MinimalTaskSerializer()
    class Meta:
        fields = (
            'id',
            'counter_enabled',
            'counter_word',
            'counter',
            'timer_enabled',
            'updated_date',
            'created_date',
            'notes'
        )
        model = Tracker


class ListTrackerSerializer(serializers.ModelSerializer):
    task = SmallTaskSerializer()
    class Meta:
        fields = (
            'id',
            'counter_enabled',
            'counter_word',
            'counter',
            'timer_enabled',
            'updated_date',
            'created_date',
            'notes'
        )
        model = Tracker


class NewTrackerSerializer(serializers.ModelSerializer):
    task = SmallTaskSerializer()
    class Meta:
        fields = (
            'id',
            'counter_enabled',
            'counter_word',
            'counter',
            'timer_enabled',
            'updated_date',
            'created_date',
            'notes'
        )
        model = Tracker
