from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import MedicalImageResult
from .serializers import (
    MedicalImageResultSerializer,
    MedicalImageResultUpdateSerializer,
    MedicalImageResultGetSerializer,
)

# APIView para listar y crear resultados de imágenes médicas
class MedicalImageResultListCreateAPIView(APIView):

    @swagger_auto_schema(
        operation_description="Retrieve a list of all medical image results.",
        responses={200: MedicalImageResultGetSerializer(many=True)}
    )
    def get(self, request):
        """
        Retorna una lista de todos los resultados de imágenes médicas almacenados
        """
        elements = MedicalImageResult.objects.all() # Recupera todos los registros en la base de datos
        serializer = MedicalImageResultGetSerializer(elements, many=True) # Serializa los datos para la respuesta
        return Response(serializer.data, status=status.HTTP_200_OK) # Retorna los datos serializados en la respuesta

    @swagger_auto_schema(
        operation_description="Create a new medical image result.",
        request_body=MedicalImageResultSerializer,
        responses={201: MedicalImageResultSerializer, 400: 'Bad Request'}
    )
    def post(self, request):
        """
        Crea un nuevo resultado de imagen médica en la base de datos
        """
        serializer = MedicalImageResultSerializer(data=request.data) # Serializa los datos recibidos
        if serializer.is_valid(): # Valida los datos antes de guardarlos
            serializer.save() # Guarda los datos si son válidos
            return Response(serializer.data, status=status.HTTP_201_CREATED) # Retorna los datos guardados
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Retorna errores si los datos no son válidos

# APIView para operaciones CRUD en un resultado de imagen médica específico
class MedicalImageResultDetailAPIView(APIView):

    @swagger_auto_schema(
        operation_description="Retrieve a specific medical image result by ID.",
        responses={200: MedicalImageResultGetSerializer, 404: 'Not Found'}
    )
    def get(self, request, id=None):
        """
        Recupera un resultado de imagen médica específico por ID
        """
        try:
            element = MedicalImageResult.objects.get(id=id) # Intenta recuperar el objeto por su ID
            serializer = MedicalImageResultGetSerializer(element) # Serializa los datos del objeto
            return Response(serializer.data, status=status.HTTP_200_OK) # Retorna los datos serializados
        except MedicalImageResult.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND) # Retorna un error si no se encuentra el objeto

    @swagger_auto_schema(
        operation_description="Update an existing medical image result by ID.",
        request_body=MedicalImageResultUpdateSerializer,
        responses={200: MedicalImageResultUpdateSerializer, 404: 'Not Found', 400: 'Bad Request'}
    )
    def patch(self, request, id=None):
        """
            - Actualiza un resultado de imagen médica existente por su ID.
            - Solo se permite actualizar el ID y el nombre del dispositivo.
        """
        try:
            element = MedicalImageResult.objects.get(id=id) # Intenta recuperar el objeto por su ID
        except MedicalImageResult.DoesNotExist:
            return Response({'error': 'Medical image result not found'}, status=status.HTTP_404_NOT_FOUND) # Retorna un error si no se encuentra el objeto

        serializer = MedicalImageResultUpdateSerializer(element, data=request.data, partial=True) # Serializa los datos para la actualización
       
        # Validación adicional en la vista para asegurar que los datos son correctos
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # Verificar si hay campos no permitidos en la actualización
        non_editable_fields = set(request.data.keys()) - {'id', 'device_name'}
        if non_editable_fields:
            return Response(
                {"detail": f"No se pueden editar los siguientes campos: {', '.join(non_editable_fields)}"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer.save() # Guarda los cambios si todo es válido
        return Response(serializer.data, status=status.HTTP_200_OK) # Retorna los datos actualizados
    
    @swagger_auto_schema(
        operation_description="Delete a specific medical image result by ID.",
        responses={204: 'Deleted successfully.', 404: 'Not Found'}
    )
    def delete(self, request, id=None):
        """
        Elimina un resultado de imagen médica específico por su ID.
        """
        try:
            element = MedicalImageResult.objects.get(id=id) # Intenta recuperar el objeto por su ID
        except MedicalImageResult.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND) # Retorna un error si no se encuentra el objeto

        element.delete() # Elimina el objeto si se encuentra
        return Response({'detail': 'Deleted successfully.'}, status=status.HTTP_204_NO_CONTENT) # Retorna un mensaje de éxito
