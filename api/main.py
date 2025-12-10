import random
from fastapi import FastAPI
#from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# from fastapi.templating import Jinja2Templates

# 1. Data Source (In-Memory List)
# This list simulates a simple, pre-defined dataset.
FOOD_CHOICES = [
    "Pizza 🍕",
    "Tacos 🌮",
    "Sushi 🍣",
    "Classic Burger 🍔",
    "Thai Curry 🌶️",    
    "Grilled Cheese & Tomato 🍅",
    "Chicken Shawarma 🐔",
    "Vegan Bowl 🥗",
    "Pho Noodle Soup 🍲"
]

# 2. App Initialization
# This creates the FastAPI application instance.

app = FastAPI()
#templates = Jinja2Templates(directory="templates") # Assuming your templates are in a 'templates' folder
templates = Jinja2Templates(directory="templates")
# app.mount("/static", StaticFiles(directory="static"), name="static")


# 3. API Endpoint Definitions (the routes)
# Default route
@app.get("/")           #endpoint, or route, always starts with a forward slash
def default_route():    #route handler function
    """
    This is the default endpoint for this back-end.
    """
    return "You have reached the default route. Back-end server is listening..."
    


@app.get("/test")           #endpoint, or route, always starts with a forward slash
def default_route():    #route handler function
    """
    {main: "This is the test endpoint for this back-end."}
    """
    return "You have reached the test route. Back-end server is listening..."
    
@app.get("/item")
def read_items():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/items/", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="index.html",
    )

# TO RUN:
# 1. Put this code in api/main.py and deploy to Vercel
# 2. Test by using your-vercel-backend-url/docs
# 3. Later call from front-end using JavaScript fetch()