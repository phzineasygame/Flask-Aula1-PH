from flask import Flask, redirect

@app.get("/home") 

def home(): 

  return redirect("/")