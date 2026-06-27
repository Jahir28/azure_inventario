from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import init_db
from app.routes.product_routes import router as product_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Inicializa la base SQLite al arrancar el contenedor del backend.
    init_db()
    yield


app = FastAPI(
    title="Azure Inventario API",
    description="API REST para administrar productos y métricas básicas de inventario.",
    version="0.1.0",
    lifespan=lifespan,
)

# El frontend se despliega como contenedor separado y consume esta API por HTTP.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    # GitHub Actions usa este endpoint para confirmar que el despliegue responde.
    return {"status": "ok"}


app.include_router(product_router, prefix="/api/products", tags=["products"])
