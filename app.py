from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)

# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clyst.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# with app.app_context():
#     db.create_all()


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # If id is not 1 then return abort with 403 error
        if current_user.id != 1:
            return abort(403)
        # Otherwise continue with the route function
        return f(*args, **kwargs)

    return decorated_function


class User(db.Model):
    __table_name__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    location = db.Column(db.String(150))
    created_at = db.Column(db.String(250))
    posts = relationship("Posts", back_populates="artist")
    products = relationship("Product", back_populates="artist")


class Posts(db.Model):
    __table_name__ = 'posts'

    post_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    artist = relationship("User", back_populates="posts")
    post_title = db.Column(db.String(255))
    description = db.Column(db.Text)
    media_url = db.Column(db.String(255))
    created_at = db.Column(db.String(255))


class Product(db.Model):
    __table_name__ = 'products'

    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    artist = relationship("User", back_populates="products")
    title = db.Column(db.String(150))
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2))
    # category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id', ondelete='SET NULL'))
    created_at = db.Column(db.String(250))

#
# with app.app_context():
#     db.create_all()


@app.route('/', methods=["GET", "POST"])
def home():
    result = db.session.execute(db.select(Posts))
    posts = result.scalars().all()
    return render_template("index.html", posts=posts, current_user=current_user)


@app.route("/products", methods=["GET", "POST"])
@admin_only
def products():
    result = db.session.execute(db.select(Product))
    products = result.scalars().all()
    return render_template("products.html", products=products, current_user=current_user)


@app.route("/add", methods=["GET", "POST"])
@admin_only
def add_posts():
    if request.method == 'POST':
        new_post = Posts(
            post_title=request.form['post_title'],
            description=request.form['description'],
            created_at=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add_posts.html", posts=Posts, current_user=current_user)


@app.route("/add_products", methods=["GET", "POST"])
@admin_only
def add_products():
    if request.method == 'POST':
        new_product = Product(
            product_name=request.form['product_name'],
            price=request.form['price'],
            img_url=request.form['product_image']
        )
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add_products.html", products=Product)


@app.route("/delete")
@admin_only
def delete_posts():
    post_id = request.args.get('post_id')
    post_to_delete = db.get_or_404(Posts, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    render_template(url_for('home'))


@app.route("/delete_products")
@admin_only
def delete_products():
    product_id = request.args.get('product_id')
    product_to_delete = db.get_or_404(Product, product_id)
    db.session.delete(product_to_delete)
    db.session.commit()
    render_template(url_for('home'))


@app.route("/profile")
@admin_only
def profile():
    return render_template("index.html", current_user=current_user)


if __name__ == "__main__":
    app.run(debug=True)
