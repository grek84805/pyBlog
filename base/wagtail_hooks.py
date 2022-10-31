from base.models import Person
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)


class PersonModelAdmin(ModelAdmin):
    model = Person
    menu_label = "People"  # ditch this to use verbose_name_plural from model
    menu_icon = "user"  # change as required
    list_display = ("first_name", "last_name", "job_title", "thumb_image")
    list_filter = ("job_title",)
    search_fields = ("first_name", "last_name", "job_title")
    inspect_view_enabled = True


class PyBlogModelAdminGroup(ModelAdminGroup):
    menu_label = "PyBlog Misc"
    menu_icon = "pilcrow"  # change as required
    menu_order = 300  # will put in 4th place (000 being 1st, 100 2nd)
    items = (PersonModelAdmin,)


# When using a ModelAdminGroup class to group several ModelAdmin classes together,
# you only need to register the ModelAdminGroup class with Wagtail:

modeladmin_register(PyBlogModelAdminGroup)
