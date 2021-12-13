from django.test import TestCase
import requests
from queue import Queue

from .models import Transition_Graph


class TestTaskApi(TestCase):
    def setUp(self):
        self.base = 'http://localhost:8000/'

    def test_create_task(self):
        """
        Test the creation of a task
        """
        res = requests.post(self.base + 'create_task/',
                            data={'task_title': 'test task'})
        self.assertEqual(res.status_code, 200)

    def test_get_task(self):
        """
        Test the get task view
        """
        task_id = requests.post(self.base + 'create_task/',
                                data={'task_title': 'test task'}).json()['task_id']

        res = requests.get(self.base + 'get_task/' + str(task_id))
        self.assertEqual(res.status_code, 200)

    def test_update_task_name(self):
        """
        Test the update task name view
        """
        task_id = requests.post(self.base + 'create_task/',
                                data={'task_title': 'test task'}).json()['task_id']
        res = requests.post(self.base + 'update_task_name/',
                            data={'task_title': 'new name', 'task_id': task_id})
        res = requests.get(self.base + 'get_task/' + str(task_id))

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()['task']['Title'], 'new name')

    def test_transitions(self):
        """
        Test the transitions of the task state

        Bfs through the graph and check that the transitions are correct

        The algorihm assumes that the graph is a DAG
        """
        transition_graph = Transition_Graph()
        task_id = requests.post(self.base + 'create_task/',
                                data={'task_title': 'test task'}).json()['task_id']
        Q = Queue(len(transition_graph.graph.keys()))
        Q.put("draft")

        while not Q.empty():
            curent_state = Q.get()
            for transition in transition_graph.graph[curent_state]:
                res = requests.post(self.base + 'update_task_state/', data={
                    'task_id': task_id, 'state': transition})
                self.assertEqual(res.status_code, 200)
                Q.put(transition)
