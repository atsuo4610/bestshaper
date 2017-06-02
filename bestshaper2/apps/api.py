from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.models import Brassiere
import json


@api_view(['GET','POST'])
def post_wash_num(request):
    print("OK")
    # bra = request.data['wash_num']w
    # jsonData = json.loads(bra.decode('utf-8'))

    print(request.data['bra_name'])

    # b = Brassiere(bra_name=request.data['bra_name'], wash_num=request.data['wash_num'])

    b = Brassiere.objects.get(pk='1')
    b.wash_num += 1
    b.save()
    return Response()
