from pathlib import Path

from sanic import Request, Sanic
from sanic.request import File
from sanic.response import html, redirect


app = Sanic("MyApp")


@app.get("/")
async def index(_: Request):
    return html(Path("index.html").read_text())


@app.post("/")
async def upload(request: Request):
    file: File = request.files["upload"][0]
    (storage / file.name).write_bytes(file.body)
    return redirect("/")


if __name__ == "__main__":
    if not (storage := Path("storage")).exists():
        storage.mkdir()

    app.run("0.0.0.0", port=25252)