import urllib.parse


def cleanup_url(input):
    parsed_url = urllib.parse.urlparse(input)
    
    scheme = parsed_url.scheme
    netloc = parsed_url.netloc
    path = parsed_url.path
    params = parsed_url.params
    fragment = parsed_url.fragment
    input_query = parsed_url.query
    
    parsed_input_query = urllib.parse.parse_qs(input_query)
    xt = parsed_input_query['xt']
    
    new_parsed_query = {'xt': xt}
    new_unparsed_query = urllib.parse.urlencode(new_parsed_query, doseq=True, safe=':')
    new_parse_result = urllib.parse.ParseResult(scheme, netloc, path, params, new_unparsed_query, fragment)
    result = urllib.parse.urlunparse(new_parse_result)
    
    return result
