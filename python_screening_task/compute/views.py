from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from compute.models import Request, CalculationResult
from compute.utils import perform_calculations

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def compute(request: HttpRequest) -> JsonResponse:
    if 'file' not in request.FILES:
        return JsonResponse({"error": "No file provided"}, status=400)

    file = request.FILES['file']

    try:
        result = perform_calculations(file)

        request_record = Request(user=request.user.username, name='example_request', file=file)
        request_record.save()

        calculation_result = CalculationResult(request=request_record, result=result)
        calculation_result.save()
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"result": result, "request_id": request_record.id})
