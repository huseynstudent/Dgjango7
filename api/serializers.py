from rest_framework import serializers

from blog.models import Post, Category, Tag

# Serializer = model obyekti ⇄ JSON tərcüməçisi.
#   obyekt → dict  (GET):   PostSerializer(post).data
#   JSON → obyekt  (POST):  PostSerializer(data=request.data) → is_valid() → save()
# Dərs 11-dəki ModelForm ilə eyni fikirdir: sahələri modeldən özü götürür, yoxlayır, bazaya yazır.
#
# Nişanlar:  [DƏRS 14] müəllim · [DƏRS 14] praktikadan sonra müəllim · [PRAKTİKA 14] tələbə · [EV 14] tapşırıq 1–3 / bonus · [REFERANS 14] tələbəyə verilmir


# [DƏRS 14] müəllim yazır
class PostSerializer(serializers.ModelSerializer):
    comment_count = serializers.SerializerMethodField()

    def get_comment_count(self, post):
        return post.comments.filter(is_active=True).count()

    class Meta:
        model = Post                                              # hansı model (ModelForm-dakı kimi)
        fields = [                                                # JSON-da hansı sahələr olsun
            "id", "title", "author", "category", "tags",
            "content", "image", "is_published", "views", "created_at",
            "comment_count",
        ]
        read_only_fields = ["views", "created_at"]                # yalnız oxunur — POST-da göndərilsə də, nəzərə alınmır


# [PRAKTİKA 14] — PostSerializer-in əkizi
class CategorySerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField()

    def get_post_count(self, category):
        return category.posts.filter(is_published=True).count()

    class Meta:
        model = Category
        fields = ["id", "name", "slug", "description", "post_count"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name", "slug"]
