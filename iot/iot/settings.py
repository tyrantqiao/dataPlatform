"""
Django settings for iot project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kv_wxnesea+=6%n65fong1-*i&t(ty301+!4tq77^)$hwfcte8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# qiao disallowedHost error
ALLOWED_HOSTS = ['*']

# django_simple_captcha 验证码配置其他配置项查看文档
# 默认格式
CAPTCHA_OUTPUT_FORMAT = '%(image)s %(text_field)s %(hidden_field)s '
CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_null', # 没有样式
# 'captcha.helpers.noise_arcs', # 线
# 'captcha.helpers.noise_dots', # 点
)
# 图片中的文字为随机英文字母，如 mdsh
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
# 图片中的文字为数字表达式，如2+2=
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
# 超时(minutes)
CAPTCHA_TIMEOUT = 1


# Application definition
# qiao: add djangorestframework
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'api',
    'captcha',
    'permission',
    'corsheaders',
    #'django_mqtt',
    #'django_mqtt.mosquitto.auth_plugin',
    #'django_mqtt.publisher',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # corsheaders
    'corsheaders.middleware.CorsMiddleware',  # cors
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'iot.urls'

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

WSGI_APPLICATION = 'iot.wsgi.application'

# qiao: rest_framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
# qiao: default is sqlite3
# default engines: django.db.backends.oracle/postgresql/mysql/sqlite3
DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'iot',
        'USER': 'root',
        # Here to set your password, By the way, If you want to use install.sh, then this password cannot change until installation completed.
        'PASSWORD': '%5QWERzxc',
        # qiao: HOST be careful, dockercompose use mysql container name
        # local run use ip
        #'HOST': '127.0.0.1',
        #'HOST': '193.112.44.251',
        'HOST': 'mysql',
        #'HOST': 'qiao_mysql_1',
        'PORT': '3306',
        'API': {
            'charset': 'utf8',
            'COLLATION': 'utf8_general_ci',
        }
    }
}

# qiao: allow cross-origin request
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

# session
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_SAVE_EVERY_REQUEST = False

# email 163 settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
SERVER_EMAIL = 'tyrantqiao@qq.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'tyrantqiao@qq.com'
EMAIL_HOST_PASSWORD = 'zfmkpurojvolbiad'
EMAIL_FROM = 'tyrantqiao <tyrantqiao@qq.com>'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
