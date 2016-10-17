from rest_framework import status
from rest_framework.test import APITestCase

from shop_rest_api.models import Item, Review


def _create_item(name):
    item = Item(name=name)
    item.save()
    return item


def _create_review(item, author_name, author_email):
    review = Review(item=item, author_name=author_name,
                    author_email=author_email, rating=4,
                    content="Foo bar baz")
    return review


def _create_item_reviews(item):
    reviews = []
    for i in range(3):
        review = _create_review(item, "Author_%s" % i, "author%s@example.com" % i)
        review.save()
        reviews.append(review)
    return reviews


class ItemTests(APITestCase):
    def test_get_item(self):
        item_name = "TestItem"
        item = _create_item(item_name)

        response = self.client.get('/items/%s/' % item.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(item.id, response.data.get('id'))

    def test_item_reviews(self):
        item = _create_item('TestName')
        reviews = _create_item_reviews(item)

        response = self.client.get('/items/%s/' % item.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get('reviews')), len(reviews))


class ReviewTests(APITestCase):
    def test_create_review(self):
        item = _create_item("TestName")
        data = {"author_name": "AuthorName",
                "author_email": "a@a.com",
                "content": "Foo Bar Baz",
                "rating": 3,
                "item": item.id}

        response = self.client.post("/reviews/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["item"], data["item"])
