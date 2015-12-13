# FSuns
This directory is code for a Fading Suns game called Radial Blur. The following will be a list of Fading Suns specific features added to evennia.

# Features
* CG currently does Lifepaths. Supports Nobles, Priests and Merchants.
* A Goal roller
* Weapon Damage Roller
* Mail system
* Web based request system (Django-helpdesk)
* notifications system
* Assets automatically deposit to each character based on rank each month to simulate yearly income.


# Settings.py modifications
Add django.contrib.humanize, markdown_deux, bootstrapform and helpdesk to your installed_apps.

# Prereqs
Use pip to install:
* django-bootstrap-form
* django-markdown-deux
* email-reply-parser