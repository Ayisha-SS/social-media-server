from django.http import JsonResponse
from django.contrib.contenttypes.models import ContentType
from posts.models import CreatePost, ViewPost


def contenttype_view(request):
    createpost_ct = ContentType.objects.get_for_model(CreatePost)
    viewpost_ct = ContentType.objects.get_for_model(ViewPost)

    return JsonResponse({
        'CreatePost ContentType ID': createpost_ct.id,
        'ViewPost ContentType ID': viewpost_ct.id
    })