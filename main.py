from mongoengine import (
    connect,
    Document,
    StringField,
    ReferenceField,
    ListField,
    DynamicDocument,
    EmbeddedDocumentField,
    EmbeddedDocument,
    CASCADE,
)
from time import perf_counter

connect("my_db", host="127.0.0.1", port=27017)


class User(DynamicDocument):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)


class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))

    meta = {"allow_inheritance": True}


class TextPost(Post):
    content = StringField()


class ImagePost(Post):
    image_path = StringField()


class LinkPost(Post):
    link_url = StringField()


ross = User(email="ross@example.com", first_name="Ross", last_name="A").save()
john = User(email="john@example.com", first_name="Roe", last_name="Kail", hello="===WORLD==="*2).save()

print("=== USER ===")
for user in User.objects():
    print(user.to_json())

msg1 = Comment(name="jamie", content="How's going?")
msg2 = Comment(name="howard", content="What are you doing?")
# msg.save()
post1 = TextPost(title="Fun with MongoEngine", author="john", comments=[msg1, msg2])
post1.content = "Took a look at MongoEngine today, looks pretty cool."
post1.tags = ["mongodb", "mongoengine"]
post1.test = "cool============================================================================"
post1.save()

post2 = LinkPost(title="MongoEngine Documentation", author=ross)
post2.link_url = "http://docs.mongoengine.com/"
post2.tags = ["mongoengine"]
post2.save()

print("\n=== POST ===")
for post in Post.objects:
    print(post.to_json())
    print(post.comments)
    print(post.title)

for post in TextPost.objects:
    print(post.to_json())