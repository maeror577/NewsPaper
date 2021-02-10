from django.contrib.auth.models import User
from accounts.models import Author
from news.models import Category, Post, Comment

# Create users and register authors
user1 = User.objects.create_user('Hwogurpeih')
user2 = User.objects.create_user('Srugaelae')
user3 = User.objects.create_user('Qhueloqpia')
user4 = User.objects.create_user('Mupomid')
author1 = Author.objects.create(user=user1)
author2 = Author.objects.create(user=user2)

# Add 4 news categories
category1 = Category.objects.create(name='ecstatic')
category2 = Category.objects.create(name='estimable')
category3 = Category.objects.create(name='offending')
category4 = Category.objects.create(name='exposed')

# Add 2 articles and 1 news item
post1 = Post.objects.create(
    author=author1,
    post_type='A',
    title='Shy merits say advice',
    content=('One advanced diverted domestic sex repeated bringing you old. '
        'Possible procured her trifling laughter thoughts property she met '
        'way. Companions shy had solicitude favourable own. Which could saw '
        'guest man now heard but. Lasted my coming uneasy marked so should. '
        'Gravity letters it amongst herself dearest an windows by. Wooded '
        'ladies she basket season age her uneasy saw. Discourse unwilling am '
        'no described dejection incommode no listening of. Before nature his '
        'parish boy.')
)
post2 = Post.objects.create(
    author=author2,
    post_type='A',
    title='Behaviour can attempted estimable',
    content=('Folly words widow one downs few age every seven. If miss part by '
        'fact he park just shew. Discovered had get considered projection who '
        'favourable. Necessary up knowledge it tolerably. Unwilling departure '
        'education is be dashwoods or an. Use off agreeable law unwilling sir '
        'deficient curiosity instantly. Easy mind life fact with see has bore '
        'ten. Parish any chatty can elinor direct for former. Up as meant '
        'widow equal an share least.')
)
post3 = Post.objects.create(
    author=author1,
    post_type='N',
    title='Trees delay fancy noise',
    content=('Another journey chamber way yet females man. Way extensive and '
        'dejection get delivered deficient sincerity gentleman age. Too end '
        'instrument possession contrasted motionless. Calling offence six joy '
        'feeling. Coming merits and was talent enough far. Sir joy northward '
        'sportsmen education. Discovery incommode earnestly no he commanded '
        'if. Put still any about manor heard.')
)

# Add categories to posts
post1.category.set((category1, category2))
post2.category.set((category3,))
post3.category.set((category4,))

# Add comments
comment1 = Comment.objects.create(
    post=post1,
    user=user1,
    text='Improve ashamed married expense bed her comfort pursuit mrs'
)
comment2 = Comment.objects.create(
    post=post2,
    user=user2,
    text='Four time took ye your as fail lady'
)
comment3 = Comment.objects.create(
    post=post2,
    user=user3,
    text='Up greatest am exertion or marianne'
)
comment4 = Comment.objects.create(
    post=post3,
    user=user4,
    text='Now who promise was justice new winding'
)
comment5 = Comment.objects.create(
    post=post3,
    user=user1,
    text='In finished on he speaking suitable advanced if'
)

# Like/dislike posts and comments:
# post1 -- 3 likes
# post2 -- 5 likes
# post3 -- -2 likes
# comment1 -- 1 like
# comment2 -- 2 likes
# comment3 -- 0 likes
# comment4 -- -3 likes
# comment5 -- 0 likes
post1.like()
post1.like()
post1.like()
post1.dislike()
post1.like()
post2.like()
post2.like()
post2.like()
post2.like()
post2.like()
post3.like()
post3.dislike()
post3.dislike()
post3.dislike()
comment1.like()
comment2.like()
comment2.like()
comment3.dislike()
comment3.like()
comment4.dislike()
comment4.dislike()
comment4.dislike()

# Update authors' rating
author1.update_rating()
author2.update_rating()

# Finding out the best author and post with comments
best_author = Author.objects.order_by('-rating')[0]
best_post = Post.objects.order_by('-rating')[0]
comments = Comment.objects.filter(post=best_post)

with open('stats.txt', 'w') as outfile:
    outfile.write('THE BEST AUTHOR\n'
                  '---------------\n'
                 f'Username: {best_author.user.username}\n'
                 f'Rating: {best_author.rating}\n\n')
    outfile.write('THE BEST POST\n'
                  '-------------\n'
                 f'Date added: {best_post.posted}\n'
                 f'Posted by: {best_post.author.user.username}\n'
                 f'Rating: {best_post.rating}\n'
                 f'Title: {best_post.title}\n'
                 f'Preview: {best_post.preview()}\n\n')
    outfile.write('COMMENTS\n'
                  '--------\n')
    for comment in comments:
        outfile.write(f'Date added: {comment.posted}\n'
                      f'Posted by: {comment.user.username}\n'
                      f'Rating: {comment.rating}\n'
                      f'Text: {comment.text}\n'
                       '--------\n')

