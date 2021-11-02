import re


def printWelcome():
    print("""
    ****************************************
    ******** Welcome to MadLib Game ********
    ----------------------------------------
    - in This game you will be asked to    -
    - enter meaningful words and at the end-
    - the Matlib game will show you funny  -
    - paragraph of your chosen words       -
    ----------------------------------------
    ****************************************
    ****************************************
    """)


def read_template(path):
    """
    function read a file
    and return the content of the file
    """
    with open(path , "r" ) as f:
        content = f.read()
        return content

def parse_template(content):
    """
    A function takes in a string as input
    and return an array
    """
    
    partCont=re.findall(r'{(.*?)}',content)
    x= tuple(partCont)
    testing=re.sub(r'{(.*?)}',"{}",content)

    return testing,x
   
def merge(file,x):
    return file.format(*x)
    

def write_template(content):
  with open("assets/make_me_a_video_game.txt",'w') as writer:
    writer.write(content)

if __name__ == "__main__":
    printWelcome()
    content=read_template("assets/make_me_a_video_game_template.txt")
    partCont=re.findall(r'{(.*?)}',content)
    arrayAnswer=[]
    for i in partCont:
     userAnswer=input(f'Please enter a {i} ')
     arrayAnswer.append(userAnswer)

    arrayWanted=tuple(arrayAnswer)
    lastText=re.sub(r'{(.*?)}',"{}",content)
    print(merge(lastText,arrayWanted))
    write_template(merge(lastText,arrayWanted))



















