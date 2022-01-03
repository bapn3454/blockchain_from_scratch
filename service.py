from flask import app
from chain import Chain

demo = Chain(5)


@app.route("/mine")
def mine():
    demo.mine()
    print(demo.getLastBloc())
    return f"""<h1>One block mined! </h1><br />
        {demo.getLastBloc()}"""

@app.route("/chain")
def chain():
    return (str(demo))

#This is just for test purposes
#In prod this method had to be called automatically
@app.route("/consensus")
def consensus():
    demo.consensus()
    return("Consensus made with other nodes")

if __name__ == "__main__":
    demo.addNode('http://www.bapn.fr:5000')
    print(demo.getLastBloc())
    app.run()