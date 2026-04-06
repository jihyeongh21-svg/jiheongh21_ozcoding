from models import Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["author", "created_at", "updated_at"]

    def validate_content(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("댓글 내용은 10자 이상이어야 합니다.")
        return value  # 추가 validation 베스트 프랙티스
