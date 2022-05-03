"""
Django settings for ComputerHardwareBackEnd project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import datetime
from pathlib import Path
import os
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=%1%&qzeywe#-c@*5mxu+zb-28m=(6wy45-gti4x%v#k&0c&gw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'simpleui',  # 注册放在admin之前
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',                       # DRF 框架
    'corsheaders',                          # 跨域
    'users.apps.UsersConfig',               # 用户 users
    'cpus.apps.CpusConfig',                 # CPU cpus
    'mainboards.apps.MainboardsConfig',     # 主板 mainboards
    'gpus.apps.GpusConfig',                 # 显卡 gpus
    'memories.apps.MemoriesConfig',         # 内存 memories
    'ssds.apps.SsdsConfig',                 # 固态 ssds
    'hdds.apps.HddsConfig',                 # 机械硬盘 hdds
    'powers.apps.PowersConfig',             # 电源 powers
    'cases.apps.CasesConfig',               # 机箱 cases
]

sys.path.insert(0, os.path.join(BASE_DIR, '../apps'))

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',    # CORS 中间件
]

ROOT_URLCONF = 'ComputerHardwareBackEnd.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
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

WSGI_APPLICATION = 'ComputerHardwareBackEnd.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 选择数据库引擎
        'HOST': '192.168.31.129',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'September',  # 数据库用户名
        'PASSWORD': 'SMILE8023+',  # 数据库用户密码
        'NAME': 'computerhardware',  # 创建的数据库名字
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'       # 使用中国语言

TIME_ZONE = 'Asia/Shanghai'     # 使用中国上海时间

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


# # 设置静态文件路径
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 配置自定义认证的用户模型类
AUTH_USER_MODEL = 'users.UserInfo'     # 子应用名.模型类名

# 配置Redis存储信息
CACHES = {
    # 默认的redis配置
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # session配置
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # 验证码配置
    "verify_codes": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# CORS设置访问白名单
CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1',
    'http://localhost',
    'http://192.168.31.129',    # 虚拟机的IP地址
    'http://192.168.31.21',
)
CORS_ALLOW_CREDENTIALS = True # 允许携带 cookie

# JWT配置信息
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

JWT_AUTH = {
    # JWT_EXPIRATION_DELTA 指明token的有效期
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
    # 配置自定义的jwt返回方法
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'users.utils.jwt_response_payload_handler',
}


SIMPLEUI_LOGO = 'http://192.168.31.129:8000/static/logo/logo.png'  # 指定logo图片
SIMPLEUI_HOME_INFO = False  # 关闭simpleui的推广
