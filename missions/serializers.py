from rest_framework import serializers

from missions.models import Targets, Missions


class TargetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Targets
        fields = ('id', 'name', 'country', 'notes', 'is_completed')

    def update(self, instance, validated_data):
        if self.instance.is_completed:
            raise serializers.ValidationError("Can not update completed target")
        return super().update(instance, validated_data)


class MissionsSerializer(serializers.ModelSerializer):
    targets = TargetsSerializer(many=True)

    class Meta:
        model = Missions
        fields = ('id', 'cat', 'is_completed', 'targets')

    def create(self, validated_data):
        targets_data = validated_data.pop('targets')

        if len(targets_data) < 1 or len(targets_data) > 3:
            raise serializers.ValidationError("Mission must have between 1 and 3 targets")

        mission = Missions.objects.create(**validated_data)
        for target_data in targets_data:
            target_data['mission'] = mission
            Targets.objects.create(**target_data)

        return mission
