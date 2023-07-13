#!/usr/bin/python
"""defines Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """represent a review.
       attributes:
        place_id : The Place id.
        user_id : The User id.
        text : The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
