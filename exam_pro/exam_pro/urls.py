"""exam_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from exam.views import login
from exam.views import save_img
from exam.views import register
from exam.views import send_record
from exam.views import exam_index


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register', register.ExamRegister.as_view()),
    url(r'^login', login.LoginView.as_view()),
    url(r'^img/info', save_img.LoginSaveImg.as_view()),
    url(r'^ai/recard', send_record.SendRecad.as_view()),
    url(r'^exam/index', exam_index.ExamIndex.as_view()),

]
