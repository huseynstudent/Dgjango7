from django.urls import path

from . import views

app_name = "api"

# config/urls.py-da:  path("api/", include("api.urls"))  →  buradakı hər ünvanın əvvəlinə /api/ gəlir.
# REST qaydası: ünvan İSİMdir (posts), fel deyil (get_posts, delete_post). Nə ediləcəyini HTTP metodu deyir.
#
#   GET    /api/posts/      siyahı            GET    /api/posts/3/   bir post
#   POST   /api/posts/      yeni post         PUT    /api/posts/3/   dəyiş
#                                             DELETE /api/posts/3/   sil
urlpatterns = [
    # [DƏRS 14]
    path("posts/", views.post_list, name="post_list"),
    path("posts/<int:post_id>/", views.post_detail, name="post_detail"),

    # [PRAKTİKA 14] tələbə · [DƏRS 14] category_detail-i praktikadan sonra müəllim
    path("categories/", views.category_list, name="category_list"),
    path("categories/<int:category_id>/", views.category_detail, name="category_detail"),

    path("tags/", views.tag_list, name="tag_list"),
    path("tags/<int:tag_id>/", views.tag_detail, name="tag_detail"),
    path("stats/", views.stats, name="stats"),

]
