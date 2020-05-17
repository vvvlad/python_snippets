# pip install emoji

import emoji
result = emoji.emojize('Python is :thumbs_up:')
print(result)
# 'Python is 👍'

# You can also reverse this:
result = emoji.demojize('Python is 👍')
print(result)
# 'Python is :thumbs_up:'
