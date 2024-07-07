from ninja import NinjaAPI, Schema

api = NinjaAPI()


class UserSchema(Schema):
    username: str
    is_authenticated: bool
    # if not authenticated, email will be None
    email: str = None


@api.get("/hello")
def hello(request):
    print(request)
    return "hello world"


@api.get("/me", response=UserSchema)
def me(request):
    print(request)
    return request.user
