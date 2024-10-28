
from pathlib import Path
from dotenv import load_dotenv
import os
from .base import *
load_dotenv() 

SECRET_KEY = os.getenv("API_KEY")
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']
MONGO_DATABASE = {
      'DRIVER': os.getenv("MONGO_DRIVER"),
      'USER': os.getenv('MONGO_USER'),
      'PASSWORD':os.getenv('MONGO_PASSWORD'),
      'HOST':os.getenv('MONGO_HOST'),
      'PORT':os.getenv('MONGO_PORT')
}



DATABASES = {
      'default':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('NAME'),
        'USER':os.getenv('USER'),
        'PASSWORD':os.getenv('PASSWORD'),
        'HOST':os.getenv('HOST'),
        'PORT':os.getenv('PORT')
    }

}






