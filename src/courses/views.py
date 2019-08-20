from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Courses
from .forms import CourseModelForm
from django.views.generic import UpdateView
# BASE VIEW CLASS = View

class CourseObjectMixin(object):
    model = Courses
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj


class CourseCreateView(View):
    template_name = 'courses/course_create.html'
    def get(self, request, *args, **kwargs):
        # with GET method
        form = CourseModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # with POST method
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)

class CourseListView(View):
    template_name = 'courses/course_list.html'
    queryset = Courses.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)

class CourseView(CourseObjectMixin, View):
    template_name = 'courses/course_detail.html'
    def get(self, request, id=None, *args, **kwargs):
        # with GET method
        context = {'object': self.get_object()}
        # if id is not None:
        #     # obj = get_object_or_404(Courses, id=id)
        #     context['object'] = obj
        return render(request, self.template_name, context)

    # def post(request, *args, **kwargs):
    #     return render(request, 'courses/about.html', {})
# HTTP METHODS

def my_vbf(request, *args, **kwargs):
    print(request.method)
    return render(request, 'courses/about.html', {})

class CourseDetailView(CourseObjectMixin, View):
    template_name = 'courses/about.html'
    def get(self, request, *args, **kwargs):
        # with GET method
        return render(request, self.template_name, {})


class CourseUpdateView(CourseObjectMixin, View):
    template_name = 'courses/course_update.html'
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Courses, id=id)
        return obj

    def get(self, request, id=None, *args, **kwargs):
        # with GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        # with POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                # form = CourseModelForm()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

# class CourseUpdateView(UpdateView):
#     template_name = 'courses/course_update.html'
#     form_class = CourseModelForm
#     queryset = Courses.objects.all()
#
#     def get_object(self, queryset=None):
#         id_ = self.kwargs.get('id')
#         return get_object_or_404(Courses, id=id_)
#
#     def form_valid(self, form):
#         # print(form.cleaned_data)
#         return super().form_valid(form)

class CourseDeleteView(CourseObjectMixin, View):
    template_name = "courses/course_delete.html" # DetailView
    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None,  *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/courses/')
        return render(request, self.template_name, context)

