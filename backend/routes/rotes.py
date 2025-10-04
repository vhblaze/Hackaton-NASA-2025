from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel
from neo4j import GraphDatabase
from typing import Any

router = APIRouter()

NEO4J_URI = "neo4j+s://18fad2f3.databases.neo4j.io"
NEO4J_USER = "sacy espaco"
NEO4J_PASSWORD = "DIlmDXkSUshKRAnzvU4DtXzUXuQVLGoLS-Xl5Fxbet0"

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

class Item(BaseModel):
    id: int
    name: str
    description: str = None

class MLInput(BaseModel):
    feature1: float
    feature2: float
    feature3: float


@router.get("/items")
def get_items():
    with driver.session() as session:
        result = session.run("MATCH (i:Item) RETURN i")
        items = []
        for record in result:
            node = record["i"]
            items.append({
                "id": node.get("id"),
                "name": node.get("name"),
                "description": node.get("description")
            })
        return items

@router.get("/items/{item_id}")
def get_item(item_id: int):
    with driver.session() as session:
        result = session.run("MATCH (i:Item {id: $id}) RETURN i", id=item_id)
        record = result.single()
        if record:
            node = record["i"]
            return {
                "id": node.get("id"),
                "name": node.get("name"),
                "description": node.get("description")
            }
        raise HTTPException(status_code=404, detail="Item not found")

@router.post("/items")
def create_item(item: Item):
    with driver.session() as session:
        session.run(
            "CREATE (i:Item {id: $id, name: $name, description: $description})",
            id=item.id, name=item.name, description=item.description
        )
    return item

@router.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    with driver.session() as session:
        result = session.run(
            "MATCH (i:Item {id: $id}) "
            "SET i.name = $name, i.description = $description "
            "RETURN i",
            id=item_id, name=updated_item.name, description=updated_item.description
        )
        record = result.single()
        if record:
            node = record["i"]
            return {
                "id": node.get("id"),
                "name": node.get("name"),
                "description": node.get("description")
            }
        raise HTTPException(status_code=404, detail="Item not found")

@router.delete("/items/{item_id}")
def delete_item(item_id: int):
    with driver.session() as session:
        result = session.run(
            "MATCH (i:Item {id: $id}) DETACH DELETE i RETURN COUNT(i) AS deleted",
            id=item_id
        )
        deleted = result.single()["deleted"]
        if deleted:
            return {"detail": "Item deleted"}
        raise HTTPException(status_code=404, detail="Item not found")


@router.post("/ml/predict")
def predict(input_data: MLInput):
    # Exemplo fictício:
    prediction = input_data.feature1 + input_data.feature2 + input_data.feature3
    return {"prediction": prediction}

# Rota para status do modelo
@router.get("/ml/status")
def model_status():
    # Exemplo de resposta
    return {"status": "Modelo carregado e pronto para predição"}

# Rota para upload de arquivo para treinamento
@router.post("/ml/train")
def train_model(file: UploadFile = File(...)):
    # Aqui você pode processar o arquivo e treinar seu modelo
    # Exemplo fictício:
    contents = file.file.read()
    # ...processamento...
    return {"detail": "Treinamento iniciado"}