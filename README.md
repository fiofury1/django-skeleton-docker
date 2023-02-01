# Django-Skeleton - BETA - UNDER DEVELOPMENT #

A Django project starter template intentionally preconfigured with "bare bones" functionality.

Current Django Version: &nbsp;Django 4.1.5

### Disclaimers: ###
This project makes no claim to be the "best way" to set up a Django project.

## Functionality & Configuration ##
The project has been set up with the following functionality/configuration:
- Code Formatting
     - Python
          - black
          - isort
     - All code formatting packages installed as Pipenv [dev-packages]
- Database
     - Datebase:  PostgreSQL
     - Database Adapter/Connector:  psycopg2
- Deployment
     - Configured for Heroku (with Procfile and runtime.txt)
- Docker - Not currently set up for Docker
- Email
     - Configured by environment as follows:
          - DEV:  To console (EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend')
          - TEST:  To localmem (EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend')
          - PROD: SMTP (EMAIL_BACKEND = django.core.mail.backends.smtp.EmailBackend)  
     - Specific values for settings read from environment.
     - Alternate configurations commented out in code for quick changes while debugging.  
- Environments / Environment Variables 
     - Separate environments for local development (DEV), test (TEST), and production (PROD)
     - Variable named 'DEV' assigned in environment specifies the environment.  Possible values:  DEV, TEST, PROD
     - Where are variables stored?
          - DEV:    .env file (not included).  Variables read into environment by Pipenv.
          - TEST:   .env-test file (not included).  Variables read into environment by pytest-dotenv.
          - PROD:   Configured through Heroku settings.  Variables read into environment by Heroku.  
     - See included EXAMPLE.env for example .env file. 
- Front End Frameworks:
     - CSS:  None
     - JavaScript:  None
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
     - Uses pytest / pytest-django packages.
          - pytest settings found in pytest.ini.
          - Uses conftest.py files to define test data/fixtures.
               - Fitures included:  browser, authenticated_browser, authenticated_user
          - Uses 'mixer' (package) for generating test data.
     - Uses pytest-dotenv to read environment variables into TEST environment.
     - Uses Selenium and ChromeDriver for functional/integration testing.  
          - Does not include a ChromeDriver in source code.  You will need to install ChromeDriver into your environment(s).
     - Includes pytest-cov (i.e. "Coverage") 
     - Test file/folder structure
          - Project level tests to be included in the project level 'tests' folder
          (i.e. '<project_name>/tests/').  
               - Includes example test file and template for functional tests. 
          - App level tests intended to be stored in app level 'tests' folder.
          (i.e. '<project_name>/<app_nam>/tests/').  This structure has been implemented in the provided 'main' app.
               - Includes example test file, working functional tests file, and template files for testing models, templates, urls, and views.
     - All testing packages installed as Pipenv [dev-packages]
- User Management
     - CustomUser Model
          - Set up in 'accounts' app
          - Extends 'AbstractUser' with no additional fields added.
     - Implemented using Django included 'auth' app.
     - URLs/Views not included by 'auth' (i.e. Sign-up) included in 'accounts/' app.
     - Functionality implemented:
          - Sign-up (no email confirm)
          - Login
          - Logout
          - Password Reset (with confirm email)
          - Password Change
     - HTML and email templates added to project level 'templates/registration/' folder.
     - **WARNING:** User management setup is not included in automated test suite.  Testing is under development and will be released soon.
- Virtual Environment
     - Pipenv
     - Environment variables loaded from .env by Pipenv in DEV. 
- Web Server
     - Django Dev Server used by default for DEV and TEST.
     - Gunicorn for PROD.
- Other Packages
     - django-debug-toolbar
     - django-extensions
- Misc/Other
     - Time Zone as 'America/New York'


## Forking or Cloning ##
After forking or cloning the project, you will need to:

1.  Create a new virtual environment and install dependencies using Pipenv.  
     - This should be done from the root folder of the project.  
     - The Python version used for your virtual environment needs to match the version in the Pipfile.
     - The `install` command will both create the virtual environment and install your dependencies.
          - **WARNING:**  Using `pipenv install` will install dependencies ***from the Pipfile***.  The Pipfile in this project does not currently specify versions of packages, which means the latest version will be installed.  To create a deterministic build of the project, then use `pipenv sync` instead.  This will result in packages being installed as specified in the Pipfile.lock file.
          - Use `$ pipenv install` to install non-dev dependencies.  
          - Use `$ pipenv install --dev` to install all dependencies including dev dependencies. 
3.  Set up PostgreSQL user and local Postgres database.
4.  Create an .env file in project root (or load environment variables in another way).
5.  Update Database settings (in .env).
6.  Update Django Admin URL (for security) (in project urls.py).
7.  Update Time Zone as needed (in settings.py).
8.  Update Email Settings (in .env).
9.  Update Allowed Hosts (in settings.py).
10.  Customize:
     - Project level README.md to describe project.
     - Home Page Title and Heading.  Obviously, also delete the header about Django-Skeleton.

## Updating Django (Section In Progress) ##
When updating Django... 
- Update all packages/dependencies.
     (Hints:  
     - Use `$ pipenv update --outdated` to see which packages are out of date
     - Use `$ pipenv update <package_name>` to update a specific package
- Update 'Current Django Version' in settings.py