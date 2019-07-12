"""Disqus Package Event Handlers.
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import lang, router, reg
from plugins import auth


def router_dispatch():
    """'pytsite.router.dispatch' event handler.
    """
    if not reg.get('disqus.short_name') and auth.get_current_user().has_role('dev'):
        router.session().add_warning_message(lang.t('disqus@plugin_setup_required_warning'))
