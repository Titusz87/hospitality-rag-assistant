from fastapi import FastAPI

#create an app instance
app=FastAPI()

#links the get operation to the root
@app.get("/")
# decalre the read_root func that returns the Json after each get query
def read_root():
    return {"messages": "Hello World"}

###################
# FIX: load menu right beginning when the app starts
###################
from pydpf import PdfReader

# create a reader object
reader = PdfReader(data/menus.pdf)

# getting pages from the file
page = reader.pages[0]

#extract text from page
text=page.extract_text()
print(text)