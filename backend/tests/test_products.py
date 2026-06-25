import unittest

from app.models.product import ProductStatus
from app.services.product_service import calculate_status


class ProductServiceTest(unittest.TestCase):
    def test_calculate_status(self) -> None:
        self.assertEqual(calculate_status(0), ProductStatus.OUT_OF_STOCK)
        self.assertEqual(calculate_status(3), ProductStatus.LOW_STOCK)
        self.assertEqual(calculate_status(8), ProductStatus.AVAILABLE)
