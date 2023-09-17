from django.test import TestCase

from lists.models import Item


class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_can_save_a_post_request(self):
        self.client.post("/", data={"item_text": "A new list item"})
        self.assertEqual(Item.objects.count(), 1)  # noqa: PT009
        new_item = Item.objects.first()
        if new_item is not None:
            self.assertEqual(new_item.text, "A new list item")  # noqa: PT009
        else:
            self.fail("First item not found")

    def test_redirects_after_post(self):
        response = self.client.post("/", data={"item_text": "A new list item"})
        self.assertRedirects(response, "/")

    def test_displays_all_list_items(self):
        Item.objects.create(text="itemey 1")
        Item.objects.create(text="itemey 2")

        response = self.client.get("/")

        self.assertContains(response, "itemey 1")
        self.assertContains(response, "itemey 2")


class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
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

    def test_only_saves_items_when_necessary(self):
        self.client.get("/")
        self.assertEqual(Item.objects.count(), 0)  # noqa: PT009
