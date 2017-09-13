def just_do_it(text):
    """Capitalize all words in <text>"""
    #return text.capitalize()
    # FIXED by unittest multiple words
    #return text.title()
    # FIXED by unittest about apostrophes
    from string import capwords
    return capwords(text)
