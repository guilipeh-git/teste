from os import system as s

comandos = "git add .",'git commit -m "commit"', "git push heroku master"

if __name__ == "__main__":
    for c in comandos:
        s(c)