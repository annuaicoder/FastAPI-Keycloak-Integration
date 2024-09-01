from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from starlette.middleware.sessions import SessionMiddleware
from typing import Annotated
from fastapi.security import OAuth2AuthorizationCodeBearer

# Initialize FastAPI app
app = FastAPI()

# Define OAuth2 and Keycloak configuration
oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl="https://yourdomain.com/realms/yourRealm/protocol/openid-connect/auth",
    tokenUrl="https://yourdomain.com/realms/yourRealm/protocol/openid-connect/token",
)


@app.get("/public", response_class=HTMLResponse)
async def public_message(request: Request):
    return HTMLResponse("<h1>This is a public message.</h1>")



@app.get("/private")
async def login(request: Request):
    keycloak_login_url = "https://yourdomain.com/realms/yourRealm/protocol/openid-connect/auth?response_type=code&client_id=YourClient&redirect_uri=http://localhost:8000/auth/callback"
    return RedirectResponse(url=keycloak_login_url)


@app.get("/auth/callback")
async def auth_callback(request: Request):
    # Handle Keycloak callback and token exchange here
    return HTMLResponse("<h1>Hey Authenticated user!</h1>")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
