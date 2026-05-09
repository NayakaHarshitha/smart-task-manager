import pandas as pd
import numpy as np


def task_analytics(tasks):

    task_data = []

    for task in tasks:

        task_data.append({
            'status': task.status
        })

    df = pd.DataFrame(task_data)

    total_tasks = len(df)

    completed_tasks = len(
        df[df['status'] == 'Completed']
    ) if total_tasks > 0 else 0

    pending_tasks = len(
        df[df['status'] == 'Pending']
    ) if total_tasks > 0 else 0

    completion_percentage = np.round(
        (completed_tasks / total_tasks) * 100,
        2
    ) if total_tasks > 0 else 0

    return {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'completion_percentage': completion_percentage
    }