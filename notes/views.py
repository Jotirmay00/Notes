from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Note, NoteChange
from .serializers import NoteSerializer, NoteChangeSerializer,UserSerializer

class UserRegistrationView(generics.CreateAPIView):

   # Create a new user.

    serializer_class = UserSerializer

class UserLoginView(ObtainAuthToken):

   # Log a user in and return a token.
    
    def post(self, request, *args, **kwargs):

        # Override the post method to return a custom response.
        
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_id': user.id, 'username': user.username})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoteCreateView(generics.CreateAPIView):
    
    # Create a new note and associate it with the current user.
    
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):

       # Set the owner of the note to the current user.
        
        serializer.save(owner=self.request.user)

class NoteDetailView(generics.RetrieveAPIView):

    # Retrieve a note's details.
    
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated,)

    async def get_object(self):
        
       # Check if the current user has permission to access the note.
        
        obj = await super().get_object()
        if self.request.user != obj.owner and self.request.user not in obj.shared_with.all():
            raise PermissionDenied("You don't have permission to access this note.")
        return obj

class NoteShareView(generics.UpdateAPIView):

   # Share a note with other users.

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated,)

    def perform_update(self, serializer):

       # Update the shared_with field of the note.
        
        instance = serializer.instance
        shared_with = self.request.data.get('shared_with', [])
        instance.shared_with.set(shared_with)
        serializer.save()

class NoteUpdateView(generics.UpdateAPIView):
    
    # Update a note and track changes.

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated,)

    async def perform_update(self, serializer):

       # Update the note and track changes.
        
        instance = serializer.instance
        user = self.request.user
        if user != instance.owner and user not in instance.shared_with.all():
            raise PermissionDenied("You don't have permission to update this note.")
        # Track changes
        NoteChange.objects.create(note=instance, content=serializer.validated_data['content'], user=user)

class NoteVersionHistoryView(generics.ListAPIView):
    
   # Retrieve a note's version history.
    
    serializer_class = NoteChangeSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):

       # Check if the current user has permission to access the note's version history.
        
        note_id = self.kwargs['id']
        note = Note.objects.get(pk=note_id)
        user = self.request.user
        if user != note.owner and user not in note.shared_with.all():
            raise PermissionDenied("You don't have permission to access this note's version history.")
        return note.changes.all()
