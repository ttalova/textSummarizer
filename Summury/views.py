from django.shortcuts import render
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
    def get(self,  request, *args, **kwargs):
        return render(request, 'home.html')
    def post(self, request, *args, **kwargs):
        ids = [1, 2, 3]
        serializer = MethodSerializer(data=request.data)
        sum_text_1 = ''
        sum_text_2 = ''
        sum_text_3 = ''
        if serializer.is_valid():
            text = request.data['text']
            for id in ids:
                if id == 1:
                    sum_text_1 = frequency_analysis.main(text)
                elif id == 2:
                    sum_text_2 = cosine_distance.main(text)
                elif id == 3:
                    sum_text_3 = tf_idf.main(text)

            data = {
                'text': text,
                'sum_text_1': sum_text_1,
                'sum_text_2': sum_text_2,
                'sum_text_3': sum_text_3
            }
            return render(request, 'result.html', data)
        return render(request, 'home.html')

