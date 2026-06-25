from dataclasses import dataclass
from enum import StrEnum


class ProductStatus(StrEnum):
    OUT_OF_STOCK = "Agotado"
    LOW_STOCK = "Bajo stock"
    AVAILABLE = "Disponible"


@dataclass
class ProductModel:
    id: int
    name: str
    category: str
    price: float
    quantity: int
    status: ProductStatus
