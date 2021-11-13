This is a Django project starter template.

This project makes no claim to be the best way to setup a django project.  
It is simply that way that I know how to setup a Django project that works.

Django Version:  Django 3.2.8

The project has been set up with the following configuration:
- CustomUser Model
---- Setup in 'accounts' app
---- Extends 'AbstractUser' with no additional fields added.
- Database
---- Includes psycopg2 to run PostgreSQL
- Docker
---- Not currently setup for Docker
- Email
---- Setup for SMTP (i.e. 
     EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend)
---- Settings read from .env  
---- Manually tested with Django development server using SendGrid
---- Commended out code to send email to console (i.e.  
     EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend')
---- Test settings (test_settings.py) uses localmem (i.e. 
     EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend')
- Environment Variables using .env file.  Read into Virtual Environment by Pipenv.
- 'main' app
---- Can be used or scrapped.
- Login and registration
---- Implemented using Django included 'auth' app.
---- URLs/Views not included by 'auth' (i.e. Signup) included in 'accounts/' app.
---- Functionality implemented:
---- ---- Signup (no email confirm)
---- ---- Login
---- ---- Logout
---- ---- Password Reset (with confirm email)
---- ---- Password Change
---- HTML and email templates added to project level 'templates/registration/' folder.
- Pipenv
---- Environment variables loaded from .env by Pipenv
- Testing
---- Includes pytest / pytest-django
---- Only dummy tests included to confirm configuration works.
---- Project level tests to be included in the project level 'tests/' folder
     (i.e. '<project_name>/tests/').  
---- App level tests intended to be saved in app level 'tests/' folder.
     (i.e. '<project_name>/<app_nam>/tests/').  This structure has been implemented in 
     the provided 'main' app.
---- Includes pytest-cov (i.e. "Coverage")
---- Includes Selenium
- Misc/Other
---- Time Zone as 'America/New York'


When cloning/forking the project please set/update make the updates below.  Depending on the update, 
the update will need to be made in .env, settings.py, or other possibly another location.

1.  Update Django Admin URL (for security) (in settings.py)
2.  Update Time Zone as needed (in settings.py)
3.  Database settings (in .env)
4.  Email Settings (in .env)

When updating Django (Future)
- Need to consider added functions and assignments in settings.py
