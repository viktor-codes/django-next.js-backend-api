from ninja import Schema
from ninja_extra import NinjaExtraAPI
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.controller import NinjaJWTDefaultController


api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)
api.add_router("/waitlists/", "waitlists.api.router")


class UserSchema(Schema):
    username: str
    is_authenticated: bool
    # if not authenticated, email will be None
    email: str = None


@api.get("/hello")
def hello(request):
    print(request)
    return {"message": "Hello World"}


@api.get("/me", response=UserSchema, auth=JWTAuth())
def me(request):
    print(request)
    return request.user
