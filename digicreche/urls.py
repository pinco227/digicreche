from accounts.forms import DigiCrecheUserForm
from core.views import IndexTemplateView
from core.webhooks import stripe_webhook
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django_registration.backends.one_step.views import RegistrationView

redirect_regx = r'^.*$' if settings.USE_AWS else r'^(?!media).*$'

urlpatterns = [
    path('admin/', admin.site.urls),
    # account views
    path('accounts/register/',
         RegistrationView.as_view(
             form_class=DigiCrecheUserForm,
             success_url="/"
         ), name='django_registration_register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # login via browsable API
    path('api-auth/',
         include('rest_framework.urls')),
    # login via REST (api)
    path('api/rest-auth/',
         include('rest_auth.urls')),
    path('api/rest-auth/registration/',
         include('rest_auth.registration.urls')),
    # Core APIViews
    path('api/', include('core.api.urls')),
    # APIViews
    path('api/', include('schools.api.urls')),
    path('api/', include('rooms.api.urls')),
    path('api/', include('pupils.api.urls')),
    path('api/', include('activities.api.urls')),
    path('api/', include('chat.api.urls')),

    # Webhooks
    path('wh/', stripe_webhook, name='webhook'),

    # Redirect to index
    re_path(redirect_regx, IndexTemplateView.as_view(), name='entry-point'),

]

if not settings.USE_AWS:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
