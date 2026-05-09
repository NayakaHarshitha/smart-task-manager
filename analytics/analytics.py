def task_analytics(tasks):

    total_tasks = len(tasks)

    completed_tasks = len(
        [task for task in tasks if task.status == "Completed"]
    )

    pending_tasks = len(
        [task for task in tasks if task.status == "Pending"]
    )

    if total_tasks > 0:

        completion_percentage = round(
            (completed_tasks / total_tasks) * 100,
            2
        )

    else:

        completion_percentage = 0

    return {

        "total_tasks": total_tasks,

        "completed_tasks": completed_tasks,

        "pending_tasks": pending_tasks,

        "completion_percentage": completion_percentage
    }