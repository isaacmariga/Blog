from flask import render_template,request,redirect,url_for,abort
from . import main
from .. import db, photos
from ..requests import get_quote
from ..models import Post,Comment, User, Quote
from .forms import PostForm,CommentForm,UpdateProfile
from flask_login import current_user, login_required



# Views
@main.route('/')
def index():
    title = 'Home'
    posts = Post.query.all()
    quotes=get_quote()



    return render_template('index.html', title = title, posts=posts, quotes=quotes)



@main.route("/post/new" ,  methods=['GET', 'POST'])
@login_required
def new_post():

  form=PostForm()
  post = Post.query.order_by(Post.id.desc()).first()
  

  if form.validate_on_submit():
    posts = Post(title=form.title.data, content=form.content.data, author=current_user)
    posts.save_post()
    # flash('Your post has been created!', 'success')
    return redirect(url_for('main.new_post'))
  
  return render_template('create_post.html', title= 'New Post', form=form, legend='New Post', id=post.id, post=post  )

@main.route("/post/<int:id>/update" ,  methods=['GET', 'POST'])
@login_required
def update_post(id):
  post = Post.query.get_or_404(id)
  if post.author != current_user:
    abort(403)
  form=PostForm()
  if form.validate_on_submit():
    posts = Post(title=form.title.data, content=form.content.data, author=current_user)
    posts.save_post()
    # flash('Your post has been created!', 'success')
    return redirect(url_for('main.new_post', id=post.id))
  
  return render_template('create_post.html', title= 'Update Post', form=form, legend='New Post', post_id=post.id, post=post  )

@main.route("/post/<int:id>/delete",  methods=['GET', 'POST']) 
@login_required
def delete_post(id):
  post = Post.query.get_or_404(id)
  if post.author != current_user:
    abort(403)
  db.session.delete(post)
  db.session.commit()
  # flash('Your Post has been deleted', 'success')
  return redirect(url_for('main.index'))

@main.route('/post/<int:id>/pic', methods=['GET','POST'])
def upload(id):
    post = Post.query.order_by(Post.id.desc()).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        post.post_image_path = path
        db.session.commit()

        return redirect(url_for('main.index', id=post.id))

    return render_template('upload.html', post=post)


@main.route('/post/<int:id>')
def single_post(id):
    post = Post.query.get(id)
    
    if post is None:
        abort(404)

    comments = Comment.get_comments(id)

    # vote = Vote.query.all()

    return render_template('comment.html', post=post, comments=comments, id=post.id)


@main.route('/comment/new/<int:id>', methods=['GET','POST'])
@login_required
def new_comment(id):
    post = Post.query.filter_by().first()

    if post is None:
        abort(404)

    form = CommentForm()

    if form.validate_on_submit():
        comment_content = form.comment_content.data
        new_comment = Comment( comment_content=comment_content, post=post )
        # user=current_user(add later)
        new_comment.save_comment()

        return redirect(url_for('.single_post', id=post.id ))

    title = 'New Comment'
    return render_template('new_comment.html', title=title, comment_form=form)


@main.route("/comment/<int:id>/delete",  methods=['GET', 'POST']) 
@login_required
def delete_comment(id):
    comment = Comment.query.get_or_404(id)
    db.session.delete(comment)
    db.session.commit()
  # flash('Your Post has been deleted', 'success')
    return redirect(url_for('main.index', id=comment.id))

@main.route("/post/int:<post_id>")
def post(post_id):
  post = Post.query.get_or_404(post_id)
  return render_template('post.html', title =post.title, post=post)



@main.route('/user/<uname>',methods = ['GET','POST'])
def profile(uname):
  user = User.query.filter_by(username = uname).first()
  if user is None:
    abort(404)
  form = UpdateProfile()
  if form.validate_on_submit():
    user.bio = form.bio.data
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('.profile',uname=user.username))


  return render_template("profile/profile.html", user = user, form=form)




@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
  user = User.query.filter_by(username = uname).first()
  if 'photo' in request.files:
    filename = photos.save(request.files['photo'])
    path = f'photos/{filename}'
    user.profile_pic_path = path  
    db.session.commit()
  return redirect(url_for('main.profile',uname=uname))