from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name="index"),
    path('links/',views.YourLinks,name="your_links"),
    path('links/<int:id>',views.UpdateLink,name="update_link"),
    path('links/delete/<int:id>',views.DeleteLink,name="delete_link"),
    path('profile/',views.YourProfile,name="your_profile"),
    path('register/',views.register,name="register"),
    path('<str:hash>',views.go,name="go"),
    path('add/',views.addlink,name="add_link")
]
