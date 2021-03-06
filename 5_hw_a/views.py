from datetime import date

from icecream import ic

from simba_framework44.templator import render_to_template
from patterns.сreational_patterns import Engine, Logger
from patterns.structural_patterns import AppRoute, Debug

site = Engine()
logger = Logger('main')

routes = {}

# контроллер - главная страница
@AppRoute(routes=routes, url='/')
class Index:
    @Debug(name='Index')
    def __call__(self, request):
        return '200 OK', render_to_template('index.html', objects_list=site.categories)


# контроллер "О проекте"
@AppRoute(routes=routes,url= '/about/')
class About:
    @Debug(name='About')
    def __call__(self, request):
        return '200 OK', render_to_template('about.html')

@AppRoute(routes=routes,url='/reg/')
class Reg:
    @Debug(name='Reg')
    def __call__(self, request):
        return '200 OK', render_to_template('regs.html', data=request.get('data', None))

# контролер контактов
@AppRoute(routes=routes,url='/conta/')
class Cont1:
    @Debug(name='Cont1')
    def __call__(self, request):
        return '200 OK', render_to_template('cont_1.html', data=request.get('data', None))


# контроллер - Расписания
@AppRoute(routes=routes,url='/table/')
class StudyPrograms:
    @Debug(name='StudyPrograms')
    def __call__(self, request):
        return '200 OK', render_to_template('table_prog.html', data=date.today())


# контроллер 404
class NotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'


# контроллер - список курсов
@AppRoute(routes=routes,url='/courses-list/')
class CoursesList:
    @Debug(name='CoursesList')
    def __call__(self, request):
        logger.log('Список курсов')
        try:
            category = site.find_category_by_id(int(request['request_params']['id']))
            return '200 OK', render_to_template('course_list.html', objects_list=category.courses, name=category.name,
                                    id=category.id)
        except KeyError:
            return '200 OK', 'No courses have been added yet'


# контроллер - создать курс
@AppRoute(routes=routes,url='/create-course/')
class CreateCourse:
    category_id = -1
    @Debug(name='CreateCourse')
    def __call__(self, request):
        if request['method'] == 'POST':
            # метод пост
            data = request['data']

            name = data['name']
            name = site.decode_value(name)

            category = None
            if self.category_id != -1:
                category = site.find_category_by_id(int(self.category_id))

                course = site.create_course('record', name, category)
                site.courses.append(course)

            return '200 OK', render_to_template('course_list.html', objects_list=category.courses,
                                    name=category.name, id=category.id)

        else:
            try:
                self.category_id = int(request['request_params']['id'])
                category = site.find_category_by_id(int(self.category_id))

                return '200 OK', render_to_template('create_course.html', name=category.name, id=category.id)
            except KeyError:
                return '200 OK', 'No categories have been added yet'


# контроллер - создать категорию
@AppRoute(routes=routes,url='/create-category/')
class CreateCategory:
    @Debug(name='CreateCategory')
    def __call__(self, request):
        if request['method'] == 'POST':
            # POST
            print(f' from qwe444 ================={request}')
            data = request['data']
            print(f'request["data"] = data(value) ===from qwe444====+++++++++++++>{data}')

            name = data['name']
            name = site.decode_value(name)
            category_id = data.get('category_id')
            ic(f'========category_id======.{category_id}')

            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))

            new_category = site.create_category(name, category)

            site.categories.append(new_category)

            return '200 OK', render_to_template('index.html', objects_list=site.categories)
        else:
            categories = site.categories
            return '200 OK', render_to_template('create_category.html', categories=categories)


# контроллер - список категорий
@AppRoute(routes=routes,url='/category-list/')
class CategoryList:
    @Debug(name='CategoryList')
    def __call__(self, request):
        logger.log('Список категорий')
        return '200 OK', render_to_template('category_list.html', objects_list=site.categories)


# контроллер - копировать курс
@AppRoute(routes=routes,url='/copy-course/')
class CopyCourse:
    @Debug(name='CopyCourse')
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

            return '200 OK', render_to_template('course_list.html', objects_list=site.courses)
        except KeyError:
            return '200 OK', 'No courses have been added yet'
