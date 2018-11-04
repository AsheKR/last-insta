# Instagram

make instagram

## Requirements

```json
{
  "SECRET_KEY": "<Django-SECRET-KEY>"
}
```

```shell
pip install -r requirements.txt
```

## Model

- User
    - img_profile
    - relation_user(User)
    - mention(Comment)

- Post
    - author(User)
    - photo
    - like_users(User)
    
- Comment
    - post(Post)
    - author(User)
    - content
    - tags(HashTag)
    
- HashTag
    - tag_name
    
## Template

- PostView / PostDetail
- PostCreate / Modify
- TagSearch
- Profile
- Login / Logout / Signup
