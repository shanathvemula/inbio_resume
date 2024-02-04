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
    greeting = RichTextField(default='')
    name = RichTextField(default='')
    role1 = RichTextField(default='')
    role2 = RichTextField(blank=True)
    role3 = RichTextField(blank=True)
    short_intro = RichTextField(blank=True)
    intro = RichTextField(blank=True)
    years_of_exp = RichTextField(default=0)
    profile_pic = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+', default=1)
    # facebook_url = RichTextField(blank=True),
    # instagram_url = RichTextField(blank=True)
    # linkedin_url = RichTextField(blank=True)

    search_fields = Page.search_fields + [index.SearchField('body'), index.SearchField('short_intro')]
    content_panels = Page.content_panels + [
        FieldPanel('body'), FieldPanel('short_intro'),
        FieldPanel('subtitle'),
        FieldPanel('greeting'),
        FieldPanel('intro'),
        FieldPanel('profile_pic'),
        FieldPanel('years_of_exp'),
        FieldPanel('name'), FieldPanel('role1'), FieldPanel('role2'), FieldPanel('role3'),
        InlinePanel('logo', label="logo image"),
        InlinePanel('socialmedia', label='SocialMedia'),
        InlinePanel('skills', label='Skills'),
        InlinePanel('whatido', label='whatido')
    ]

    def clean(self):
        self.short_intro = self.short_intro.strip()  # Remove leading and trailing whitespace
        self.short_intro = re.sub(r'<.*?>', '', self.short_intro)  # Remove HTML tags
        self.intro = self.intro.strip()
        self.intro = re.sub(r'<.*?>', '', self.intro)
        self.subtitle = self.subtitle.strip()
        self.subtitle = re.sub(r'<.*?>', '', self.subtitle)
        self.body = self.body.strip()
        self.body = re.sub(r'<.*?>', '', self.body)
        self.name = self.name.strip()
        self.name = re.sub(r'<.*?>', '', self.name)
        self.greeting = self.greeting.strip()
        self.greeting = re.sub(r'<.*?>', '', self.greeting)
        self.years_of_exp = self.years_of_exp.strip()
        self.years_of_exp = re.sub(r'<.*?>', '', self.years_of_exp)
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


class SocialMedia(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='socialmedia')
    logo = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
    url = RichTextField()

    panels = [
        FieldPanel('logo'),
        FieldPanel('url')
    ]

    def clean(self):
        self.url = self.url.strip()  # Remove leading and trailing whitespace
        self.url = re.sub(r'<.*?>', '', self.url)  # Remove HTML tags


class Skills(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='skills')
    logo = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')

    panels = [
        FieldPanel('logo')
    ]


class WhatIDo(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='whatido')
    icon = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
    title = RichTextField(blank=True)
    content = RichTextField(blank=True)

    panel = [FieldPanel('icon'), FieldPanel('title'), FieldPanel('content')]

    def clean(self):
        self.title = self.title.strip()  # Remove leading and trailing whitespace
        self.title = re.sub(r'<.*?>', '', self.title)  # Remove HTML tags
        self.content = self.content.strip()
        self.content = re.sub(r'<.*?>','', self.content)