from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils import Choices


class Guest(models.Model):
    ATTENDING_STATUSES = Choices(
        (1, "yes", _("Yes")),
        (2, "no", _("No")),
        (3, "maybe", _("Maybe")),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(_("Name"), max_length=30)
    surname = models.CharField(_("Surname"), max_length=50)
    attending = models.PositiveSmallIntegerField(
        _("attending"),
        choices=ATTENDING_STATUSES,
        default=ATTENDING_STATUSES.maybe,
    )
    attending_afters = models.PositiveSmallIntegerField(
        _("attening afters"),
        choices=ATTENDING_STATUSES,
        default=ATTENDING_STATUSES.maybe,
    )
    wants_bus = models.BooleanField(
        _("Wants bus"),
        default=False,
    )
    is_vegetarian = models.BooleanField(
        _("is vegetarian"),
        default=False,
    )
    comments = models.TextField(_("additional comment"), blank=True, max_length=200)
    is_accompanying_person = models.BooleanField(
        _("is accompanying person"), default=False
    )
    eligible_for_afters = models.BooleanField(_("eligible for afters"), default=False)

    class Meta:
        verbose_name = _("Guest")
        verbose_name_plural = _("Guests")

    def __str__(self):
        return "{} {}".format(self.name, self.surname)


class Gift(models.Model):
    name = models.CharField(_("name"), max_length=100)
    guest = models.ForeignKey(
        Guest, verbose_name=_("guest"), on_delete=models.CASCADE, blank=True, null=True
    )
    url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = _("Gift")
        verbose_name_plural = _("Gifts")

    def __str__(self):
        return self.name
