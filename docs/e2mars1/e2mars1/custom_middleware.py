# class CustomMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, required):
#         # Code to be executed for each request before the view (get_response)
#         print("Request:", equired)
#
#         response = self.get_response(equired)
#         print("Response:", response)
#         # Code to be executed for each request/response after the view
#         return response