"""Tests for next Irish lottery draw date."""
from datetime import datetime
from unittest import TestCase

from freezegun import freeze_time

from date_calculate import get_next_lottery_date


class TestDateCalculation(TestCase):
    """Tests for next Irish lottery draw date."""

    def test_next_date_within_current_week(self):
        """Test next date within the current week."""
        date = datetime(2018, 4, 12, 1, 10, 10)

        result_date = get_next_lottery_date(date)

        self.assertEqual(result_date, datetime(2018, 4, 14, 20))
        self.assertEqual(result_date.strftime('%a %I%p'), 'Sat 08PM')

    def test_next_date_at_next_week(self):
        """Test next date at the next week."""
        date = datetime(2018, 4, 14, 9)

        result_date = get_next_lottery_date(date)

        self.assertEqual(result_date, datetime(2018, 4, 18, 20))
        self.assertEqual(result_date.strftime('%a %I%p'), 'Wed 08PM')

    def test_next_date_at_next_month(self):
        """Test next date at the next month."""
        date = datetime(2018, 4, 28)

        result_date = get_next_lottery_date(date)

        self.assertEqual(result_date, datetime(2018, 5, 2, 20))
        self.assertEqual(result_date.strftime('%a %I%p'), 'Wed 08PM')

    def test_next_date_at_current_match_date(self):
        """Test passed date as current lottery draw date."""
        date = datetime(2018, 4, 11, 20)

        result_date = get_next_lottery_date(date)

        self.assertEqual(result_date, datetime(2018, 4, 14, 20))
        self.assertEqual(result_date.strftime('%a %I%p'), 'Sat 08PM')

        date = datetime(2018, 4, 14, 20)

        result_date = get_next_lottery_date(date)

        self.assertEqual(result_date, datetime(2018, 4, 18, 20))

    @freeze_time('2018-04-11')
    def test_current_date_as_default(self):
        """Test default value for a date evaluates to the current date."""
        result_date = get_next_lottery_date()

        self.assertEqual(result_date, datetime(2018, 4, 14, 20))
        self.assertEqual(result_date.strftime('%a %I%p'), 'Sat 08PM')
