"""
Django settings for youthful project.

Generated by 'django-admin startproject' using Django 4.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^x*kutk$_myco&qhx+h+l%^vp0@%k#=3j(=(dehjkbvm^wx8f#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # 앱등록
    'accounts',
    'articles',
    'communities',
    'deposits',
    'savings',
    'subsidies',
    'maps',
    'exchanges',
    # 여기까지 앱 등록

    # 추가 된 부분---------------------------------------------------------------------

    'rest_framework',  # Django REST Framework - RESTful API 구축을 위한 강력한 툴킷
    'rest_framework.authtoken',  # DRF의 토큰 기반 인증 시스템
    'dj_rest_auth',  # dj-rest-auth - REST API 엔드포인트를 통한 인증 기능 제공
    'corsheaders',  # django-cors-headers - 크로스 오리진 리소스 공유(CORS) 설정을 위한 앱
    'django.contrib.sites',  # Django의 사이트 프레임워크 - 여러 도메인 관리에 사용
    'allauth',  # django-allauth - 유연한 인증, 등록, 계정 관리 기능 제공
    'allauth.account',  # allauth의 계정 관리 기능
    'dj_rest_auth.registration',  # dj-rest-auth의 등록 기능 - REST API를 통한 사용자 등록

    # 여기까지 추가-------------------------------------------------------------------------

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# 추가 된 부분-------------------------------------------------------------------------

# Django의 sites 프레임워크에서 사용할 현재 사이트의 ID
# django.contrib.sites 앱을 사용할 때 필요하며, 기본값으로 1을 사용
SITE_ID = 1

# Django REST Framework (DRF) 설정
REST_FRAMEWORK = {
    # 인증 설정
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 토큰 기반 인증을 기본 인증 방식으로 설정
        # 클라이언트는 요청 헤더에 'Authorization: Token <your-token>' 형식으로 토큰을 포함시켜야 함
        'rest_framework.authentication.TokenAuthentication',
    ],

    # 권한 설정
    'DEFAULT_PERMISSION_CLASSES': [
        # 모든 뷰에 대해 기본적으로 누구나 접근 가능하도록 설정
        # 주의: 이 설정은 개발 중에는 편리할 수 있지만, 프로덕션 환경에서는 보안상 위험할 수 있음
        # 실제 서비스에서는 더 제한적인 권한 설정을 사용하는 것이 좋음
        'rest_framework.permissions.AllowAny',
    ],
}

# 여기까지 추가 된 부분--------------------------------------------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',    # CORS(Cross-Origin Resource Sharing) 관련 설정을 처리하는 미들웨어
                                                # 프론트엔드와 백엔드가 다른 도메인에 있을 때 필요한 HTTP 헤더를 추가
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',     # django-allauth의 계정 관련 기능을 처리하는 미들웨어
                                                        # 사용자 인증, 로그인 상태 확인 등의 기능을 제공
]

# 추가 된 부분------------------------------------------------------

# CORS(Cross-Origin Resource Sharing) 설정
# 이 설정은 특정 출처(도메인)에서의 API 요청만을 허용합니다.
CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:5173',  # 로컬 개발 서버 주소 (IP 주소 사용)
    'http://localhost:5173',  # 로컬 개발 서버 주소 (localhost 사용)
]
# 이 설정은 위에 나열된 출처에서 오는 크로스 오리진 요청만을 허용합니다.
# 주로 프론트엔드 개발 서버의 주소를 지정합니다.
# 5173은 Vite 등의 최신 프론트엔드 개발 서버에서 흔히 사용되는 기본 포트입니다.


# 여기까지 추가 된 부분--------------------------------------------

ROOT_URLCONF = 'youthful.urls'

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

WSGI_APPLICATION = 'youthful.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# 추가 한 부분----------------------------------------------------------------

# Django의 기본 사용자 모델을 커스텀 사용자 모델로 대체하는 설정
AUTH_USER_MODEL = 'accounts.User'

# 이 설정은 Django에게 프로젝트에서 사용할 사용자 모델을 지정합니다.
# 'accounts.User'는 'accounts' 앱 내의 'User' 모델을 사용하겠다는 의미입니다.
# 이를 통해 Django의 기본 User 모델 대신 우리가 정의한 커스텀 User 모델을 사용할 수 있습니다.


# dj-rest-auth 설정
# dj-rest-auth 라이브러리의 회원가입 기능을 커스터마이즈하기 위한 설정

# 회원가입 시 사용할 커스텀 시리얼라이저 지정
REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'accounts.serializers.CustomRegisterSerializer',
}

# 사용자 상세 정보를 위한 커스텀 시리얼라이저 지정
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'accounts.serializers.CustomUserDetailsSerializer',
}

# allauth의 계정 어댑터를 커스텀 어댑터로 지정
# 이를 통해 회원가입 시 추가 필드를 처리할 수 있음
ACCOUNT_ADAPTER = 'accounts.adapters.CustomAccountAdapter'

# 미디어 파일 설정 (프로필 이미지를 위해 필요)
# 사용자가 업로드한 파일(예: 프로필 이미지)을 저장하고 제공하기 위한 설정
MEDIA_URL = '/media/'  # 미디어 파일에 접근할 때 사용할 URL 접두사
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 미디어 파일이 저장될 서버의 실제 경로

# 여기까지 추가 한 부분---------------------------------------------------------------