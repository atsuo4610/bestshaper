from rest_framework.decorators import api_view
from apps.models import Brassiere
import json


@api_view(['POST'])
def post_wash_num(request):
    bra = {'wash_num':request.POST['wash_num']}
    jsonData = json.loads(bra.decode('utf-8'))

    b = Brassiere(wash_num=jsonData)
    b.save()
