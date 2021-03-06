from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils.http import urlencode
from rest_framework import status
from rest_framework.test import APITestCase

from games.models import GameCategory


class GameCategoryTests(APITestCase):
    def create_game_category(self, name):
        url = reverse('gamecategory-list')
        data = {'name': name}
        resp = self.client.post(url, data, format='json')
        return resp

    def test_create_and_retrieve_game_category(self):
        new_game_category_new = 'New Game Category'
        resp = self.create_game_category(new_game_category_new)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(GameCategory.objects.count(), 1)
        self.assertEqual(GameCategory.objects.get().name,
                         new_game_category_new)
        print("PK {0}".format(GameCategory.objects.get().pk))

    def test_create_duplicated_game_category(self):
        url = reverse('gamecategory-list')
        new_game_category_new = 'New Game Category'
        date = {'name': new_game_category_new}
        resp1 = self.create_game_category(new_game_category_new)
        self.assertEqual(resp1.status_code, status.HTTP_201_CREATED)
        resp2 = self.create_game_category(new_game_category_new)
        self.assertEqual(resp2.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_game_categories_list(self):
        new_game_category_name = 'New Game Category'
        self.create_game_category(new_game_category_name)
        url = reverse('gamecategory-list')
        resp = self.client.get(url, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['count'], 1)
        self.assertEqual(resp.data['results'][0]['name'],
                         new_game_category_name)

    def test_update_game_category(self):
        new_game_category_name = 'Initial Name'
        resp = self.create_game_category(new_game_category_name)
        url = reverse('gamecategory-detail',
                      None,
                      {resp.data['pk']})
        updated_game_category_name = 'Updated Game Category Name'
        data = {'name': updated_game_category_name}
        path_resp = self.client.patch(url, data, format='json')
        self.assertEqual(path_resp.status_code,
                         status.HTTP_200_OK)
        self.assertEqual(path_resp.data['name'],
                         updated_game_category_name)

    def test_filter_game_category_by_name(self):
        game_category_name1 = 'First game category name'
        self.create_game_category(game_category_name1)
        game_category_name2 = 'Second game category name'
        self.create_game_category(game_category_name2)
        filter_by_name = {'name': game_category_name1}
        url = '{0}?{1}'.format(reverse('gamecategory-list'),
                               urlencode(filter_by_name))
        resp = self.client.get(url, format='json')
        self.assertEqual(
            resp.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(resp.data['count'], 1)
        self.assertEqual(
            resp.data['results'][0]['name'],
            game_category_name1
        )