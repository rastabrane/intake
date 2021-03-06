from unittest import TestCase
from django.core.paginator import Paginator
from intake import utils


class TestGetPageNavigationCounter(TestCase):

    def run_case(self, full_range, wing_size, pages):
        page_size = 5
        fake_objects = list(range(len(full_range) * page_size))
        paginator = Paginator(fake_objects, page_size)
        for page_number, expected_result in pages.items():
            page = paginator.page(page_number)
            result = utils.get_page_navigation_counter(page, wing_size)
            self.assertEqual(result, expected_result)

    def test_target_situation(self):
        self.run_case(
            full_range=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
            wing_size=4,
            pages={
                1:  [1,      2,   3,   4,   5,   6,   7, 'jump',  13],
                2:  [1,      2,   3,   4,   5,   6,   7, 'jump',  13],
                3:  [1,      2,   3,   4,   5,   6,   7, 'jump',  13],
                4:  [1,      2,   3,   4,   5,   6,   7, 'jump',  13],
                5:  [1,      2,   3,   4,   5,   6,   7, 'jump',  13],
                6:  [1, 'jump',   4,   5,   6,   7,   8, 'jump',  13],
                7:  [1, 'jump',   5,   6,   7,   8,   9, 'jump',  13],
                8:  [1, 'jump',   6,   7,   8,   9,  10, 'jump',  13],
                9:  [1, 'jump',   7,   8,   9,  10,  11,     12,  13],
                10: [1, 'jump',   7,   8,   9,  10,  11,     12,  13],
                11: [1, 'jump',   7,   8,   9,  10,  11,     12,  13],
                12: [1, 'jump',   7,   8,   9,  10,  11,     12,  13],
                13: [1, 'jump',   7,   8,   9,  10,  11,     12,  13]
            }
        )

    def test_even_steven(self):
        self.run_case(
            full_range=[1, 2, 3, 4, 5, 6, 7, 8],
            wing_size=3,
            pages={
                1:  [1,      2,   3,   4,   5, 'jump',   8],
                2:  [1,      2,   3,   4,   5, 'jump',   8],
                3:  [1,      2,   3,   4,   5, 'jump',   8],
                4:  [1,      2,   3,   4,   5, 'jump',   8],
                5:  [1, 'jump',   4,   5,   6,      7,   8],
                6:  [1, 'jump',   4,   5,   6,      7,   8],
                7:  [1, 'jump',   4,   5,   6,      7,   8],
                7:  [1, 'jump',   4,   5,   6,      7,   8]
            }
        )

    def test_not_long_enough(self):
        self.run_case(
            full_range=[1, 2, 3, 4, 5, 6, 7],
            wing_size=0,
            pages={
                1:  [1, 2, 3, 4, 5, 6, 7],
                2:  [1, 2, 3, 4, 5, 6, 7],
                3:  [1, 2, 3, 4, 5, 6, 7],
                4:  [1, 2, 3, 4, 5, 6, 7],
                5:  [1, 2, 3, 4, 5, 6, 7],
                6:  [1, 2, 3, 4, 5, 6, 7],
                7:  [1, 2, 3, 4, 5, 6, 7],
            }
        )
