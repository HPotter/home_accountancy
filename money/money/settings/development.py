from base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS += ('debug_toolbar', )
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )

DEBUG_TOOLBAR_PATCH_SETTINGS = True


class AllIps(object):
    def __contains__(self, ip):
        return True

INTERNAL_IPS = AllIps()