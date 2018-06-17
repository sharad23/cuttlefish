from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from experiment.models import TestModel
from experiment.serializer import TestSerializer


class TestViewSet(ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer

    def list(self, request, *args, **kwargs):
        result = TestModel.get_all()
        print(result)
        return super(TestViewSet, self).list(request, *args, **kwargs)

