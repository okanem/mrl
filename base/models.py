from django.db import models
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
)
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)

@register_setting
class NavigationSettings(BaseGenericSetting):
    facebook_url = models.URLField(verbose_name="Facebook URL", blank=True)
    x_url = models.URLField(verbose_name="X URL", blank=True)
    instagram_url = models.URLField(verbose_name="Instagram URL", blank=True)
    linkedin_url = models.URLField(verbose_name="LinkedIn URL", blank=True)



    panels = [
        MultiFieldPanel(
            [
                FieldPanel("facebook_url"),
                FieldPanel("x_url"),
                FieldPanel("instagram_url"),
                FieldPanel("linkedin_url"),
            ],
            "Social settings",
        )
    ]