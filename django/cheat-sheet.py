# create a new Django project
django-admin startproject myproject

# create a new Django app
python manage.py startapp myapp

# run the development server
python manage.py runserver

# create a new model
class MyModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()

# create a database migration for the model
python manage.py makemigrations

# apply the database migration
python manage.py migrate

# create a Django admin user
python manage.py createsuperuser

# create a Django view
def myview(request):
    return render(request, 'template.html', {'key': 'value'})

# create a Django template
<html>
  <body>
    {{ key }}
  </body>
</html>

# create a Django URL pattern
urlpatterns = [
    path('myview/', myview),
]

# create a Django form
class MyForm(forms.Form):
    field1 = forms.CharField(max_length=100)
    field2 = forms.IntegerField()

# ----------------------- More Snippets ----------------------------------

# render a template
return render(request, 'template.html', {'key': 'value'})

# redirect to another URL
return redirect('/new-url/')

# create a form
class MyForm(forms.Form):
    field1 = forms.CharField(max_length=100)
    field2 = forms.IntegerField()

# create a model form
class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['field1', 'field2']

# process a form submission
if request.method == 'POST':
    form = MyForm(request.POST)
    if form.is_valid():
        # process the form data
        form.save()
        return redirect('/success/')

# create an object from a form
form = MyForm(request.POST)
if form.is_valid():
    obj = MyModel.objects.create(**form.cleaned_data)

# create an object from a model form
form = MyModelForm(request.POST)
if form.is_valid():
    form.save()

# filter objects by a field
MyModel.objects.filter(field='value')

# order objects by a field
MyModel.objects.order_by('field')

# paginate objects
from django.core.paginator import Paginator
objects = MyModel.objects.all()
paginator = Paginator(objects, 25)
page = request.GET.get('page')
objects
