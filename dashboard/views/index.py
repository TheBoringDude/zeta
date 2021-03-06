from dashboard.models.collections import Collections
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View


@method_decorator(login_required, name="dispatch")
class IndexDashboardView(View):
    """
    Dashboard > Index (Main) View
    """

    template_name = "main/index.html"

    def get(self, request, *args, **kwargs):
        # query the collections
        collections = Collections.objects.filter(owner=request.user)

        # query each type
        movies = collections.filter(type="movie")
        series = collections.filter(type="series")
        animes = collections.filter(type="anime")
        books = collections.filter(type="book")
        mangas = collections.filter(type="manga")
        asian_dramas = collections.filter(type="asian drama")

        # render
        return render(
            request,
            self.template_name,
            {
                "col_count": collections.count(),
                "collections": [
                    {"name": "movies", "title": "Movies", "collections": movies},
                    {"name": "series", "title": "Series", "collections": series},
                    {"name": "animes", "title": "Animes", "collections": animes},
                    {"name": "books", "title": "Books", "collections": books},
                    {"name": "mangas", "title": "Mangas", "collections": mangas},
                    {
                        "name": "asian_dramas",
                        "title": "Asian Dramas",
                        "collections": asian_dramas,
                    },
                ],
            },
        )
