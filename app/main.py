from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware  # <-- Add this
from app.routers import auth_routes, oauth_routes
from app.database import engine, Base
from app.config import SECRET_KEY  # <-- Use the secret from your .env

app = FastAPI(title="Gameapp")

# Add session middleware for OAuth
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

# Create tables (run once, or use migrations in prod)
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth_routes.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(oauth_routes.router, prefix="/api/oauth", tags=["OAuth Login"])

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to YourAppName API"}
