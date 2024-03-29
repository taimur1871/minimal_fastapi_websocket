"""
main app
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI

# 2. Create app and model objects
app = FastAPI()

# 1. Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=9010, reload = True)
