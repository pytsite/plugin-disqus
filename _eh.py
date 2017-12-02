"""Disqus Package Event Handlers.
"""
from pytsite import lang as _lang, router as _router, reg as _reg
from plugins import auth as _auth

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def router_dispatch():
    """'pytsite.router.dispatch' event handler.
    """
    if not _reg.get('disqus.short_name') and _auth.get_current_user().has_permission('disqus.settings.manage'):
        _router.session().add_warning_message(_lang.t('disqus@plugin_setup_required_warning'))
