from django.test import TestCase

from lists.models import Item


class HomePageTest(TestCase):
    def test_uses_home_template(self) -> None:
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_can_save_a_post_request(self) -> None:
        response = self.client.post("/", data={"item_text": "A new list item"})
        self.assertContains(response, "A new list item")
        self.assertTemplateUsed(response, "home.html")


class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self) -> None:
        first_item = Item()
        first_item.text = "The first (ever) list item"
        first_item.save()

        first_item = Item()
        first_item.text = "Item the second"
        first_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)  # noqa: PT009

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, "The first (ever) list item")  # noqa: PT009
        self.assertEqual(second_saved_item.text, "Item the second")  # noqa: PT009
