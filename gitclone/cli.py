import typer
from gitclone.commands import init, add, commit

app=typer.Typer()

@app.command(name="init")
def init_command(repo: str=None):
    init.run(repo)

@app.command(name="add")
def add_command(file_path: str):
    add.run(file_path)

@app.command(name="commit")
def commit_command(mes: str):
    commit.run(mes)

# app=typer.Typer()
# @app.command()
# def hello():
#     print("Hello it works!\n")python
# if __name__=="__main__":
#     typer.run(hello)