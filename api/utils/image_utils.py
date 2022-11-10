import os

# Renaming school logo
def rename_image(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_image.%s" % (instance.id, ext)
    return os.path.join('image', filename)