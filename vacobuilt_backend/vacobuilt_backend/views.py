from rest_framework import viewsets
from .serializers import BlogSerializer, CategorySerializer
from .models import Blog, Category


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

    def destroy(self, request, *args, **kwargs):
        if kwargs.get('pk'):  
            return super().destroy(request, *args, **kwargs)
        else: 
            self.queryset.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer