from django.db import models

# Create your models here.

class Value(models.Model):
    value_name = models.CharField(max_length = 50)
    value_description = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.value_name


class Goal(models.Model):
    goal_name = models.CharField(max_length = 50)
    values = models.ManyToManyField(Value, related_name='values', blank=False)
    goal_description = models.TextField()
    goal_achieved = models.BooleanField(default = False)
    created_date = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.goal_name

class Task(models.Model):
    task_name = models.CharField(max_length = 100)
    goal = models.ForeignKey(Goal, related_name='goal', blank=False, on_delete=models.CASCADE)
    task_complete = models.BooleanField(default = False)
    created_date = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.task_name


class Tracker(models.Model):
    task = models.ForeignKey(Task, related_name='task', blank=False, on_delete=models.CASCADE)
    positive_tracking = models.BooleanField(default = True)

    counter_enabled = models.BooleanField(default = False)
    counter_word = models.CharField(max_length = 50, blank = True)
    counter = models.IntegerField(blank = True)

    timer_enabled = models.BooleanField(default = False)
    updated_date = models.DateTimeField(auto_now = True)

    created_date = models.DateTimeField(auto_now_add = True)

    notes = models.CharField(max_length = 200)

    class Meta:
        ordering = ('-created_date',)

    # def __str__(self):
    #     return self.task_name
