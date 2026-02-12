from flask import Flask as Fk

app = Fk(__name__)

@app.route('/')
def home():
    return 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)