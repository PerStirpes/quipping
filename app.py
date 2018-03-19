import requests
from flask import Flask, render_template, session, redirect, request, url_for, g


app = Flask(__name__)
app.secret_key = ''
