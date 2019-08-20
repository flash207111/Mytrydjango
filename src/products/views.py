# from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from  .forms import ProductForm, RawProductForm

# def product_create_view(request):
#     my_form = RowProductForm()
#     if request.method == 'POST':
#         my_form = RowProductForm(request.POST)
#         if my_form.is_valid():
#             # now the data is good
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#             # my_form = RowProductForm()
#         else:
#             print(my_form.errors)
#     context = {
#         'form': my_form,
#     }
#     return render(request, "products/product.create.html", context)


# def product_create_view(request):
#     # print(request.GET)
#     # print(request.POST)
#     if request.method == 'POST':
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#         # Product.object.create(title=my_new_title)
#     context = {}
#     return render(request, "products/product.create.html", context)

def render_initial_data(request):
    initial_data = {
        'title': "My this awesome title"
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form }
    return render(request, "products/product.create.html", context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form }
    return render(request, "products/product.create.html", context)

def product_update_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
            }
    return render(request, "products/product.create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    #     'price': obj.price,
    # }
    context = {
        'object': obj
    }
    return render(request, "products/product.detail.html", context)

def dynamic_lookup_view(request, my_id):
    # obj = Product.objects.get(id=my_id)
    obj = get_object_or_404(Product, id=my_id)
    # try:
    #     obj = Product.objects.get(id=my_id)
    # except Product.DoesNotExist:
    #     raise Http404

    context = {
        'object': obj
            }
    return render(request, "products/product.detail.html", context)

def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    # POST request
    if request.method == 'POST':
        # confirming delete
        obj.delete()
        return redirect('../../')
    context = {
        'object': obj
            }
    return render(request, "products/product.delete.html", context)

def product_list_view(request):
    queryset = Product.objects.all() # list of objects
    context = {
        'object_list': queryset
    }
    return render(request, "products/product.list.html", context)