import multiprocessing

# bind = "127.0.0.1:8000"
bind = "0.0.0.0:8089"
workers = multiprocessing.cpu_count() * 2 + 1
wsgi_app = "search_operation.wsgi"
accesslog = "./info.log"
errorlog = "./error.log"