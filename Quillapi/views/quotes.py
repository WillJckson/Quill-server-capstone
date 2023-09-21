from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from Quillapi.models import Quote, QuillUser, QuoteCategory
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated  # Import IsAuthenticated

class QuoteUserSerializer(serializers.ModelSerializer):
    
    # user = UserSerializer(many=False)
    
    class Meta:
        model = QuillUser
        fields = ('id', 'user', 'bio', 'full_name', 'username')

class QuoteCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = QuoteCategory
        fields = ('id', 'category')

class QuoteSerializer(serializers.ModelSerializer):
    
    quill_user = QuoteUserSerializer(many=False)
    quote_category = QuoteCategorySerializer(many=False)
    class Meta:
        model = Quote
        fields = ('id', 'text', 'author', 'quill_user', 'quote_category')

class QuoteView(ViewSet):
    def list(self, request):
        quotes = Quote.objects.all()
        
        if "type" in request.query_params and request.query_params["type"] == "current":
            quill_user = QuillUser.objects.get(user=request.auth.user)
            quotes = Quote.objects.filter(quill_user=quill_user)
            
        serializer = QuoteSerializer(quotes, many=True)
        

        return Response(serializer.data)

    def retrieve(self, request, pk):
        
        quote = Quote.objects.get(pk=pk)
        
        serializer = QuoteSerializer(quote)
        return Response(serializer.data)

    def create(self, request):
        # Extract data from the request
        quill_user = QuillUser.objects.get(user=request.auth.user)
        quote_category = QuoteCategory.objects.get(pk=request.data["category"])

        # Create a new Quote object
        quote = Quote.objects.create(
            text=request.data["text"],
            author=request.data["author"],
            quill_user=quill_user,  # Assuming request.user is available
            quote_category=quote_category
        )

        # Serialize and return the created quote
        serializer = QuoteSerializer(quote)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        quote = Quote.objects.get(pk=pk)
        quote.text = request.data['text']
        quote.author = request.data['author']
        
        quote_category_data = request.data.get('category')
        if quote_category_data:
            quote_category = QuoteCategory.objects.get(pk=quote_category_data)
            quote.quote_category = quote_category
            
        quote.save()
        
        serializer = QuoteSerializer(quote)
        return Response(serializer.data)
    
    def destroy(self, request, pk=None):
        quote = Quote.objects.get(pk=pk)
        quote.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

