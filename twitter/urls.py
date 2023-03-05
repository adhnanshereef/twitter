from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from allauth.account.views import LoginView

class CustomLoginView(LoginView):
    template_name='google_login.html'
    authentication_method = 'oauth2'
    extra_context={
            'account_provider': 'Google'
        }

custom_login_view = CustomLoginView.as_view()

urlpatterns = [
    # path('accounts/login/', LoginView.as_view(), name='google_login'),
    path('sdjhfaldsfalksdfagsdkhfagsdfasfasfadsasljj/accounts/', include('allauth.urls')),
    path('i/', include('user.urls')),
    path("admin/admin/", admin.site.urls),
    path('', include('home.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
