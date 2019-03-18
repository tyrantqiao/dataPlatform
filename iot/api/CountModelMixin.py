from rest_framework.decorators import action
from rest_framework.response import Response

class CountModelMixin(object):
    """
    根据条件返回count值
    """
    @action(detail=False)
    def count(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        content = {'count': queryset.count()}
        return Response(content)
