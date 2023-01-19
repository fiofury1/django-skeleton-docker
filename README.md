# Django-Skeleton #

A Django project starter template preconfigured with bare bones functionality.

Current Django Version: &nbsp;Django 4.0

### Disclaimers: ###
This project makes no claim to be the "best way" to set up a Django project.

## Functionality & Configuration ##
The project has been set up with the following functionality/configuration:
- CustomUser Model
     - Set up in 'accounts' app
     - Extends 'AbstractUser' with no additional fields added.
- Database
     - Includes psycopg2 to run PostgreSQL
- Docker - Not currently set up for Docker
- Email
     - Configured for SMTP (i.e. 
     EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend)
     - Settings read from .env  
     - Manually tested with Django development server using SendGrid
     - Includes commended out code to send email to console 
     (i.e. EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend')
     - Test settings (in test_settings.py) uses localmem (i.e. 
     EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend')
- Environment Variables 
     - Uses .env file.  
     - Read into Virtual Environment by Pipenv. 
- Deployment
     - Configured for Heroku (with Procfile and runtime.txt)
- 'main' app
     - Can be used or scrapped.
- Static Files
     - Configured to use WhiteNoise for both development and production.
     - During development, configured to look for static files in 'static/' folder in root of project and apps.
     - Set up to collect static files into 'staticfiles/' folder in project root.
          - Note that 'staticfiles/' directory not included in source control so 'collect static' command will need to be run to include them in desired environment.
     - Static files compressed and cached
       (STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage')
       *See whitenoise documentation for non-cached option.* 
- Testing
     - Includes pytest / pytest-django
     - Only dummy tests included to confirm configuration works.
     - Project level tests to be included in the project level tests folder
     (i.e. '<project_name>/tests/').  
     - App level tests intended to be stored in app level tests folder.
     (i.e. '<project_name>/<app_nam>/tests/').  This structure has been implemented in 
     the provided 'main' app.
     - Includes pytest-cov (i.e. "Coverage")
     - Uses pytest-dotenv to read environment variables for testing.
     - Includes Selenium, but does not include a Web Driver.  You will need to install this into your environment.
- User Management
     - Implemented using Django included 'auth' app.
     - URLs/Views not included by 'auth' (i.e. Sign-up) included in 'accounts/' app.
     - Functionality implemented:
          - Sign-up (no email confirm)
          - Login
          - Logout
          - Password Reset (with confirm email)
          - Password Change
     - HTML and email templates added to project level 'templates/registration/' folder.
- Virtual Environment
     - Pipenv
     - Environment variables loaded from .env by Pipenv 
- Web Server
     - Gunicorn
- Other Packages
     - django-debug-toolbar
     - django-extensions
     - isort
- Misc/Other
     - Time Zone as 'America/New York'


## Forking or Cloning ##
After forking or cloning the project, you will need to:

1.  Create a new virtual environment and install dependencies using Pipenv.  
     - This should be done from the root folder of the project.  
     - The Python version used for your virtual environment needs to match the version in the Pipfile.
     - The `install` command will both create the virtual environment and install your dependencies.
          - **WARNING:**  Using `pipenv install` will install dependencies ***from the Pipfile***.  The Pipfile in this project does not currently specify versions of packages.  To create a deterministic build of the project, then use `pipenv sync` instead.  This will result in packages being installed as specified in the Pipfile.lock file.
          - Use `$ pipenv install` to install non-dev dependencies.  
          - Use `$ pipenv install --dev` to install all dependencies including dev dependencies. 
3.  Set up PostgreSQL user and local Postgres database.
4.  Create an .env file in project root (or load environment variables in another way).
5.  Update Database settings (in .env)
6.  Update project level README.md to describe project.
7.  Update Django Admin URL (for security) (in project urls.py)
8.  Update Time Zone as needed (in settings.py)
9.  Update Email Settings (in .env)
10.  Update Allowed Hosts (in settings.py)

## Updating Django (Section In Progress) ##
When updating Django... 
- Update all packages/dependencies.
     (Hints:  
     - Use `$ pipenv update --outdated` to see which packages are out of date
     - Use `$ pipenv update <package_name>` to update a specific package
- Update 'Current Django Version' in settings.py