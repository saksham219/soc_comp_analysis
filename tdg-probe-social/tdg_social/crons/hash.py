from tdg_social.models.hash import Hash
from tdg_social.models.post import Post
from tdg_social.utils.api import get_hash
from flask_script import Command, Option

class AddHashtag(Command):
    def run(self):
        print("adding hashtags")
        for post in Post.query.all():
            hashtag_list = get_hash(post)
            for tag in hashtag_list:
                hash_info = Hash.query.filter_by(hashtag = tag).first()
                post_info = Post.query.filter_by(post_id = post.post_id).first()
                if not hash_info:
                    hash_info = Hash(tag)
                    post_info.hashtags.append(hash_info)
                    hash_info.save()
                    post_info.save()
                else:
                    a = Hash.query.filter(Hash.posts.any(id = post.id)).all()
                    if hash_info not in a:
                        post_info.hashtags.append(hash_info)
                        post_info.save()

