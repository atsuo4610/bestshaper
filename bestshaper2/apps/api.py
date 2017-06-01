from rest_framework.decorators import api_view
from apps.models import Brassiere
import json


@api_view(['POST'])
def post_wash_num(request):

    bra = request.POST.get['wash_num', 1]
    jsonData = json.loads(bra.decode('utf-8'))

    b = Brassiere(jsonData)
    b.save()
