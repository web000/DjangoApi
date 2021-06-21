
from django.contrib import admin
from django.urls import path
from api.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentInfo/<int:pk>', student_detail),
    path('studentList/', studentList),
    path('studentCreate/', studentCreate),
    path('studentApi/', studentApi),
    path('studentApi/<int:pk>', studentApi),
    # class Based APIView
    path('studentAPI/', StudentAPI.as_view()),
    path('studentAPI/<int:pk>', StudentAPI.as_view()),






]
