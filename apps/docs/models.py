from django.db import models
from django.utils.translation import ugettext_lazy as _
from wagtail.admin import edit_handlers
from wagtail.core import fields
from wagtail.core.blocks import RichTextBlock
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

from .blocks import DocsBlock


class DocsPage(Page):

    image = models.ForeignKey(
        'images.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    body = fields.StreamField([
        ('documents_list', DocsBlock()),
        ('Text', RichTextBlock())
    ])

    description = models.CharField(max_length=200)

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        edit_handlers.FieldPanel('description'),
        edit_handlers.StreamFieldPanel('body'),
    ]

    class Meta:
        verbose_name = _('Documents')

    parent_page_types = [
        'home.HomePage'
    ]
    subpage_types = []
