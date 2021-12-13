from .models import Transition_Graph
# Create your tests here.

import requests

base = base + ''


def test_create_task():
    """
    Test the creation of a task
    """
    res = requests.post(base + 'create_task/',
                        data={'task_title': 'test task'})
    assert res.status_code == 200


def test_get_task():
    """
    Test the get task view
    """
    task_id = requests.post(base + 'create_task/',
                            data={'task_title': 'test task'}).json()['task_id']

    res = requests.get(base + 'get_task/' + str(task_id))
    assert res.status_code == 200


def test_update_task_name():
    """
    Test the update task name view
    """
    task_id = requests.post(base + 'create_task/',
                            data={'task_title': 'test task'}).json()['task_id']
    res = requests.post(base + 'update_task_name/',
                        data={'task_title': 'new name', 'task_id': task_id})
    res = requests.get(base + 'get_task/' + str(task_id))

    assert res.status_code == 200
    assert res.json()['task_title'] == 'new name'


def test_transitions():
    """
    Test the transitions of the task state
    """
    transition_graph = Transition_Graph()
    task_id = requests.post(base + 'create_task/',
                            data={'task_title': 'test task'}).json()['task_id']
    old_state = 'draft'

    for state in transition_graph.graph:
        for new_state in transition_graph.graph:
            res = requests.post(
                base + 'update_task_state/', data={'to_state': new_state})
            assert res.status_code == 200 if transition_graph.is_valid_transition(
                old_state, new_state) else 400
            old_state = new_state


print(res.json())
