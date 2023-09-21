# from rest_framework.response import Response
# from rest_framework import serializers, status
# from rest_framework.viewsets import ViewSet
# from Quillapi.models import QuillUser

# class QuillUserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = QuillUser
#         fields = ('id', 'user', 'bio', 'full_name', 'username')

# class QuillUserView(ViewSet):

#     def retrieve(self, request, pk):
#         quill_user = QuillUser.objects.get(pk=pk)
#         serializer = QuillUserSerializer(quill_user)
#         return Response(serializer.data)

#     def list(self, request):
#         quill_users = QuillUser.objects.all()
#         serializer = QuillUserSerializer(quill_users, many=True)
#         return Response(serializer.data)
