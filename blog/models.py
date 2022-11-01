"""Node model and Node admin interaction."""

from django import forms

from django.db import models

from modelcluster.fields import ParentalManyToManyField, ParentalKey

from wagtailmetadata.models import MetadataPageMixin
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.admin.panels import MultiFieldPanel, InlinePanel

from wagtail.fields import StreamField
from wagtail.models import Page, Orderable
from wagtail.search import index

from base.blocks import BaseStreamBlock
from base.models import Person
from wagtail.contrib.routable_page.models import RoutablePageMixin


class BlogPersonRelationship(Orderable, models.Model):
    """
    This defines the relationship between the `Person` within the `base`
    app and the BlogPage below. This allows people to be added to a BlogPage.
    We have created a two way relationship between BlogPage and Person using
    the ParentalKey and ForeignKey
    """

    page = ParentalKey(
        "Article", related_name="blog_person_relationship", on_delete=models.CASCADE
    )
    person = models.ForeignKey(
        "base.Person", related_name="person_blog_relationship", on_delete=models.CASCADE
    )
    panels = [FieldPanel("person")]


class BlogIndexPage(RoutablePageMixin, MetadataPageMixin, Page):
    """
    Index page for blogs.
    We need to alter the page model's context to return the child page objects,
    the BlogPage objects, so that it works as an index page

    RoutablePageMixin is used to allow for a custom sub-URL for the tag views
    defined above.
    """

    introduction = models.TextField(help_text="Text to describe the page", blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Landscape mode only; horizontal width between 1000px and 3000px.",
    )

    content_panels = Page.content_panels + [
        FieldPanel("introduction", classname="full"),
        FieldPanel("image"),
    ]

    # Speficies that only BlogPage objects can live under this index page
    subpage_types = ["Article"]

    # Defines a method to access the children of the page (e.g. BlogPage
    # objects). On the demo site we use this on the HomePage
    def children(self):
        return self.get_children().specific().live()

    # Overrides the context to list all child items, that are live, by the
    # date that they were published
    # https://docs.wagtail.org/en/stable/getting_started/tutorial.html#overriding-context
    def get_context(self, request):
        context = super(BlogIndexPage, self).get_context(request)
        context["posts"] = (
            Article.objects.descendant_of(self).live().order_by("-date")
        )
        return context

    def serve_preview(self, request, mode_name):
        # Needed for previews to work
        return self.serve(request)

    # Returns the child BlogPage objects for this BlogPageIndex.
    # If a tag is used then it will filter the posts by tag.
    def get_posts(self, tag=None):
        posts = Article.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    class Meta:
        verbose_name = "Category Page"
        verbose_name_plural = "Categories Pages"


class Article(MetadataPageMixin, Page):
    date = models.DateField("Post date")
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True, use_json_field=True
    )

    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('body'),
    ]
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Landscape mode only; horizontal width between 1000px and 3000px.",
    )

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel("image"),
        MultiFieldPanel([
            FieldPanel('date'),
        ], heading="Blog information"),
        InlinePanel(
            "blog_person_relationship", label="Author(s)", panels=None, min_num=1
        ),
    ]

    def authors(self):
        """
        Returns the BlogPage's related people. Again note that we are using
        the ParentalKey's related_name from the BlogPersonRelationship model
        to access these objects. This allows us to access the Person objects
        with a loop on the template. If we tried to access the blog_person_
        relationship directly we'd print `blog.BlogPersonRelationship.None`
        """
        return Person.objects.filter(live=True, person_blog_relationship__page=self)

    parent_page_types = ["BlogIndexPage"]

    # Specifies what content types can exist as children of BlogPage.
    # Empty list means that no child content types are allowed.
    subpage_types = []

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
