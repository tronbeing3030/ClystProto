from flask import Flask, render_template
from sqlalchemy.orm import DeclarativeBase
from flask_sqlalchemy import SQLAlchemy

# from models.dbs import (User, Artists, Posts)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy()

app = Flask(__name__, static_folder='static')

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///clyst.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/', methods=["GET", "POST"])
def home():
    # posts = db.session.query(
    #     Posts.post_id,
    #     Posts.post_title,
    #     Posts.description,
    #     Posts.created_at,
    #     Posts.media_url,
    #     Artists.role.label("tag"),
    #     User.name.label("artist_name")
    # ).join(
    #     Artists, Posts.artist_id == Artists.artist_id
    # ).join(
    #     User, User.user_id == Artists.user_id
    # ).all()
    #
    # all_postings = [
    #     {
    #         'id': post.post_id,
    #         'title': post.post_title,
    #         'description': post.description,
    #         'image': post.media_url,
    #         'date': post.created_at.strftime('%Y-%m-%d'),
    #         'tag': post.tag.value if post.tag else '',
    #         'artist_name': post.artist_name
    #     } for post in posts
    # ]

    all_postings = [{
            'id': "post_id",
            'title': "post_title",
            'description': "description",
            'image': "boyimage",
            'date': "12-12-2025",
            'tag': "value",
            'artist_name': "artist_name"
        },{
            'id': "post_id2",
            'title': "post_title2",
            'description': "description2",
            'image': "boyimage2",
            'date': "10-12-2025",
            'tag': "value2",
            'artist_name': "artist_name2"
        }]

    return render_template("index.html", posts=all_postings)


@app.route("/add", methods=["GET", "POST"])
def add():
    pass
    # if request.method == "POST":
    #     new_book = Post(
    #         product_name=request.form["product_name"],
    #         artist_name=request.form["artist_name"],
    #         price=request.form["price"]
    #     )
    #     db.session.add(new_book)
    #     db.session.commit()
    #     return redirect(url_for('home'))
    # return render_template("add.html")


@app.route("/delete")
def delete():
    pass
    # post_id = request.args.get('id')
    # post_to_delete = db.get_or_404(Post, post_id)
    # db.session.delete(post_to_delete)
    # db.session.commit()
    # return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
