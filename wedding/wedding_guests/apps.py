from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WeddingGuestsConfig(AppConfig):
    name = "wedding.wedding_guests"
    verbose_name = _("Wedding Guests")
