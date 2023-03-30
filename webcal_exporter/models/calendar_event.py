import requests
import caldav
import logging

from calendar import Calendar
from requests.auth import HTTPBasicAuth
from odoo import models, fields, api
_logger = logging.getLogger(__name__)

_logger = logging.getLogger(__name__)

class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    external_uuid = fields.Char(string='External UUID')

