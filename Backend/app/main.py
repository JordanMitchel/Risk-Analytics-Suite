from fastapi import FastAPI

from Backend.app.api.routes.portfolios import router as portfolios_router


app = FastAPI(
    title="Risk Analytics Suite",
    version="0.1.0",
)

app.include_router(
    portfolios_router,
    prefix="/api/v1",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}