import datetime
from pytz import utc
from .models import Survey

def auth_middleware(get_response):
    def middleware(request):
        s = Survey.objects.all()
        for i in s:
            now = datetime.datetime.utcnow().replace(tzinfo=utc)
            timediff = now - i.created_at
            if timediff.days >= 1:
                i.is_active = False
                i.save()
                # print("hii ", po
        response = get_response(request)
        print('++++++++++++++++++++++')
        return response
    return middleware