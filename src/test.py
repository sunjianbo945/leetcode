google_news_url = "https://news.google.com/news/rss"
import requests
#
#
# def get_headlines(rss_url):
#     """
#     @returns a list of titles from the rss feed located at `rss_url`
#     """
#     response = requests.get(rss_url)
#
#     if response.status_code != 200:
#         raise Exception(f'request has eroor {rss_url} can not get response with error code {response.status_code}')
#
#     content = response.text
#     res = []
#     for index, value in enumerate(content):
#
#         if value == '<' and index + 7 <= len(content) and content[index:index + 7] == '<title>':
#             title = extract_title(content, index + 7)
#             res.append(title)
#
#     return res[1:]
#
#
# def extract_title(content, index):
#     if index >= len(content):
#         return ''
#
#     res = ''
#     for i in range(index, len(content)):
#         if content[i] == '<' and i + 8 <= len(content) and content[i:i + 8] == '</title>':
#             return res
#         res += content[i]
#
#     return res
#
#
# print(get_headlines(google_news_url))

total =1
for i in range(1,21):
    total*=i

print(total)
