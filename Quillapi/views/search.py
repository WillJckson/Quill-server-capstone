from django.http import JsonResponse
from Quillapi.models import Quote

def search_view(request):
    query = request.GET.get('q')
    
    # Perform search based on the query
    if query:
        search_results = Quote.objects.filter(text__icontains=query)
    else:
        # If no query is provided, return all quotes
        search_results = Quote.objects.all()

    # Serialize search results
    results_data = [{'text': quote.text, 'author': quote.author} for quote in search_results]
    
    return JsonResponse({'results': results_data})