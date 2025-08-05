import typer
from gitclone.commands import init, add

app=typer.Typer()

@app.command(name="init")
def init_command(repo: str=None):
    init.run(repo)

@app.command(name="add")
def add_command(file_path: str):
    add.run(file_path)


if __name__=="__main__":
    app() 

# app=typer.Typer()
# @app.command()
# def hello():
#     print("Hello it works!\n")python
# if __name__=="__main__":
#     typer.run(hello)