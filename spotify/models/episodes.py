from __future__ import annotations

from typing import Literal
from typing import Optional
from typing import TYPE_CHECKING

from pydantic import BaseModel

from .shared.external_urls import ExternalUrls
from .shared.image import Image
from .shared.restrictions import Restrictions
from .shared.resume_point import ResumePoint

if TYPE_CHECKING:  # avoid circular imports
    from .shows import SimplifiedShow


class SimplifiedEpisode(BaseModel):
    audio_preview_url: Optional[str] = None
    description: str
    html_description: str
    duration_ms: int
    explicit: bool
    external_urls: ExternalUrls
    href: str
    id: str
    images: list[Image]
    is_externally_hosted: bool
    is_playable: bool
    languages: list[str]
    name: str
    release_date: str
    release_date_precision: Literal["year", "month", "day"]
    resume_point: ResumePoint
    type: Literal["episode"]
    uri: str
    restrictions: Optional[Restrictions] = None


class Episode(SimplifiedEpisode):
    show: SimplifiedShow
