from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import strawberry
from strawberry.fastapi import GraphQLRouter
from gql.core import Mutation, Query

def create_app():
    app = FastAPI(
        title="Backend Service",
        description="Webservice code",
        version="1.0.0",
    )

    origins = [
        "*"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app

app = create_app()

# @strawberry.type
# class Query:
#     @strawberry.field
#     def hello(self) -> str:
#         return "Hello masonite"

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
)
graphgql_app = GraphQLRouter(schema)
app.include_router(graphgql_app, prefix="/graphql")

@app.on_event("startup")
async def startup_event():
    
    pass
   

@app.on_event("shutdown")
async def shutdown_event():

    pass


@app.get("/")
def index():
    return {"message": "Service is live!"}

@app.get("/ping")
def ping():
    return {"message": "pong"}
