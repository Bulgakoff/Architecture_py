from datetime import date
from views import Index, About, StudyPrograms, CoursesList, \
    CreateCourse, CreateCategory, CategoryList, \
    CopyCourse, Reg, Cont1


# front controller
def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

# routes = {
    # '/': Index(),
    # '/about/': About(),
    # '/table/': StudyPrograms(),
    # '/reg/': Reg(),
    # '/conta/': Cont1(),
    # '/courses-list/': CoursesList(),
    # '/create-course/': CreateCourse(),
    # '/create-category/': CreateCategory(),
    # '/category-list/': CategoryList(),
    # '/copy-course/': CopyCourse()
# }
