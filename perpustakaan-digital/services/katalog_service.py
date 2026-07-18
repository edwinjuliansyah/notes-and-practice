from models.media import Media
class KatalogService:
    def __init__(self):
        self.katalog: dict[str, Media] = {}

    def tambah_media(self, media: Media):
        self.katalog[media.id_media] = media
        return True
    
    def cari_by_id(self, id_media):
        return self.katalog.get(id_media)