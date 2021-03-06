#!/usr/bin/env python3
"""
    this file deals with any image that comes in.

    it currently just inserts the image with a caption saying the title and author.
"""

from   jinja2 import Environment
from  .render import fill

def main(text, meta={}, env=Environment()):
    """
        this is the driver for poem typesetting.
        text is the text of the poem.
        meta is metadata, eg, author, title, bio.
        env is a jinja2 environment.
    """
    lines_out = fill("image.tex", env=env, meta=meta)
    return lines_out

if __name__ == "__main__":
    POEM = open("my_fucking_restaurant.tex").read()
    print(main(POEM))
        #insert each one into the index
