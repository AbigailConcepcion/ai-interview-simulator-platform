from celery import Celery

celery = Celery("tasks", broker="redis://redis:6379/0")

@celery.task
def score_answer(answer):
    return len(answer)
