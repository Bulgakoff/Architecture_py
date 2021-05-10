from datetime import date
from views import TablePrograms, About, Reg, Cont1, Index, \
    CreateCategory, CoursesList, CreateCourse, CategoryList, CopyCourse


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
    '/table/': TablePrograms(),
    '/about/': About(),
    '/reg/': Reg(),
    '/conta/': Cont1(),
    '/courses-list/': CoursesList(),
    '/create-course/': CreateCourse(),
    '/create-category/': CreateCategory(),
    '/category-list/': CategoryList(),
    '/copy-course/': CopyCourse(),
}
