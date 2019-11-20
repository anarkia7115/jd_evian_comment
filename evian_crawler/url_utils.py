def generate_comment_request_url(page_num=1, page_size=50):
    # https://sclub.jd.com/comment/productPageComments.action?productId=1384071&score=1&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1
    action_path = "https://sclub.jd.com/comment/productPageComments.action"
    product_id = 1384071
    score = 0
    sort_type = 6
    # page_num = 1
    page_size = 10
    is_shadow_sku = 0
    fold = 1

    # url params
    params = {
        'productId': product_id, 
        'score': score, 
        'sortType': sort_type, 
        'page': page_num, 
        'pageSize': page_size, 
        'isShadowSku': is_shadow_sku, 
        'fold': fold
    }

    # concat url
    result_url = action_path
    for name, val in params.items():
        result_url = add_param_to_url(result_url, name, val)

    # clean_up last &
    result_url = clean_url(result_url)

    return result_url

def add_param_to_url(url: str, name: str, val):
    if url.endswith("&"):  # not first param
        url_format = "{url}{param_name}={param_val}&"
    else:  # first param
        url_format = "{url}?{param_name}={param_val}&"

    return url_format.format(url=url, param_name=name, param_val=val)

def clean_url(url):
    return url.rstrip("&")
