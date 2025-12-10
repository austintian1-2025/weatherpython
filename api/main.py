import random
from fastapi import FastAPI

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

# 3. API Endpoint Definitions (the routes)

# Default route
@app.get("/data")           #endpoint, or route, always starts with a forward slash
def default_route():    #route handler function
    """
    This is the default endpoint for this back-end.
    """
    data = {"name": "Alice", "age": 30, "city": "New York", "data": "This is a test"}
    headers = {"X-Custom-Header": "MyValue"}
    return JSONResponse(content=data, headers=headers)

    

@app.get("/test")           #endpoint, or route, always starts with a forward slash
def default_route():    #route handler function
    """
    {main: "This is the test endpoint for this back-end."}
    """
    return "You have reached the default route. Back-end server is listening..."
    
@app.get("/items/")
async def read_items():
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



# When a user sends a GET request to '/random-choice', this function runs.
"""
@app.get("/random-choice")
def get_random_food_choice():
    """
    Returns a single random food choice from the FOOD_CHOICES list.
    """
    # Use the built-in Python 'random' module to pick one item.
    selected_choice = random.choice(FOOD_CHOICES)
    
    # Return a Python dictionary, which FastAPI converts to a JSON response.
    return {"status": "success", "choice": selected_choice}

@app.get("/my-choice/")
def get_my_food_choice(choice):    
    # convert to integer
    choiceNumber = int(choice)

    # check if choice is a valid index i.e. between 0 and length of list
    if choiceNumber >= 0 and choiceNumber < len(FOOD_CHOICES):
      # Use the passed in choice number; passed in as query parameter
      selected_choice = FOOD_CHOICES[choiceNumber]
    
      # Return a Python dictionary, which FastAPI converts to a JSON response.     
      return {"status": "success", "choice": selected_choice}
    else:
      return {"status": "error", "message": f"invalid choice:{choice}"}  
"""

# TO RUN:
# 1. Put this code in api/main.py and deploy to Vercel
# 2. Test by using your-vercel-backend-url/docs
# 3. Later call from front-end using JavaScript fetch()