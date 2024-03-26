import uvicorn
from fastapi import FastAPI
app=FastAPI()

@app.get('/')
def sample():
    return 'Hello, Cprime Team! This is sample web application deployed on Azure'


if __name__=='__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)




