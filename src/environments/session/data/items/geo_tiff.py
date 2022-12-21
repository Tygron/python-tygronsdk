from . import Item

class GeoTiff(Item):

    @property
    def uploader_name(self):
        return self._data.get( 'uploaderName', None )