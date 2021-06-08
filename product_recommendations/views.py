# product_recommendations/views.py
from aiohttp import web
from utils import get_recommendation_list


async def get_product_recommendations(request):
    """
    Response json recommendation sku list
    :param request:
    :return:
    """
    sku = request.rel_url.query.get('sku', None)
    min_threshold = request.rel_url.query.get('min_threshold', None)
    if sku is None:
        error_message = {'status': 'error', 'error_message': 'Required parameter sku not set'}
        return web.json_response(error_message, status=400)
    data = get_recommendation_list(sku, min_threshold)
    return web.json_response(data, status=200)


