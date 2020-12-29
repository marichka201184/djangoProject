from django.urls import path

from .views import pets, owners, base, calc

# , index

urlpatterns = [
    path('', base),
    # path('owners/<int:id>', pets, name='pets'),
    path('owners/<int:id>', pets, name='pets'),
    path('owners/', owners, name='owners'),
    path('<int:first>/<str:option>/<int:second>', calc, name='calc')
]
