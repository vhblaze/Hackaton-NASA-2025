from neo4j import GraphDatabase, basic_auth

import requirements
from flask import Flask, request, jsonify
from fastapi import FastAPI

import os
import json
from routes.rotes import router  

app = FastAPI()

app.include_router(router)