"""
Django settings for flourish_child project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SITE_ID = 1

ETC_DIR = '/etc'

APP_NAME = 'flourish_child'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u6n_*li7t!e23ne*cs))g^b3k2w8%258)&3q8g4k)_im*rf)qt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DEFAULT_STUDY_SITE = 40

ALLOWED_HOSTS = []

DEVICE_ID = 20

DEVICE_ROLE = 'Client'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_crypto_fields.apps.AppConfig',
    'django.contrib.sites',
    'django_q',
    'edc_action_item.apps.AppConfig',
    'edc_dashboard.apps.AppConfig',
    'edc_device.apps.AppConfig',
    'edc_lab.apps.AppConfig',
    'edc_odk.apps.AppConfig',
    'edc_identifier.apps.AppConfig',
    'edc_registration.apps.AppConfig',
    'edc_reference.apps.AppConfig',
    'edc_metadata_rules.apps.AppConfig',
    'edc_base.apps.AppConfig',
    'edc_data_manager.apps.AppConfig',
    'edc_consent.apps.AppConfig',
    'edc_visit_schedule.apps.AppConfig',
    'flourish_prn.apps.AppConfig',
    'flourish_reference.apps.AppConfig',
    'flourish_metadata_rules.apps.AppConfig',
    'flourish_follow.apps.AppConfig',
    'flourish_labs.apps.AppConfig',
    'flourish_caregiver.apps.AppConfig',
    'flourish_child.apps.EdcAppointmentAppConfig',
    'flourish_child.apps.EdcMetadataAppConfig',
    'flourish_child.apps.EdcProtocolAppConfig',
    'flourish_child.apps.EdcTimepointAppConfig',
    'flourish_child.apps.EdcVisitTrackingAppConfig',
    'flourish_child.apps.EdcFacilityAppConfig',
    # 'flourish_child.apps.EdcSenaiteInterfaceAppConfig',
    'flourish_visit_schedule.apps.AppConfig',
    'flourish_child.apps.AppConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'edc_dashboard.middleware.DashboardMiddleware',
    'edc_subject_dashboard.middleware.DashboardMiddleware',
]

ROOT_URLCONF = 'flourish_child.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'flourish_child.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

COUNTRY = 'botswana'
HOLIDAY_FILE = os.path.join(BASE_DIR, 'holidays.csv')

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

DASHBOARD_URL_NAMES = {}

if 'test' in sys.argv:

    class DisableMigrations:

        def __contains__(self, item):
            return True

        def __getitem__(self, item):
            return None

    MIGRATION_MODULES = DisableMigrations()
    PASSWORD_HASHERS = ('django.contrib.auth.hashers.MD5PasswordHasher',)
    DEFAULT_FILE_STORAGE = 'inmemorystorage.InMemoryStorage'
