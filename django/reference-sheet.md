# Reference Sheet

## Models

```python
# create a model
class MyModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()

# create a database migration for the model
python manage.py makemigrations

# apply the database migration
python manage.py migrate

# access the model from the Django ORM
MyModel.objects.all()
MyModel.objects.create(field1='value1', field2=123)
MyModel.objects.filter(field1='value1')

# define a relationship between models
class MyModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    related_model = models.ForeignKey(RelatedModel, on_delete=models.CASCADE)
```

## Views

```python
# create a view
def myview(request):
    return render(request, 'template.html', {'key': 'value'})

# create a view with a form
def myview(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # process the form data
            form.save()
            return redirect('/success/')
    else:
        form
```
