"""
URL configuration for DjangoProjectRoot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import include  # Import include for URL routing
from django.views.generic import RedirectView  # Import RedirectView for root URL redirection
from django.conf.urls.i18n import i18n_patterns  # Import i18n_patterns for internationalization


# Typing Support
from django.urls import URLPattern, URLResolver  # Add this import
from typing import List  # Use List for type compatibility

from . import views

urlpatterns: list[list[URLPattern] | URLPattern | URLResolver] = [
    
    # 国际化语言支持
    path('i18n/', include('django.conf.urls.i18n')),
    
    
    
    # 后台管理路由
    path('admin/', admin.site.urls),
    # 可在此添加自定义路由，如：
    # path('blog/', include('blog.urls')),
    
    # 参数：
    #   - ''：根路径
    #   - views.hello：视图函数
    #   - name='hello'：路由名称
    # path("hello/", views.hello, name="hello"),
    # path("test/", views.test, name="test"),
]

# 主页
# Include the URLs from the home_page app
urlpatterns += i18n_patterns(
    path("home_page/", include(('home_page_app.urls', 'home_page_app'), namespace='home_page_app')),
    path("introduction_page/", include(('introduction_page_app.urls', 'introduction_page_app'), namespace='introduction_page_app')),
    path("thanks_page/", include(('thanks_page_app.urls', 'thanks_page_app'), namespace='thanks_page_app'))
)


