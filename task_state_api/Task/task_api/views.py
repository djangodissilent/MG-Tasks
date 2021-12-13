from django.http import JsonResponse

from .models import Task, Transition_Graph
from .models import Task_Serializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def create_task(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST method required'}, status=400)

    task_name = request.POST.get('task_title')
    task = Task(
        Title=task_name,
        State="draft",
    )
    task.save()
    return JsonResponse({"success": True, "task_id": task.ID})


@csrf_exempt
def get_task(request, task_id):
    if request.method != 'GET':
        return JsonResponse({"success": False})
    valid_task = Task.objects.filter(ID=task_id).exists()
    if not valid_task:
        return JsonResponse({"success": False})

    task = Task.objects.get(ID=task_id)
    serializer = Task_Serializer(task)
    return JsonResponse({"success": True, "task": serializer.data})


@csrf_exempt
def update_task_name(request):
    if request.method != 'POST':
        return JsonResponse({"success": False})

    task_id = request.POST.get('task_id')
    valid_task = Task.objects.filter(ID=task_id).exists()
    if not valid_task:
        return JsonResponse({"success": False})
    task = Task.objects.get(ID=task_id)
    task.Title = request.POST.get('task_title')
    task.save()
    return JsonResponse({"success": True})


@csrf_exempt
def update_task_state(request):
    if request.method != 'POST':
        return JsonResponse({"success": False})

    task_id = request.POST.get('task_id')
    valid_task = Task.objects.filter(ID=task_id).exists()

    if not valid_task:
        return JsonResponse({"success": False})

    task = Task.objects.get(ID=task_id)
    from_state = task.State
    to_state = request.POST.get('to_state')
    transition_graph = Transition_Graph()
    if transition_graph.is_valid_transition(from_state, to_state):
        task.State = to_state
        task.save()
        return JsonResponse({"success": True})
    else:
        return JsonResponse({"success": False})


@csrf_exempt
def delete_task(request):
    if request.method != 'POST':
        return JsonResponse({"success": False})

    task_id = request.POST.get('task_id')
    valid_task = Task.objects.filter(ID=task_id).exists()

    if not valid_task:
        return JsonResponse({"success": False})

    task = Task.objects.get(ID=task_id)
    task.delete()
    return JsonResponse({"success": True})
