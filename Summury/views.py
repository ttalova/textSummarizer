from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, action
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from rest_framework.views import APIView

from .serializers import MethodSerializer
from . import frequency_analysis, cosine_distance, tf_idf


class MethodView(APIView):
    permission_classes = (AllowAny, )
    serializer_class = MethodSerializer
    renderer_classes = (JSONRenderer,)

    @swagger_auto_schema(
        request_body=serializer_class,
        responses={
            201: 'Created',
            400: 'Bad Request',
            403: 'Forbidden'
        }
    )
    def post(self, request, *args, **kwargs):
        id = self.kwargs["id"]
        serializer = MethodSerializer(data=request.data)
        if serializer.is_valid():
            text = request.data['text']
            if id == 1:
                sum_text = frequency_analysis.main(text)
            elif id == 2:
                sum_text = cosine_distance.main(text)
            elif id == 3:
                sum_text = tf_idf.main(text)

            return Response(sum_text, status=status.HTTP_201_CREATED, )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

