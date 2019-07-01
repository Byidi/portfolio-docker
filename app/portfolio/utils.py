def slugify(str):
    import re
    test = re.sub("[!@#$%^&*()[\]{};:,\\|./<>?|~\-=_+]", "", str)
    test = test.replace(' ','_')
    return test
