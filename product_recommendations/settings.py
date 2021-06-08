# product_recommendations/settings.py
import pathlib
import yaml

BASE_DIR = pathlib.Path(__file__).parent.parent
DEFAULT_CONFIG_PATH = BASE_DIR / 'config' / 'api_recom_product.yaml'
CSV_RECOMMENDS_FILE_PATH = BASE_DIR / 'product_recommendations/static' / 'recommends.csv'
PICKLE_RECOMMENDS_FILE_PATH = BASE_DIR / 'product_recommendations/static' / 'recommends.pickle'


def get_config():
    with open(DEFAULT_CONFIG_PATH) as f:
        config = yaml.safe_load(f)
    return config
