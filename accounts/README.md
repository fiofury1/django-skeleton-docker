# Accounts #

An app that:
- Provides user management in conjunction with or in addition to the Django provided 'auth' app.  
- Includes templates other than those expected in the 'registration/' folder.
- Defines the CustomerUser model

### Disclaimers ###
The Django included 'auth' app expects a number of HTML and email templates to be included in a directory called 'registration/'.  For this project, the 'registration/' folder is included in a project-level 'templates/' folder.  All other user management templates, views, and urls included here are either expected by the 'auth' app OR  override those of the 'auth' app.