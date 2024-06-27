from flask import Flask, request, jsonify, json
from model.post import Post
from db import posts
import uuid


app = Flask(__name__)


# Helper function to find a post by id
def find_post(post_id):
    return next((post.to_dict() for post in posts if post.to_dict()['id'] == post_id), None)


@app.route("/")
def index():
    return "<p>Hello, World!</p>"


@app.route("/posts", methods=['POST'])
def create_post():
    post_data = request.get_json()
    #
    post = Post(uuid.uuid4().hex, post_data['title'],
                post_data['author'], post_data['content'])
    posts.append(post)
    return jsonify({'status': 'success'}), 201


@app.route("/posts", methods=['GET'])
def get_posts():
    return jsonify([post.to_dict() for post in posts])


@app.route("/posts/<id>", methods=['GET'])
def get_post(id):
    post = find_post(id)
    if post is None:
        return jsonify({'error': 'Post not found'}), 404

    return jsonify(post)


@app.route("/posts/<id>", methods=['PUT'])
def update_post(id):

    post_data = request.get_json()

    post = find_post(id)

    if post is None:
        return jsonify({'error': 'Post not found'}), 404

    author = post_data.get('author')
    title = post_data.get('title')
    content = post_data.get('content')

    # Проверка наличия необходимых полей
    if not all([author, title, content]):
        return jsonify({'error': 'Missing required fields'}), 400

    # Обновление поста
    post['author'] = author
    post['title'] = title
    post['content'] = content

    # Update the post
    # post.update(title=title, author=author, content=content)
    return jsonify(post), 200


if __name__ == '__main__':
    app.run(debug=True)
