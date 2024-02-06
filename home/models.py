import re

from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, BlockField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from django.core.validators import MaxValueValidator, MinValueValidator

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
        InlinePanel('logo', label="Logo Image"),
        InlinePanel('socialmedia', label='SocialMedia'),
        InlinePanel('skills', label='Skills'),
        InlinePanel('whatido', label='What I Do'),
        InlinePanel('portfolio', label='Portfolio'),
        InlinePanel('education', label='Education Details'),
        InlinePanel('professional', label='Professional Skills'),
        InlinePanel('experience', label='Experience'),
        InlinePanel('testimonial', label='Testimonial')
    ]

    def clean(self):
        self.short_intro = self.short_intro.strip()  # Remove leading and trailing whitespace
        self.short_intro = re.sub(r'<.*?>', '', self.short_intro)  # Remove HTML tags
        self.short_intro = self.short_intro.replace('&#x27;', "'")
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
        self.content = re.sub(r'<.*?>', '', self.content)


class Portfolio(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='portfolio')
    portfolio_logo = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
    type = RichTextField()
    project_title = RichTextField()
    description = RichTextField()
    description2 = RichTextField(blank=True)
    project_link = models.URLField()

    # panel = [FieldPanel('logo'), FieldPanel('type'), FieldPanel('liked'), FieldPanel('title'),
    #          FieldPanel('description'), FieldPanel('project_link')]
    panels = [FieldPanel('portfolio_logo'), FieldPanel('type'), FieldPanel('project_title'),
              FieldPanel('description'), FieldPanel('project_link')]

    def clean(self):
        self.type = self.type.strip()  # Remove leading and trailing whitespace
        self.type = re.sub(r'<.*?>', '', self.type)  # Remove HTML tags
        self.project_title = self.project_title.strip()
        self.project_title = re.sub(r'<.*?>', '', self.project_title)
        self.project_title = self.project_title.replace('&amp;', '&')
        self.description = self.description.strip()
        self.description = re.sub(r'<.*?>', '', self.description)


class Education(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='education')
    qualification = RichTextField()
    start_date = models.DateField()
    end_date = models.DateField()
    university = RichTextField()
    university_address = RichTextField()
    completed = models.BooleanField()
    percentage = models.FloatField()

    panels = [FieldPanel('qualification'), FieldPanel('start_date'), FieldPanel('end_date'), FieldPanel('university'),
              FieldPanel('university_address'), FieldPanel('completed'), FieldPanel('percentage')]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-end_date')
        context['blogpages'] = blogpages
        return context

    def clean(self):
        self.university = self.university.strip()  # Remove leading and trailing whitespace
        self.university = re.sub(r'<.*?>', '', self.university)  # Remove HTML tags
        self.university = self.university.replace('&amp;', '&')
        self.qualification = self.qualification.strip()
        self.qualification = re.sub(r'<.*?>', '', self.qualification)
        self.qualification = self.qualification.replace('&amp;', '&')
        # self.about_university = self.about_university.strip()
        # self.about_university = re.sub(r'<.*>?', '', self.about_university)


class Professional(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='professional')
    skill_name = RichTextField()
    how_much_percentage = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])

    panels = [FieldPanel('skill_name'), FieldPanel('how_much_percentage')]

    def clean(self):
        self.skill_name = self.skill_name.strip()  # Remove leading and trailing whitespace
        self.skill_name = re.sub(r'<.*?>', '', self.skill_name)  # Remove HTML tags


class Experience(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='experience')
    company_name = RichTextField()
    designation = RichTextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    responsibilities = RichTextField()

    panels = [FieldPanel('company_name'), FieldPanel('designation'), FieldPanel('start_date'), FieldPanel('end_date'),
              FieldPanel('responsibilities')]

    def clean(self):
        self.designation = self.designation.strip()  # Remove leading and trailing whitespace
        self.designation = re.sub(r'<.*?>', '', self.designation)  # Remove HTML tags
        self.company_name = self.company_name.strip()
        self.company_name = re.sub(r'<.*?>', '', self.company_name)
        self.responsibilities = self.responsibilities.strip()
        self.responsibilities = re.sub(r'<.*?>', '', self.responsibilities)


class Testimonial(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='testimonial')
    thumbnail = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
    subtitle = RichTextField()
    title = RichTextField()
    designation = RichTextField()
    app_name = RichTextField()
    app_date = RichTextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = RichTextField()

    panel = [FieldPanel('thumbnail'), FieldPanel('subtitle'), FieldPanel('title'), FieldPanel('designation'),
             FieldPanel('app_name'), FieldPanel('app_date'), FieldPanel('rating'), FieldPanel('description')]

    def clean(self):
        self.subtitle = self.subtitle.strip()  # Remove leading and trailing whitespace
        self.subtitle = re.sub(r'<.*?>', '', self.subtitle)  # Remove HTML tags
        self.title = self.title.strip()
        self.title = re.sub(r'<.*?>', '', self.title)
        self.designation = self.designation.strip()
        self.designation = re.sub(r'<.*?>', '', self.designation)
        self.app_name = self.app_name.strip()
        self.app_name = re.sub(r'<.*?>', '', self.app_name)
        self.app_date = self.app_date.strip()
        self.app_date = re.sub(r'<.*?>', '', self.app_date)
        self.description = self.description.strip()
        self.description = re.sub(r'<.*?>', '', self.description)