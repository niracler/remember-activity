import xadmin
from .models import Images


class ImagesAdmin(object):
    list_display = ["name", "image", "add_time"]
    search_fields = ['name', ]
    list_filter = ["name", "add_time"]

xadmin.site.register(Images, ImagesAdmin)
