from flask import Flask, url_for, request, redirect, abort, jsonify
from BookDao import bookDao

app = Flask(__name__, static_url_path='', static_folder='staticpages')


@app.route('/')
def index():
    return "hello"
#get all


@app.route('/books')
def getAll():
    return jsonify(bookDao.getAll())


# find By id

@app.route('/books/<int:id>')
def findById(id):
    return jsonify(bookDao.findById(id))

# create
# curl -X POST -d "{\"title\":\"test\", \"author\":\"some guy\", \"price\":123}" http://127.0.0.1:5000/books


@app.route('/books', methods=['POST'])
def create():
    global nextId
    if not request.json:
        abort(400)

    book = {
        "id": nextId,
        "title": request.json["title"],
        "author": request.json["author"],
        "price": request.json["price"]
    }
    nextId += 1
    return jsonify(bookDao.create(book))

    return "served by Create "

#update
# curl -X PUT -d "{\"Title\":\"new Title\", \"Price\":999}" -H "content-type:application/json" http://127.0.0.1:5000/books/1


@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    foundBook=bookDao.findById(id)
    print (foundBook)
    if foundBook == {}:
        return jsonify({}), 404
    currentBook = foundBook
    if 'title' in request.json:
        currentBook['title'] = request.json['title']
    if 'author' in request.json:
        currentBook['author'] = request.json['author']
    if 'price' in request.json:
        currentBook['price'] = request.json['price']
    bookDao.update(currentBook)

    return jsonify(currentBook)

#delete
# curl -X DELETE http://127.0.0.1:5000/books/1


@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    bookDao.delete(id)

    return jsonify({"done": True})


if __name__ == "__main__":
    app.run(debug=True)