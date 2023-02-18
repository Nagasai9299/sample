from flask import Flask

app = Flask(__name__)

@app.run('/')
def helloworld():
    print('helloworld')
    return  'Hello world'

if __name__ =='__main__':
    app.run()