from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloworld():
    print('helloworld')
    return  'Hello world'

@app.route('/api')
def api():
    print('inside api')
    return  'Inside api'

if __name__ =='__main__':
    app.run()