import xadmin
from .models import Images


class ImagesAdmin(object):
    list_display = ["id", "image", "add_time"]
    search_fields = ['id', ]
    list_filter = ["id", "add_time"]


xadmin.site.register(Images, ImagesAdmin)
