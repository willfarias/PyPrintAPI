from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import socket


app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("pyprint:app", host="PUTYOURSERVERIP", port=59900, log_level="info")

@app.get("/")
def home():
	return "PyPrintAPI: Prints through socket."

class Print(BaseModel):
	ip: str
	port: int
	body: str

@app.post("/print")
def params(params: Print):
	mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         
	host = params.ip 
	port = params.port
	retorno = 0
	try:           
		mysocket.connect((host, port)) #connecting to host
		mysocket.send(bytes(params.body,'utf-8'))#using bytes
		mysocket.close () #closing connection
		retorno = 1
	except:
		retorno = 0

	return retorno