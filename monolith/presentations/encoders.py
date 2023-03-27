from .models import Presentation
from events.encoders import ConferenceListEncoder
from common.json import ModelEncoder


class PresentationListEncoder(ModelEncoder):
    model = Presentation
    properties = ["title"]

    def get_extra_data(self, o):
        return {"status": o.status.name}


class PresentationDetailEncoder(ModelEncoder):
    model = Presentation
    properties = [
        "presenter_name",
        "company_name",
        "presenter_email",
        "title",
        "synopsis",
        "created",
        "conference",
    ]
    encoders = {
        "conference": ConferenceListEncoder(),
    }
