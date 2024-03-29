"""
Django settings for ansible project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import pymysql
pymysql.install_as_MySQLdb()
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zlmx+!igwb=0jtf7tv0=32#h^g!7l@8)qcj-38=hlw=!5syt_8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'devops.apps.DevopsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ansible.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'ansible.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

#这里设置为连接mysql。
DATABASES = {
        'default':{
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'mydevops',
            'USER': 'admin',
            'PASSWORD': 'mysqlpass',
            'HOST': '127.0.0.1',
            'PORT': '', #留空表示默认为3306
            'OPTION': {},
            'init_command': 'SET sql_mode=STRICT_TRANS_TABLES,'
                            'SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED,autocommit=1,names "utf-8";',
        }
  }




# Email settings smtp/pop3
#邮件服务器配置文件
EMAIL_USE_SSL = True
#邮件服务
EMAIL_HOST = 'smtp.qq.com'
#端口号
EMAIL_PORT = 465
#邮箱账号
EMAIL_HOST_USER = '805403077@qq.com'
#授权码
EMAIL_HOST_PASSWORD = 'ckhkuhaaxlmubddc'
#发送人
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
#
# # logging
#
# LOGGING = {
#
#     'version':1,
#     'disable_existing_loggers':False,
#     'formatters':
#         {
#             'verbose':{
#                 'format':'{}'
#             }
#         }
#
#
# }



# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIR = (
    os.path.join(BASE_DIR,'static'),
)