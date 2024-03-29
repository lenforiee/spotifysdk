from __future__ import annotations

from typing import Literal
from typing import TYPE_CHECKING

from pydantic import BaseModel

from .shared.copyright import Copyright
from .shared.external_urls import ExternalUrls
from .shared.image import Image
from .shared.paging_object import PagingObject

if TYPE_CHECKING:  # avoid circular imports
    from .chapters import SimplifiedChapter


class AudiobookCredit(BaseModel):
    name: str


class SimplifiedAudiobook(BaseModel):
    authors: list[AudiobookCredit]
    available_markets: list[str]
    copyrights: list[Copyright]
    description: str
    html_description: str
    edition: str
    explicit: bool
    external_urls: ExternalUrls
    href: str
    id: str
    images: list[Image]
    languages: list[str]
    media_type: str
    name: str
    narrators: list[AudiobookCredit]
    publisher: str
    type: Literal["audiobook"]
    uri: str
    total_chapters: int


class Audiobook(SimplifiedAudiobook):
    chapters: PagingObject[SimplifiedChapter]
