from django.shortcuts import render

from .models import Task, Transition_Graph


def create_task(request):
    if request.method == 'POST':
        task_name = request.POST.get('task_title')
        task = Task(
            task_name=task_name,
            State="draft",
        )
        task.save()
        return json_response({"success": True, "task_id": task.id})
    else:
        return json_response({"success": False})


def get_task(request):
    if request.method != 'GET':
        return json_response({"success": False})
    task_id = request.GET.get('task_id')
    valid_task = Task.objects.filter(id=task_id).exists()
    if not valid_task:
        return json_response({"success": False})

    task = Task.objects.get(id=task_id)
    serializer = Task_Serializer(task)
    return json_response({"success": True, "task": serializer.data})


def update_task_name(request):
    if request.method != 'POST':
        return json_response({"success": False})

    task_id = request.POST.get('task_id')
    valid_task = Task.objects.filter(id=task_id).exists()
    if not valid_task:
        return json_response({"success": False})
    task = Task.objects.get(id=task_id)
    task.task_name = request.POST.get('task_name')
    task.save()
    return json_response({"success": True})


def update_task_state(request):
    if request.method != 'POST':
        return json_response({"success": False})

    task_id = request.POST.get('task_id')
    valid_task = Task.objects.filter(id=task_id).exists()

    if not valid_task:
        return json_response({"success": False})

    task = Task.objects.get(id=task_id)
    from_state = task.State
    to_state = request.POST.get('to_state')
    transition_graph = Transition_Graph()
    if transition_graph.is_valid_transition(from_state, to_state):
        task.State = to_state
        task.save()
        return json_response({"success": True})
    else:
        return json_response({"success": False})


def delete_task(request):
    if request.method != 'POST':
        return json_response({"success": False})

    task_id = request.POST.get('task_id')
    valid_task = Task.objects.filter(id=task_id).exists()

    if not valid_task:
        return json_response({"success": False})

    task = Task.objects.get(id=task_id)
    task.delete()
    return json_response({"success": True})
