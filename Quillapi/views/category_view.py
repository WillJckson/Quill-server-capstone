from rest_framework import viewsets
from Quillapi.models import QuoteCategory
from rest_framework import serializers
from rest_framework.response import Response

class QuoteCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = QuoteCategory
        fields = ('id', 'category')

class CategoryView(viewsets.ModelViewSet):
    queryset = QuoteCategory.objects.all()
    serializer_class = QuoteCategorySerializer
    
    def retrieve(self, request, pk):
        category = QuoteCategory.objects.get(pk=pk)
        serializer = QuoteCategorySerializer(category)
        return Response(serializer.data)

    
def list(self, request):
    categories = QuoteCategory.objects.all()
    serializer = QuoteCategorySerializer(categories, many=True)
    return Response(serializer.data)

    
    
# quote.category = QuoteCategory.objects.get(category=request.auth.user)
# quote.quote_category = request.data['quote_category']