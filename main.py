from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!!'


@app.route('/new')
def newword() -> str:
    return 'new word'
'''
    f3
    add
    f3 new  add
'''

def main():
    app.run(host='0.0.0.0', port=80)


'''
   main
'''
if __name__ == '__main__':
    main()

'''
    ne feat at the and
'''