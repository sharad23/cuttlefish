from experiment.models import TestModel
from experiment.serializer import TestSerializer
from helpers.test_mixins import TestSerializerMixin


class SerializerTest(TestSerializerMixin):
    request = None
    format_kwarg = None
    data = {'name': 'sharad'}
    serializer = TestSerializer
    model = TestModel

    def test_serializer_validation(self):
        super(SerializerTest, self).serializer_validation()

    def test_serializer_create(self):
        super(SerializerTest, self).serializer_create()

    def test_serializer_update(self):
        obj = TestModel.objects.create(name='apple')
        data = {'name': 'ball', 'obj': obj}
        super(SerializerTest, self).serializer_update(**data)

    def test_deserialization(self):
        obj = TestModel.objects.create(name='apple')
        data = {'obj': obj}
        super(SerializerTest, self).deserialization(**data)
