from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin import edit_handlers
from wagtail.core import blocks
from wagtail.core import fields
from wagtail.core.models import Orderable
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

from apps.home.blocks import ColumnsListBlock
from apps.home.blocks import TeaserListBlock
from apps.home.blocks import UpdatesBlock
from apps.images.models import CustomImage
from apps.projects.blocks import CurrentProjectsListBlock


class HomePage(Page):
    image = models.ForeignKey(
        CustomImage,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    body = fields.StreamField([
        ('text', blocks.RichTextBlock(icon='doc-full',
                                      template='home/blocks/text.html')),
        ('html', blocks.RawHTMLBlock(template='home/blocks/text.html')),
        ('teasers', TeaserListBlock()),
        ('columns', ColumnsListBlock()),
        ('projects', CurrentProjectsListBlock()),
        ('updates', UpdatesBlock())
    ])

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        edit_handlers.StreamFieldPanel('body'),
    ]

    parent_page_types = [
        'wagtailcore.Page'
    ]


class SimplePage(Page):
    body = fields.RichTextField(blank=True)
    body_block = fields.StreamField([
        ('text', blocks.RichTextBlock(icon='doc-full',
                                      template='home/blocks/text.html')),
        ('html', blocks.RawHTMLBlock(template='home/blocks/text.html')),
        ('teasers', TeaserListBlock()),
        ('columns', ColumnsListBlock()),
        ('projects', CurrentProjectsListBlock()),
        ('updates', UpdatesBlock())
    ], blank=True)

    content_panels = [
        edit_handlers.FieldPanel('title'),
        edit_handlers.FieldPanel('body'),
        edit_handlers.StreamFieldPanel('body_block'),
    ]

    parent_page_types = [
        'home.HomePage'
    ]
    subpage_types = []


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    link_page = models.ForeignKey('wagtailcore.Page', on_delete=models.CASCADE)

    @property
    def url(self):
        return self.link_page.url

    def __str__(self):
        return self.title

    panels = [
        edit_handlers.FieldPanel('title'),
        edit_handlers.PageChooserPanel('link_page')
    ]


@register_snippet
class NavigationMenu(ClusterableModel):
    title = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.title

    panels = [
        edit_handlers.FieldPanel('title'),
        edit_handlers.InlinePanel('items')
    ]


class NavigationMenuItem(Orderable, MenuItem):
    parent = ParentalKey('NavigationMenu', related_name='items')
