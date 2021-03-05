from django.utils.text import slugify

def unique_slug_generator(model_instance,title,slug_field):
    '''
    this view for generate unique slug field
    :param model_instance:
    :param title:
    :param slug_field:
    :return:
    '''
    slug = slugify(title)
    modeld_class = model_instance.__class__
    while modeld_class._default_manager.filter(slug=slug).exists():
        object_pk = modeld_class._default_manager.latest('pk')
        object_pk = object_pk.pk + 1
        slug = f'{slug}-{object_pk}'
    return slug
