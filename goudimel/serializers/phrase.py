from goudimel.models.phrase import Phrase

from rest_framework import serializers

class PhraseSerializer(serializers.HyperlinkedModelSerializer):
    piece_id = serializers.RelatedField()
    

    class Meta:
        model = Phrase