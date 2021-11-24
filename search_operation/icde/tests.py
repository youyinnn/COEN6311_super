from django.test import TestCase
from . import models as ICDE
from .models import IcdeRecord
from common.project_const import const

class IcdeTestcase(TestCase):

    def test_paper_search_record(self):
        ICDE.paper_search_record(123, "adder")
        query = IcdeRecord.objects.all()
        record = query[0]
        self.assertEqual(record.user_id, 123)
        self.assertEqual(record.operation_type, const.PAPER_SEARCH)
        self.assertEqual(record.input_text, "adder")

    def test_paper_detail_record(self):
        ICDE.paper_detail_click_record(123, "456", "paper")
        query = IcdeRecord.objects.all()
        record = query[0]
        self.assertEqual(record.user_id, 123)
        self.assertEqual(record.operation_type, const.PAPER_DETAIL_CLICK)
        self.assertEqual(record.paper_id, "456")    
        self.assertEqual(record.paper_title, "paper")    
        
    def test_paper_origin_record(self):
        ICDE.paper_origin_click_record(123, "456", "paper")
        query = IcdeRecord.objects.all()
        record = query[0]
        self.assertEqual(record.user_id, 123)
        self.assertEqual(record.operation_type, const.PAPER_ORIGIN_CLICK)
        self.assertEqual(record.paper_id, "456")
        self.assertEqual(record.paper_title, "paper")    

    def test_paper_like_record(self):
        ICDE.paper_like_click_record(123, "456", "paper")
        query = IcdeRecord.objects.all()
        record = query[0]
        self.assertEqual(record.user_id, 123)
        self.assertEqual(record.operation_type, const.PAPER_LIKE_CLICK)
        self.assertEqual(record.paper_id, "456")

    def test_paper_dilike_record(self):
        ICDE.paper_dislike_click_record(123, "456", "paper")
        query = IcdeRecord.objects.all()
        record = query[0]
        self.assertEqual(record.user_id, 123)
        self.assertEqual(record.operation_type, const.PAPER_DISLIKE_CLICK)
        self.assertEqual(record.paper_id, "456")
        self.assertEqual(record.paper_title, "paper")    

    def test_paper_share_record(self):
        ICDE.paper_share_click_record(123, "456", 789, "team", "paper")
        query = IcdeRecord.objects.all()
        record = query[0]
        # print(record.__dict__)
        self.assertEqual(record.user_id, 123)
        self.assertEqual(record.operation_type, const.PAPER_SHARE)
        self.assertEqual(record.paper_id, "456")
        self.assertEqual(record.team_id, 789)
        self.assertEqual(record.team_name, "team")
        self.assertEqual(record.paper_title, "paper")    