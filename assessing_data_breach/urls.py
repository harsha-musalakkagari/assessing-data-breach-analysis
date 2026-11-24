# """assessing_data_breach URL Configuration
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/3.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.conf.urls import url
# from django.contrib import admin
# from Remote_User import views as remoteuser
# from assessing_data_breach import settings
# from Service_Provider import views as serviceprovider
# from django.conf.urls.static import static
#
#
# urlpatterns = [
#     url('admin/', admin.site.urls),
#     url(r'^$', remoteuser.index, name="index"),
#     url(r'^login/$', remoteuser.login, name="login"),
#     url(r'^Register1/$', remoteuser.Register1, name="Register1"),
#     url(r'^Predict_Data_Breach_Type/$', remoteuser.Predict_Data_Breach_Type, name="Predict_Data_Breach_Type"),
#     url(r'^ViewYourProfile/$', remoteuser.ViewYourProfile, name="ViewYourProfile"),
#     url(r'^serviceproviderlogin/$',serviceprovider.serviceproviderlogin, name="serviceproviderlogin"),
#     url(r'View_Remote_Users/$',serviceprovider.View_Remote_Users,name="View_Remote_Users"),
#     url(r'^charts/(?P<chart_type>\w+)', serviceprovider.charts,name="charts"),
#     url(r'^charts1/(?P<chart_type>\w+)', serviceprovider.charts1, name="charts1"),
#     url(r'^likeschart/(?P<like_chart>\w+)', serviceprovider.likeschart, name="likeschart"),
#     url(r'^View_Predicted_Data_Breach_Type_Ratio/$', serviceprovider.View_Predicted_Data_Breach_Type_Ratio, name="View_Predicted_Data_Breach_Type_Ratio"),
#     url(r'^train_model/$', serviceprovider.train_model, name="train_model"),
#     url(r'^View_Predicted_Data_Breach_Type/$', serviceprovider.View_Predicted_Data_Breach_Type, name="View_Predicted_Data_Breach_Type"),
#     url(r'^Download_Predicted_DataSets/$', serviceprovider.Download_Predicted_DataSets, name="Download_Predicted_DataSets"),
#
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""assessing_data_breach URL Configuration"""

from django.urls import path
from django.contrib import admin

from Remote_User import views as remoteuser
from Service_Provider import views as serviceprovider
from assessing_data_breach import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', remoteuser.index, name="index"),
    path('login/', remoteuser.login, name="login"),
    path('Register1/', remoteuser.Register1, name="Register1"),
    path('Predict_Data_Breach_Type/', remoteuser.Predict_Data_Breach_Type, name="Predict_Data_Breach_Type"),
    path('ViewYourProfile/', remoteuser.ViewYourProfile, name="ViewYourProfile"),
    path('serviceproviderlogin/', serviceprovider.serviceproviderlogin, name="serviceproviderlogin"),
    path('View_Remote_Users/', serviceprovider.View_Remote_Users, name="View_Remote_Users"),
    path('charts/<str:chart_type>', serviceprovider.charts, name="charts"),
    path('charts1/<str:chart_type>', serviceprovider.charts1, name="charts1"),
    path('likeschart/<str:like_chart>', serviceprovider.likeschart, name="likeschart"),
    path('View_Predicted_Data_Breach_Type_Ratio/', serviceprovider.View_Predicted_Data_Breach_Type_Ratio, name="View_Predicted_Data_Breach_Type_Ratio"),
    path('train_model/', serviceprovider.train_model, name="train_model"),
    path('View_Predicted_Data_Breach_Type/', serviceprovider.View_Predicted_Data_Breach_Type, name="View_Predicted_Data_Breach_Type"),
    path('Download_Predicted_DataSets/', serviceprovider.Download_Predicted_DataSets, name="Download_Predicted_DataSets"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)