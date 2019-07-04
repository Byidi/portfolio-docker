def slugify(str):
    import re
    slug = re.sub("[!@#$%^&*()[\]{};:,\\|./<>?|~=+]", "", str)
    slug = test.replace(' ','_')
    return slug
