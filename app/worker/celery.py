# from celery import Celery

# from app import config as conf

# celery_worker = Celery(
#     "tasks",
#     broker=conf.redis_url_celery(),
#     include=["app.tasks.tasks",],
# )

# if __name__ == '__main__':
#     celery_worker.start()
