from rest_framework import serializers
from .models import Singer,Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields = '__all__'





class SingerSerializer(serializers.ModelSerializer):
    sungby = SongSerializer(many=True,read_only=True)
    # song = serializers.StringRelatedField(many=True,read_only=True)
    # song = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # song = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='song-detail')
    # song = serializers.SlugRelatedField(many=True,read_only=True,slug_field='duration')
    # song = serializers.HyperlinkedIdentityField(many=True,read_only=True,view_name='song-detail')
    
    class Meta:
        model=Singer
        fields= ['id','name','gender','sungby']