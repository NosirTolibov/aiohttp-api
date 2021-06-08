# product_recommendations/routes.py
from views import get_product_recommendations


def setup_routes(app):
    app.router.add_get('/getProductRecommendations', get_product_recommendations)
