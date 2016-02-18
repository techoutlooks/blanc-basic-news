from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


default_app_config = 'blanc_basic_news.apps.BlancBasicNewsConfig'

# Don't call these in models.py. 
# It calls registry which is not loaded yet.
def get_post_model():
    try:
        conf_model = getattr(settings, 'NEWS_POST_MODEL', 'news.Post')
        return django_apps.get_model(conf_model)
    except ValueError:
        raise ImproperlyConfigured("NEWS_POST_MODEL must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured("NEWS_POST_MODEL refers to model '%s' that has not been installed" % conf_model)
        
def get_category_model():
    try:
        conf_model = getattr(settings, 'NEWS_CATEGORY_MODEL', 'news.Category')
        return django_apps.get_model(conf_model)
    except ValueError:
        raise ImproperlyConfigured("NEWS_CATEGORY_MODEL must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured("NEWS_CATEGORY_MODEL refers to model '%s' that has not been installed" % conf_model)
                

