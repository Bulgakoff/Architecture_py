# get requests
from icecream import ic


class GetRequests:

    @staticmethod
    def str_to_dict_parse_input_data(data: str) -> dict:
        result = {}
        if data:
            # делим параметры через &
            params = data.split('&')
            for item in params:
                # делим ключ и значение через =
                k, v = item.split('=')
                result[k] = v
        return result  #: dict

    @staticmethod
    def get_request_params(environ) -> dict:
        # получаем параметры запроса
        ic(type(environ))  #: <class 'dict'>
        query_string = environ['QUERY_STRING']
        ic(type(query_string))  #: <class 'str'>
        ic(query_string)  # query_string: 'id=1&category=10'
        # превращаем параметры в словарь
        request_params = GetRequests.str_to_dict_parse_input_data(query_string)
        return request_params  #: dict


# post requests
class PostRequests:

    @staticmethod
    def parse_input_data(data: str) -> dict:
        result = {}
        if data:
            # делим параметры через &
            params = data.split('&')
            for item in params:
                # делим ключ и значение через =
                k, v = item.split('=')
                result[k] = v
        return result

    @staticmethod
    def get_wsgi_input_data(env) -> bytes:  # return bytes
        # получаем длину тела
        content_length_data = env.get('CONTENT_LENGTH')
        ic(content_length_data) # 43
        # приводим к int
        content_length = int(content_length_data) if content_length_data else 0
        # считываем данные, если они есть
        data = env['wsgi.input'].read(content_length) if content_length > 0 else b'' # b''
        return data

    def parse_wsgi_input_data(self, data: bytes) -> dict:
        result = {}
        if data:
            # декодируем данные
            data_str = data.decode(encoding='utf-8')
            ic(data_str) # data_str: 'name=qwe&email=hlbu%40yandex.ru&location=ny'
            # собираем их в словарь
            result = self.parse_input_data(data_str)
        return result

    def get_request_params(self, environ) -> dict:
        # получаем данные
        data = self.get_wsgi_input_data(environ)  # b''
        # превращаем данные в словарь
        data = self.parse_wsgi_input_data(data)  #: dict
        return data  #: dict
