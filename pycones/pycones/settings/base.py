# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from os.path import abspath, basename, dirname, join, normpath
from sys import path


# PATH CONFIGURATION
# ------------------------------------------------------------------------------
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)


# DEBUG CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False


# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Marcos Gabarda', 'hola@marcosgabarda.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
# END MANAGER CONFIGURATION

# AUTHENTICATION BACKENDS CONFIGURATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = (
    'attendees.auth.AttendeeAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
)


# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'Europe/Madrid'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'es'
ugettext = lambda s: s
LANGUAGES = (
    ('es', ugettext(u'Español')),
    ('ca', ugettext(u'Catalán')),
    ('gl', ugettext(u'Gallego')),
    ('eu', ugettext(u'Euskera')),
    ('en', ugettext(u'English')),
)
LOCALE_PATHS = (
    normpath(join(SITE_ROOT, 'locale')),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True


# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'


# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'static')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key should only be used for development and testing.
SECRET_KEY = r"gfz5zzdhvgs#&2j8rv^s&4t6ef^6=k!ag0_n!k6@md(ntkwr9p"


# SITE CONFIGURATION
# ------------------------------------------------------------------------------
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []


# FIXTURE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    normpath(join(SITE_ROOT, 'fixtures')),
)


# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/templates/
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            normpath(join(SITE_ROOT, 'templates')),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.debug',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
                'schedule.context_processors.schedule_active',
                'configurations.context_processors.options',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'string_if_invalid': 'NULL',
        },
    },
]


# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
    # Default Django middleware.
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


# URL CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = '%s.urls' % SITE_NAME


# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Useful template tags:
    'django.contrib.humanize',
    # Admin panel and documentation:
    'suit',
    'django.contrib.admin',
    # 'django.contrib.admindocs',
    'rosetta',
    'taggit',
    'taggit_autosuggest',
)

# Apps specific for this project go here.
LOCAL_APPS = (
    'configurations',
    'blog',
    'conference',
    'schedule',
    'speakers',
    'proposals',
    'sponsorship',
    'attendees',
    'reviewers',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS


# DJANGO SUIT CONFIGURATION
# ------------------------------------------------------------------------------
SUIT_CONFIG = {
    'ADMIN_NAME': 'PyConES 2016',
    'MENU_ICONS': {
        'auth': 'icon-lock',
        'blog': 'icon-pencil',
        'sites': 'icon-leaf',
        'conference': 'icon-globe',
        'proposals': 'icon-inbox',
        'schedule': 'icon-calendar',
        'speakers': 'icon-bullhorn',
        'sponsorship': 'icon-briefcase',
        'attendees': 'icon-user',
        'reviewers': 'icon-thumbs-up',
        'configurations': 'icon-wrench',
        'taggit': 'icon-tags',
    }
}


# DJANGO EXTENSIONS CONFIGURATION
# ------------------------------------------------------------------------------
INSTALLED_APPS += (
    'django_extensions',
)


# LOGGING CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


# WSGI CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME

# PIPELINE CONFIGURATION
# ------------------------------------------------------------------------------
INSTALLED_APPS += (
    'pipeline',
)
PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
    'pipeline.compilers.coffee.CoffeeScriptCompiler',
)
PIPELINE_CSS = {
    'pycones': {
        'source_filenames': (
            'icons/fontello/css/pycones.css',
            'icons/fontello/css/animation.css',
            'less/pycones.less',
        ),
        'output_filename': 'css/pycones.css',
        'extra_context': {
            'media': 'screen,projection,print',
        },
    }
}
PIPELINE_JS = {
    'vendor': {
        'source_filenames': (
            'vendor/bootstrap/dist/js/bootstrap.js',
        ),
        'output_filename': 'js/vendor.js',
    },
    'pycones': {
        'source_filenames': (
            'js/*.js',
        ),
        'output_filename': 'js/pycones.js'
    }
}
PIPELINE_LESS_BINARY = "%s/node_modules/.bin/lessc" % dirname(dirname(DJANGO_ROOT))
PIPELINE_YUGLIFY_BINARY = "%s/node_modules/.bin/yuglify" % dirname(dirname(DJANGO_ROOT))
PIPELINE_LESS_ARGUMENTS = '--clean-css'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'
PIPELINE_YUGLIFY_JS_ARGUMENTS = '--terminal'
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
STATICFILES_FINDERS += (
    'pipeline.finders.PipelineFinder',
)

# TEST CONFIGURATION
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'


# MESSAGES CONFIGURATION
# ------------------------------------------------------------------------------
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}


# MARKUP FIELD CONFIGURATION
# ------------------------------------------------------------------------------
INSTALLED_APPS += (
    'markupfield',
)

import markdown
from docutils.core import publish_parts


def render_rest(markup):
    parts = publish_parts(source=markup, writer_name="html4css1")
    return parts["fragment"]


MARKUP_FIELD_TYPES = (
    ('markdown', markdown.markdown),
    ('ReST', render_rest),
)


# MODELTRANSLATION CONFIGURATION
# ------------------------------------------------------------------------------
INSTALLED_APPS += (
    'modeltranslation',
)
MODELTRANSLATION_DEFAULT_LANGUAGE = 'es'
MODELTRANSLATION_FALLBACK_LANGUAGES = ('es', 'en')

# Rosetta settings
# ------------------------------------------------------------------------------
ROSETTA_MESSAGES_SOURCE_LANGUAGE_CODE = 'es'
ROSETTA_MESSAGES_SOURCE_LANGUAGE_NAME = 'Español'
ROSETTA_STORAGE_CLASS = 'rosetta.storage.CacheRosettaStorage'
ROSETTA_MESSAGES_PER_PAGE = 25

# Taggit settings
# ------------------------------------------------------------------------------
TAGGIT_CASE_INSENSITIVE = True
