from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from lists.views import home_page


class HomePageTest(TestCase):
    def test_rool_url_resolve_to_home_page_view(self) -> None:
        found = resolve("/")
        self.assertEqual(found.func, home_page)  # noqa: PT009

    def test_home_page_returns_correct_html(self) -> None:
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode("utf8")
        self.assertTrue(html.startswith("<html>"))  # noqa: PT009
        self.assertIn("<title>To-Do lists</title>", html)  # noqa: PT009
        self.assertTrue(html.endswith("</html>"))  # noqa: PT009
