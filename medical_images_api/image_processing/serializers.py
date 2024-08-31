from rest_framework import serializers
from .models import MedicalImageResult

class MedicalImageResultSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)  # permite que 'id' sea opcional

    class Meta:
        model = MedicalImageResult
        fields = '__all__'  # esto permite crear o listar todos los campos

    def validate_mean_before_normalization(self, value):
        # valida que la media antes de la normalización no sea negativa
        if value < 0:
            raise serializers.ValidationError("La media antes de la normalización no puede ser negativa.")
        return value

    def validate_mean_after_normalization(self, value):
        # valida que la media después de la normalización no sea negativa
        if value < 0:
            raise serializers.ValidationError("La media después de la normalización no puede ser negativa.")
        return value

    def validate_data_size(self, value):
        # valida que el tamaño de los datos sea positivo
        if value <= 0:
            raise serializers.ValidationError("El tamaño de los datos debe ser un valor positivo.")
        return value

    def validate_raw_data(self, value):
        # valida que los datos sin procesar no estén vacíos
        if not value:
            raise serializers.ValidationError("Los datos sin procesar no pueden estar vacíos.")
        return value

    def validate(self, data):
        # validación personalizada para asegurar la coherencia entre 'data_size' y 'raw_data'
        if 'data_size' in data and 'raw_data' in data:
            if data['data_size'] != len(data['raw_data']):
                raise serializers.ValidationError("El tamaño de los datos no coincide con la longitud de 'raw_data'.")
        return data


class MedicalImageResultUpdateSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)  # permite que 'id' sea opcional si se requiere
    device_name = serializers.CharField(required=True)  # asegura que device_name sea obligatorio

    class Meta:
        model = MedicalImageResult
        fields = ['id', 'device_name']  # solo permite actualizar el id y el nombre del dispositivo


class MedicalImageResultGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalImageResult
        fields = ['device_name', 'mean_before_normalization', 'mean_after_normalization', 'data_size', 'raw_data']
        # esto muestra solo los campos esenciales para la operación de lectura
