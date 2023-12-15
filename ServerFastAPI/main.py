from fastapi import FastAPI, UploadFile, File
import pymysql
from pymysql import cursors


app = FastAPI()

mydb = pymysql.connect(
    cursorclass= cursors.DictCursor,
    host = "localhost",
    user = "root",
    password = "1488",
    database="myphoto"
)


@app.get("/image")
def get_image():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM images")
    result = cursor.fetchall()
    return {"image": result}


@app.get("/image/{id}")
def get_image(id: int):
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM images WHERE id = '{id}'")
    result = cursor.fetchone()
    return result


@app.post("/image")
def add_image(tags: str, image: UploadFile):
    print(image)
    cursor = mydb.cursor()
    sql = "INSERT INTO images (tags, image) VALUES (%s, %s)"
    val = (tags, image.file.read())
    cursor.execute(sql, val)
    mydb.commit()
    return {"message": "image added successfully"}


@app.delete("/image/{id}")
def delete_image(id: int):
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM images WHERE id = {id}")
    mydb.commit()
    return {"message": "Image deleted successfully"}


@app.post("/file/upload-file")
def upload_file(image: UploadFile):
  return image


