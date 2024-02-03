import re

from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, BlockField
from wagtail.admin.panels import FieldPanel, InlinePanel

from wagtail.search import index


class HomePage(Page):
    body = RichTextField(blank=True)
    subtitle = RichTextField(blank=True)
    greeting = RichTextField()
    name = RichTextField()
    role1 = RichTextField()
    role2 = RichTextField(blank=True)
    role3 = RichTextField(blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    short_intro = RichTextField(blank=True)
    # facebook_url = RichTextField(blank=True)
    # instagram_url = RichTextField(blank=True)
    # linkedin_url = RichTextField(blank=True)

    search_fields = Page.search_fields + [index.SearchField('body'), index.SearchField('short_intro')]
    content_panels = Page.content_panels + [
        FieldPanel('body'), FieldPanel('short_intro'),
        FieldPanel('facebook_url'), FieldPanel('instagram_url'), FieldPanel('linkedin_url'),
        FieldPanel('subtitle'),
        FieldPanel('greeting'),
        FieldPanel('name'), FieldPanel('role1'), FieldPanel('role2'), FieldPanel('role3'),
        InlinePanel('logo', label="logo image"),
    ]

    def clean(self):
        self.short_intro = self.short_intro.strip() # Remove leading and trailing whitespace
        self.short_intro = re.sub(r'<.*?>', '', self.short_intro)  # Remove HTML tags
        self.subtitle = self.subtitle.strip()
        self.subtitle = re.sub(r'<.*?>', '', self.subtitle)
        self.body = self.body.strip()
        self.body = re.sub(r'<.*?>', '', self.body)
        self.name = self.name.strip()
        self.name = re.sub(r'<.*?>', '', self.name)
        self.greeting = self.greeting.strip()
        self.greeting = re.sub(r'<.*?>', '', self.greeting)
        self.role1 = self.role1.strip()
        self.role1 = re.sub(r'<.*?>', '', self.role1)
        self.role2 = self.role2.strip()
        self.role2 = re.sub(r'<.*?>', '', self.role2)
        self.role3 = self.role3.strip()
        self.role3 = re.sub(r'<.*?>', '', self.role3)


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='logo')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]
