from django.db import models
from rest_framework import serializers


class Task(models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    State = models.CharField(max_length=20)

    def __str__(self):
        return f"< Task ><ID > {self.ID} < /ID ><Title > {self.Title} < /Title ><State > {self.State} < /State ></Task >"

    class Meta:
        db_table = "Task"
        verbose_name = "Task"


class Task_Serializer(serializers.ModelSerializer):
    ID = serializers.IntegerField(read_only=True)
    Title = serializers.CharField(max_length=100)
    State = serializers.CharField(max_length=20)

    class Meta:
        model = Task
        fields = ('ID', 'Title', 'State')


class Transition_Graph:
    def __init__(self):
        self.graph = {'draft': ["active", "archived"], 'active': [
            "archived", "done"], 'done': ["archived"]}

    def is_valid_transition(self, from_state, to_state):
        return to_state in self.graph[from_state]
