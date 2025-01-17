from django.http import HttpResponse
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return HttpResponse("Hello, World!")

@csrf_exempt
def post_view(request):
    print("POST")
    if request.method == "POST":
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body.decode('utf-8'))

            # Extract coordinates from the parsed JSON data
            x_coordinate = data.get('x-coordinate')
            y_coordinate = data.get('y-coordinate')

            # Log the received coordinates
            print(f"Received x: {x_coordinate}, y: {y_coordinate}")

            # Create a response context to send back (if needed)
            context = {
                'x_coord': x_coordinate,
                'y_coord': y_coordinate
            }

            # Return a JSON response with the received coordinates (if appropriate)
            return JsonResponse(context)

        except json.JSONDecodeError:
            # If JSON is not valid, return a 400 Bad Request error
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    if request.method == "GET":
        return JsonResponse({"message": "This endpoint is for POST requests only"})

    # If the request is not POST, return an error or a default response
    return JsonResponse({'error': 'Invalid method'}, status=405)

def get_view(request):
    print("GET")
    if request.method == "GET":
        pass #handle get request
    if request.method == "POST":
        return JsonResponse({"message": "This endpoint is for GET requests only"})

    # If the request is not POST, return an error or a default response
    return JsonResponse({'error': 'Invalid method'}, status=405)