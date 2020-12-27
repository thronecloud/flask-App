#!/usr/bin/python3
from flask import Flask, render_template,request
import re
import csv
import requests
import pandas as pd

inchDF=pd.read_csv('1inch.csv')
airdropDF=pd.read_csv("Tornado.csv", names=["address", "tokens"])
uniswapDF=pd.read_csv("uniswap-distribution.csv")
inch_list=list(inchDF['address'])
airdrop_list=list(airdropDF['address'])
uniswap_list=list(uniswapDF['address'])

app = Flask(__name__)

@app.route('/')
def index():
    title="Ether Tools"
    return render_template("index.html",title=title)

@app.route('/airdrop')
def airdrop():
    title = "Batch Airdrop Check for Uniswap, Tornado & 1Inchs"
    return render_template("airdrop.html",title=title)
    
@app.route('/result', methods=["POST"])
def result():
    Result=[]
    erc20s=request.form.get("erc20s").splitlines()
    for addr in erc20s:
        if addr in inch_list:
            ind=inch_list.index(addr)
            Result.append("1Inch "+ str(addr) + " " + str (inchDF['tokens'][ind]))
        if addr in airdrop_list:
            ind=airdrop_list.index(addr)
            Result.append("Tornado "+str(addr)+ " " + str(airdropDF['tokens'][ind]))
        if addr in uniswap_list:
            ind=uniswap_list.index(addr)
            Result.append("Uniswap "+str(addr)+ " " + str(uniswapDF['uni'][ind]))
    
    print(Result)
    return render_template("result.html",title=erc20s,result=Result)