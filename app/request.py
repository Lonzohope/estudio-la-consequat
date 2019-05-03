import urllib.request
import json, requests
from PIL import Image
from . import photos
from pypexels import PyPexels

# Photo = photos.Photo


# # Getting api key

# api_key = '4ad87624acc8e4b68273e54ab783f9817a33fc758693b8978df70f6f98a0bd2c'
# base_url = 'https://api.unsplash.com/photos/?client_id={}'
# # source_url = None
# # pexels_url = None

# # # Getting the news base url
# # def configure_request(app):
# #     global base_url, api_key
# #     api_key =
# #     base_url = app.config["PHOTO_BASE_URL"]


# # def get_photo(photonow):
# #     get_photo_url = base_url.format(photonow, api_key)

# #     with urllib.request.urlopen(get_photo_url) as url:
# #         get_photo_data = url.read()
# #         get_photo_response = json.loads(get_photo_data)

# #         photo_results = None

# #         if get_photo_response['pexels']:  # getting our data from the Api
# #             photo_result_list = get_photo_response["pexels"]
# #             photo_results = process_results(photo_result_list)

# #     return photo_results



# def get_sources():

#     popular_photos = base_url.format(api_key)

#     photo_results = []

#     with urllib.request.urlopen(popular_photos) as url:
#         get_photo_data = url.read()
#         get_photo_response = json.loads(get_photo_data)

#         for photo in get_photo_response:
#             # for key, value in photo.items:
#             #     if key == "urls":

#             image = photo['urls']['raw']

#             # image = requests.get(image)
#             img = Image.open(requests.get(image, stream = True).raw)

#             photo_results.append(img)
        
        
#     return photo_results


# def process_result(source_list):
#     source_results = []
#     for source in source_list:
#         id = source.get("id")
#         name = source.get("name")
#         url = source.get("url")

#         source_obj = source(id, name, url)
#         source_results.append(source_obj)
#         source_results = source_results[0:4]
#     return source_results

# def process_results(photo_list):
#     photo_results = []
#     for photo_item in photo_list:
#         title = photo_item.get("title")
#         description = photo_item.get("description")
#         url = photo_item.get("url")
#         urlToImage = photo_item.get("urlToImage")
#         if title and urlToImage:
#             photo_object = Photo(title, description, url,
#                                  urlToImage)
#             photo_results.append(photo_object)
#             photo_results = photo_results[0:12]

#     return photo_results


# geting the articles
