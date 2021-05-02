from datetime import date
from views import Index, About, Cont


# front controller
def secret_front(request):
    request['data'] = date.today()


def other_front(request):
    request['key'] = 'key'

def strange_front(request):
    request['my_key'] = 'my_key'
fronts = [secret_front, other_front, strange_front]


routes = {
    '/': Index(),
    '/about/': About(),
    '/cont/': Cont(),
}
