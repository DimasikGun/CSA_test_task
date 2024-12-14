from rest_framework import serializers

from spy_cats.models import SpyCats


class SpyCatsSerializer(serializers.ModelSerializer):
    salary = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)

    class Meta:
        model = SpyCats
        fields = '__all__'

    def update(self, instance, validated_data):
        unchangeable_fields = ['name', 'years_of_experience', 'breed']
        modified_fields = [field for field in unchangeable_fields if field in validated_data]

        if modified_fields:
            raise serializers.ValidationError({
                'detail': f'The following fields are read-only and cannot be updated: {modified_fields}'
            })
        return super().update(instance, validated_data)
