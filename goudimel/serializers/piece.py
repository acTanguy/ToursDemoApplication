from goudimel.models.piece import Piece
from goudimel.serializers.phrase import PhraseSerializer
from rest_framework import serializers

class PieceSerializer(serializers.HyperlinkedModelSerializer):
    book_id = serializers.RelatedField()
    phrases = PhraseSerializer()

    class Meta:
        model = Piece