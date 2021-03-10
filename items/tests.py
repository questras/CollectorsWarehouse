from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from .models import CollectionSet, Item

User = get_user_model()


class TestUserObjectFactory:
    def __init__(self):
        # Counter of created user objects.
        self.counter = 0

    def create_user(self) -> User:
        email = f'testUser{self.counter}@test.com'
        first_name = f'testFirstName{self.counter}'
        last_name = f'testLastName{self.counter}'
        password = f'testPassword{self.counter}'

        self.counter += 1

        return User.objects.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )


class CollectionSetModelTests(TestCase):
    def setUp(self) -> None:
        self.userFactory = TestUserObjectFactory()
        self.cset_owner = self.userFactory.create_user()
        self.cset = CollectionSet.objects.create(
            name='testCSet',
            owner=self.cset_owner
        )

    def test_add_item_item_of_same_owner(self):
        """Test whether item of collection set owner can be added
        to collection set."""

        item = Item.objects.create(
            name='testItem',
            owner=self.cset_owner
        )
        self.cset.add_item(item)
        self.assertEqual(self.cset.items.all().count(), 1)

    def test_add_item_item_of_different_owner(self):
        """Test whether item owned by different owner can be added
        to collection set."""

        different_user = self.userFactory.create_user()
        item = Item.objects.create(
            name='testItem',
            owner=different_user
        )
        with self.assertRaises(ValidationError):
            self.cset.add_item(item)
