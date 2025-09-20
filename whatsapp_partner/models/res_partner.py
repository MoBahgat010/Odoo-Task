from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError
from urllib.parse import quote

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def action_whatsapp_chat(self):
        self.ensure_one()
        mobile = self.mobile.strip() if self.mobile else ''
        if not mobile or mobile == '+20':
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': _('WhatsApp Chat'),
                    'message': _('Please enter a valid mobile number starting with +20 (e.g., +201234567890).'),
                    'type': 'warning',
                    'sticky': False,
                }
            }

        clean_mobile = ''.join(filter(lambda x: x.isdigit() or x == '+', mobile))
        if not clean_mobile.startswith('+20'):
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': _('WhatsApp Chat'),
                    'message': _('Mobile number must start with +20 (e.g., +201234567890).'),
                    'type': 'warning',
                    'sticky': False,
                }
            }

        digits = clean_mobile[1:]
        if len(digits) < 10 or len(digits) > 15:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': _('WhatsApp Chat'),
                    'message': _('Invalid mobile number length. Use international format (e.g., +201234567890).'),
                    'type': 'warning',
                    'sticky': False,
                }
            }

        return {
            'type': 'ir.actions.act_window',
            'name': _('Send WhatsApp Message'),
            'res_model': 'whatsapp.message.input',
            'view_mode': 'form',
            'view_type': 'form',
            'views': [(False, 'form')],
            'target': 'new',
            'context': {
                'default_partner_id': self.id,
                'default_mobile_digits': digits,
            },
        }

    @api.constrains('mobile')
    def _check_mobile_prefix(self):
        for record in self:
            if record.mobile and not record.mobile.strip().startswith('+20'):
                raise ValidationError(_('Mobile number must start with +20 (e.g., +201234567890).'))

    @api.model
    def create(self, vals):
        if 'mobile' not in vals or not vals['mobile'] or vals['mobile'].strip() == '':
            vals['mobile'] = '+20'
        elif vals['mobile'] and not vals['mobile'].strip().startswith('+20'):
            vals['mobile'] = '+20' + ''.join(filter(str.isdigit, vals['mobile']))
        return super(ResPartner, self).create(vals)

    def write(self, vals):
        if 'mobile' in vals:
            if not vals['mobile'] or vals['mobile'].strip() == '':
                vals['mobile'] = '+20'
            elif not vals['mobile'].strip().startswith('+20'):
                vals['mobile'] = '+20' + ''.join(filter(str.isdigit, vals['mobile']))
        return super(ResPartner, self).write(vals)

class WhatsAppMessageInput(models.TransientModel):
    _name = 'whatsapp.message.input'
    _description = 'WhatsApp Message Input'

    partner_id = fields.Many2one('res.partner', string='Contact', readonly=True)
    mobile_digits = fields.Char(string='Mobile Digits', readonly=True)
    message = fields.Text(string='Message', placeholder='Enter your message here...')

    def send_whatsapp_message(self):
        self.ensure_one()
        message = self.message.strip() if self.message else ''
        if not message:
            raise UserError(_('Please enter a message to send.'))

        encoded_message = quote(message, safe='')
        url = f"https://wa.me/{self.mobile_digits}?text={encoded_message}"

        return {
            'type': 'ir.actions.act_url',
            'url': url,
            'target': 'new',
        }