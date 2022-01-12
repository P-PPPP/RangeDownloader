from urllib.parse import  unquote
import Parser as Ps

##### Fast Api Config #####
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
Api = FastAPI()
origins = ["https://livedb.asoulfan.com","http://localhost"]
Api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
############ End #############

Extracts = [
    "bilibili.com","asoul-rec.com","youtube.com","youtu.be"
]

class Parse_Template():
    Url:str
    Args:str=""
    Download_Url:str
    Play_Html:str
    Web_Title:str
    Save_Name:str
    Video_Format:str="mp4"
    Download_Tool:str="ffmpeg"

A = Parse_Template()

@Api.get("/Parse/{url:path}")
def Parse(url:str)->Parse_Template:
    global A
    A.Url = url

    Special = False
    for item in Extracts:
        if item in url:
            Special = True
            A = Ps.Parse(url)
    if Special==False:
        A.Download_Url= url
        A.Play_Html = f"<video src='{url}' controls></video>"
        A.Web_Title = url.split("/")[-1].replace("?","").replace(" ","")
        A.Save_Name = url.split("/")[-1].replace("?","").replace(" ","")

    A.Download_Url = unquote(A.Download_Url)
    A.Play_Html = unquote(A.Play_Html)
    A.Save_Name = unquote(A.Save_Name)
    return A
