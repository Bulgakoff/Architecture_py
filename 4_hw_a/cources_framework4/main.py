import quopri

from icecream import ic

from cources_framework4.requests import GetRequests, PostRequests


class PageNotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'


class Framework:
    """Класс Framework - основа фреймворка"""

    def __init__(self, routes_obj, fronts_obj):
        self.routes_lst = routes_obj
        self.fronts_lst = fronts_obj

    def __call__(self, environ, start_response):
        # получаем адрес, по которому выполнен переход
        path = environ['PATH_INFO']

        # добавление закрывающего слеша
        if not path.endswith('/'):
            path = f'{path}/'

        request = {}
        # Получаем все данные запроса
        method = environ['REQUEST_METHOD']
        request['method'] = method
        ic(method) # GET or POST

        if method == 'POST':
            # ic(environ)
            data = PostRequests().get_request_params(environ)  #: return py dict
            request['data'] = data
            ic(f'Нам пришёл post-запрос: {Framework.decode_value(data)}')
            # print(f'Нам пришёл post-запрос: {data}')
            ic(request)
            # {'name': 'qwe', 'email': 'qaz%40mail.com', 'location': 'ny'}
            ic(type(data)) # <class 'dict'>
        if method == 'GET':
            request_params = GetRequests().get_request_params(environ) #: dict
            request['request_params'] = request_params
            #writen for GET: ?id=1&category=10
            ic(f'Нам пришли GET-параметры: {request_params}')
            # request_params= {'id': '1', 'category': '10'}

        # находим нужный контроллер
        # отработка паттерна page controller
        if path in self.routes_lst:
            view = self.routes_lst[path]
        else:
            view = PageNotFound404()
        # request = {}
        # наполняем словарь request элементами
        # этот словарь получат все контроллеры
        # отработка паттерна front controller
        for front in self.fronts_lst:
            front(request)
        print(f'+++from 4_hw-a+++++++++++++{request}')
        # запуск контроллера с передачей объекта request
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    @staticmethod
    def decode_value(data) -> dict:
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = quopri.decodestring(val).decode('UTF-8')
            new_data[k] = val_decode_str
        return new_data
