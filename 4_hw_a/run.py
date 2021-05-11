from wsgiref.simple_server import make_server

from simba_framework44.main import Framework
from urls import routes, fronts


application = Framework(routes, fronts)

with make_server('', 8080, application) as httpd:
    print("Запуск на порту 8080 qwe4444...")
    httpd.serve_forever()
