from models.media import Media
class KatalogService:
    def __init__(self) -> None:
        self.katalog: dict[str, Media] = {}

    def tambah_media(self, media: Media) -> bool:
        self.katalog[media.id_media] = media
        return True
    
    def cari_by_id(self, id_media: str) -> Media | None:
        return self.katalog.get(id_media)
    
    def hapus_media(self, id_media: Media) -> bool:
        if id_media in self.katalog:
            del self.katalog[id_media]
            return True
        else:
            return False