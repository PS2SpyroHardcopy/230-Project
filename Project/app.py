from bottle import run, get, post, template, request

all_posts = [["title1", "body1"], ["title2", "body2"], ["title3", "body3"]]

@get('/')
def render_index():
	return template('index')

#/login
@post('/login')
def login_user():
		#login user
		# get 'all_posts' variable (array)
	return template('secret_website', posts=all_posts)

#/new_post
@post('/new_post')
def new_post():
	post = [request.forms.get("title"),request.forms.get("body")]
	all_posts.append(post)
		# add new post to database or csv
		# update 'all_posts' variable
	return template('secret_website', posts=all_posts)
	
	
run(debug= True, reloader = True)

