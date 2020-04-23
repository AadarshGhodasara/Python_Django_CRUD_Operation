
from django.contrib import admin
from django.urls import path
from mysite import view
from . import view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.index, name='index'),
    path('index', view.index, name='index'),
    # path('', view.register)
    path('register', view.register, name='register'),
    path('view', view.view, name='view'),
    path('delete/<int:id>', view.delete),
    path('edit/<int:id>', view.edit),
    path('update/<int:id>', view.update)
]
