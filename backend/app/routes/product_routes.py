from fastapi import APIRouter, HTTPException, Path, status

from app.schemas.product import InventoryMetrics, Product, ProductCreate, ProductUpdate
from app.services import product_service

router = APIRouter()


@router.get(
    "/",
    response_model=list[Product],
    summary="Listar productos",
)
def list_products() -> list[Product]:
    return product_service.list_products()


@router.get(
    "/metrics",
    response_model=InventoryMetrics,
    summary="Obtener métricas del inventario",
)
def get_metrics() -> InventoryMetrics:
    return product_service.get_metrics()


@router.get(
    "/{product_id}",
    response_model=Product,
    summary="Obtener producto por ID",
)
def get_product(product_id: int = Path(gt=0)) -> Product:
    product = product_service.get_product(product_id)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    return product


@router.post(
    "/",
    response_model=Product,
    status_code=status.HTTP_201_CREATED,
    summary="Crear producto",
)
def create_product(payload: ProductCreate) -> Product:
    return product_service.create_product(payload)


@router.put(
    "/{product_id}",
    response_model=Product,
    summary="Actualizar producto",
)
def update_product(payload: ProductUpdate, product_id: int = Path(gt=0)) -> Product:
    product = product_service.update_product(product_id, payload)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    return product


@router.delete(
    "/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar producto",
)
def delete_product(product_id: int = Path(gt=0)) -> None:
    deleted = product_service.delete_product(product_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
