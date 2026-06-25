from sqlite3 import Row

from app.database import get_connection
from app.models.product import ProductStatus
from app.schemas.product import InventoryMetrics, Product, ProductCreate, ProductUpdate


def calculate_status(quantity: int) -> ProductStatus:
    """Calculate stock status using the rules approved for the project."""
    if quantity == 0:
        return ProductStatus.OUT_OF_STOCK
    if quantity <= 5:
        return ProductStatus.LOW_STOCK
    return ProductStatus.AVAILABLE


def map_product(row: Row) -> Product:
    return Product(
        id=row["id"],
        name=row["name"],
        category=row["category"],
        price=row["price"],
        quantity=row["quantity"],
        status=calculate_status(row["quantity"]),
    )


def list_products() -> list[Product]:
    with get_connection() as connection:
        rows = connection.execute("SELECT * FROM products ORDER BY id DESC").fetchall()
    return [map_product(row) for row in rows]


def get_product(product_id: int) -> Product | None:
    with get_connection() as connection:
        row = connection.execute(
            "SELECT * FROM products WHERE id = ?",
            (product_id,),
        ).fetchone()
    return map_product(row) if row else None


def create_product(payload: ProductCreate) -> Product:
    with get_connection() as connection:
        cursor = connection.execute(
            """
            INSERT INTO products (name, category, price, quantity)
            VALUES (?, ?, ?, ?)
            """,
            (payload.name, payload.category, payload.price, payload.quantity),
        )
        product_id = int(cursor.lastrowid)

    product = get_product(product_id)
    if product is None:
        raise RuntimeError("Product was not created.")
    return product


def update_product(product_id: int, payload: ProductUpdate) -> Product | None:
    current = get_product(product_id)
    if current is None:
        return None

    data = payload.model_dump(exclude_unset=True, exclude_none=True)
    updated = current.model_dump()
    updated.update(data)

    with get_connection() as connection:
        connection.execute(
            """
            UPDATE products
            SET name = ?, category = ?, price = ?, quantity = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
            """,
            (
                updated["name"],
                updated["category"],
                updated["price"],
                updated["quantity"],
                product_id,
            ),
        )

    return get_product(product_id)


def delete_product(product_id: int) -> bool:
    with get_connection() as connection:
        cursor = connection.execute("DELETE FROM products WHERE id = ?", (product_id,))
        deleted_rows = cursor.rowcount
    return deleted_rows > 0


def get_metrics() -> InventoryMetrics:
    products = list_products()
    return InventoryMetrics(
        total_products=len(products),
        available_products=sum(1 for product in products if product.status == ProductStatus.AVAILABLE),
        low_stock_products=sum(1 for product in products if product.status == ProductStatus.LOW_STOCK),
        out_of_stock_products=sum(1 for product in products if product.status == ProductStatus.OUT_OF_STOCK),
        inventory_value=sum(product.price * product.quantity for product in products),
    )
