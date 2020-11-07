from rest_framework.response import Response
from rest_framework.views import APIView
import numexpr as ne


class Test(APIView):
    def get(self, request, f):
        try:
            evaluated = ne.evaluate(f)
            return Response(evaluated)
        except:
            return Response({"ERROR": "incorrect"})
