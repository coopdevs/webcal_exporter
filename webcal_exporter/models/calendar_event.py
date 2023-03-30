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

    @api.model
    def _create_unsync_tag(self):
        Tag = self.env['calendar.event.type']
        tag_name = '#unsync'
        unsync_tag = Tag.search([('name', '=', tag_name)])
        if not unsync_tag:
            unsync_tag = Tag.create({'name': tag_name})
            self.env['ir.config_parameter'].sudo().set_param(
                'webcal_exporter.unsync_tag_id', unsync_tag.id)
        return unsync_tag
