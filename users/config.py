# -*- coding: utf-8 -*-

from livesettings import config_register, ConfigurationGroup, StringValue, LongStringValue
from django.utils.translation import ugettext_lazy as _

# First, setup a grup to hold all our possible configs
MYAPP_GROUP = ConfigurationGroup(
    'app', # key: internal name of the group to be created
    _('Application Settings'), # name: verbose name which can be automatically translated
    ordering=0             # ordering: order of group in the list (default is 1)
)

config_register(StringValue(
    MYAPP_GROUP,
    'title',
    description=_('Application Title'), # label for the value
    help_text=_("Displayed in header in all pages."), # help text
    default='Office Management System'  # value used if it have not been modified by the user interface
))

config_register(LongStringValue(
    MYAPP_GROUP,
    'header',
    description=_('Header for Forms'),
    help_text=_("Usually the name of the Office"),
    default=''
))

config_register(StringValue(
    MYAPP_GROUP,
    'fiscal_year',
    description=_('Fiscal Year'),
    #help_text=_("Displayed in header in all pages."),
    default=''
))