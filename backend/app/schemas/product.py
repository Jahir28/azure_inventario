from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from app.models.product import ProductStatus


class ProductBase(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100,
        examples=["Laptop Lenovo ThinkPad"],
    )
    category: str = Field(
        min_length=2,
        max_length=60,
        examples=["Computadoras"],
    )
    price: float = Field(ge=0, examples=[850.0])
    quantity: int = Field(ge=0, examples=[12])

    @field_validator("name", "category")
    @classmethod
    def normalize_text(cls, value: str) -> str:
        cleaned_value = value.strip()
        if not cleaned_value:
            raise ValueError("The value cannot be empty.")
        return cleaned_value


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    category: str | None = Field(default=None, min_length=2, max_length=60)
    price: float | None = Field(default=None, ge=0)
    quantity: int | None = Field(default=None, ge=0)

    @field_validator("name", "category")
    @classmethod
    def normalize_optional_text(cls, value: str | None) -> str | None:
        if value is None:
            return value

        cleaned_value = value.strip()
        if not cleaned_value:
            raise ValueError("The value cannot be empty.")
        return cleaned_value

    @model_validator(mode="after")
    def validate_at_least_one_field(self) -> "ProductUpdate":
        if not self.model_dump(exclude_none=True):
            raise ValueError("At least one field must be provided.")
        return self


class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    status: ProductStatus


class InventoryMetrics(BaseModel):
    total_products: int
    available_products: int
    low_stock_products: int
    out_of_stock_products: int
    inventory_value: float
