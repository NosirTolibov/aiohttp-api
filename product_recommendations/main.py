# product_recommendations/main.py

from aiohttp import web

from utils import convert_csv_pickle
from routes import setup_routes
from settings import get_config, CSV_RECOMMENDS_FILE_PATH


def init_app():
    app = web.Application()
    app['config'] = get_config()

    # setup views and routes
    setup_routes(app)

    return app


def main():
    app = init_app()

    config = get_config()
    web.run_app(app,
                host=config['host'],
                port=config['port'])


if __name__ == '__main__':
    convert_csv_pickle(CSV_RECOMMENDS_FILE_PATH)
    main()
