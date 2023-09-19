from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from Quillapi.models import Quote, Profile

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('id', 'text', 'author', 'user')

class QuoteView(ViewSet):
    def list(self, request):
        quotes = Quote.objects.all()
        serializer = QuoteSerializer(quotes, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            quote = Quote.objects.get(pk=pk)
            serializer = QuoteSerializer(quote, context={'request': request})
            return Response(serializer.data)
        except Quote.DoesNotExist:
            return HttpResponseServerError(ex)

    def create(self, request):
        new_quote = Quote()
        new_quote.text = request.data['text']
        new_quote.author = request.data['author']
        new_quote.user = Profile.objects.get(user=request.auth.user)
        new_quote.save()

        serializer = QuoteSerializer(new_quote, context={'request': request})

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        quote = Quote.objects.get(pk=pk)
        quote.text = request.data['text']
        quote.author = request.data['author']
        quote.user = Profile.objects.get(user=request.auth.user)
        quote.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        quote = Quote.objects.get(pk=pk)
        quote.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
