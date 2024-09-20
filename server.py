import uvicorn
from mainapp.user import *
from mainapp.book import *
from mainapp.admin import *

if __name__ == '__main__':
    uvicorn.run(app)