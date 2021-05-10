from datetime import date

from cources_framework4.templator import render_to_templ
from patterns.cp import Engine, Logger

site = Engine()
logger = Logger('main')


class Index:
    def __call__(self, request):
        return '200 OK', render_to_templ('index.html', objects_list=site.categories)

# schedule
class TablePrograms:
    def __call__(self, request):
        return '200 OK', render_to_templ('first.html', data=date.today())


class About:
    def __call__(self, request):
        return '200 OK', render_to_templ('about.html', data=request.get('data', None))


class Reg:
    def __call__(self, request):
        return '200 OK', render_to_templ('regs.html', data=request.get('data', None))


class Cont1:
    def __call__(self, request):
        return '200 OK', render_to_templ('cont_1.html', data=request.get('data', None))



class NotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'


# ���������� - ������ ������
class CoursesList:
    def __call__(self, request):
        logger.log('list course')
        print(f'==============={request}')
        try:
            category = site.find_category_by_id(int(request['request_params']['id']))
            return '200 OK', render_to_templ('course_list.html', objects_list=category.courses, name=category.name, id=category.id)
        except KeyError:
            return '200 OK', 'No courses have been added yet'


# ���������� - ������� ����
class CreateCourse:
    category_id = -1

    def __call__(self, request):
        if request['method'] == 'POST':
            # ����� ����
            data = request['data']

            name = data['name']
            name = site.decode_value(name)

            category = None
            if self.category_id != -1:
                category = site.find_category_by_id(int(self.category_id))

                course = site.create_course('record', name, category)
                site.courses.append(course)

            return '200 OK', render_to_templ('course_list.html', objects_list=category.courses,
                                    name=category.name, id=category.id)

        else:
            try:
                self.category_id = int(request['request_params']['id'])
                category = site.find_category_by_id(int(self.category_id))

                return '200 OK', render_to_templ('create_course.html', name=category.name, id=category.id)
            except KeyError:
                return '200 OK', 'No categories have been added yet'


# ���������� - ������� ���������
class CreateCategory:
    def __call__(self, request):
        print('Created new category!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

        if request['method'] == 'POST':
            # ����� ����
            print('Created new POST....................................................')
            print(f'******************{request}')
            data = request['data']
            print(f'Created new data {type(data)}==----------------..---------------..---------------..==')

            name = data['name']
            name = site.decode_value(name)
            print(f'name =========================> {name}')

            category_id = data.get('category_id')

            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))

            new_category = site.create_category(name, category)

            site.categories.append(new_category)

            return '200 OK', render_to_templ('index.html', objects_list=site.categories)
        else:
            categories = site.categories
            return '200 OK', render_to_templ('create_category.html', categories=categories)


# ���������� - ������ ���������
class CategoryList:
    def __call__(self, request):
        logger.log('list category')
        return '200 OK', render_to_templ('category_list.html', objects_list=site.categories)


# ���������� - ���������� ����
class CopyCourse:
    def __call__(self, request):
        request_params = request['request_params']

        try:
            name = request_params['name']
            old_course = site.get_course(name)
            if old_course:
                new_name = f'copy_{name}'
                new_course = old_course.clone()
                new_course.name = new_name
                site.courses.append(new_course)

            return '200 OK', render_to_templ('course_list.html', objects_list=site.courses)
        except KeyError:
            return '200 OK', 'No courses have been added yet'
