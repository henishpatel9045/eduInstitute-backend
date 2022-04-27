# **Education Backend**
This is backend project for educational institute portal written in python using django-rest-framework.

## **Project Structure**
```
├── core
│   ├── admin.py
│   │   ├── StudentAdmin
│   │   ├── CourceAdmin
│   │   └── EnrolledCourceAdmin
│   ├── models.py
│   │   ├── Student
│   │   ├── Cources
│   │   └── EnrolledCources
│   ├── serializers.py
│   │   ├── StudentSerializer
│   │   ├── CourceSerializer
│   │   └── EnrolledCourceSerializer
│   ├── views.py
│   │   ├── CourceViewSet - OPEN
│   │   ├── StudentViewSet - PROTECTED
│   │   └── EnrolledCourceAdmin - PROTECTED
│   ├── tests.py
│   ├── urls.py
│   └── apps.py
├── manager
│   ├── admin.py
│   │   └── RegistrationAdmin
│   ├── models.py
│   │   └── RegistrationRequests
│   ├── serializers.py
│   │   └── RegistrationRequestsSerializer
│   ├── views.py
│   │   └── RegistrationRequestsViewSet - PROTECTED
│   ├── tests.py
│   ├── urls.py
│   └── apps.py
├── core
│   ├── admin.py
│   │   ├── SiteAdmin
│   │   ├── StoryAdmin
│   │   ├── SocialMediaAdmin
│   │   └── AddressAdmin
│   ├── models.py
│   │   ├── SocialMediaInfo
│   │   ├── AddressInfo
│   │   ├── Story
│   │   └── SiteInfo
│   ├── serializers.py
│   │   ├── SiteInfoSerializer
│   │   ├── StorySerializer
│   │   ├── AddressInfoSerializer
│   │   └── SocialMediaInfoSerializer
│   ├── views.py
│   │   ├── SiteInfoViewSet - OPEN
│   │   └── StoryViewSet - OPEN
│   ├── tests.py
│   ├── urls.py
│   └── apps.py
├── eduInstitute - PROJECT FOLDER
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .gitignore
├── Education Institute Model.drawio - SCHEMA DIAGRAM
├── manage.py - PROJECT ENTRY POINT
├── Pipfile - PIPENV
└── Pipfile.lock - PIPENV
```



