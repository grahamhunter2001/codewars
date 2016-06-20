from urllib.parse import urlparse
def strip_url_params(url, params_to_strip=[]):
    a = urlparse(url)
    path = a[2]
    query =a[4]
    a = query.split("&")
    if query == '': return path
    b = []
    for item in a:
        b.append(item.split("="))
    d = {}
    if len(a) == 0: return path
    for item in b:
        if item[0] not in d:
            d[item[0]] = item[1]
    for param in params_to_strip:
        if param in d:
            del d[param]
    out_query = ""
    for k in sorted(d.items()):
        if k != list(sorted(d.items()))[-1]:
            out_query += "%s=%s&" % (k[0], k[1])
        else: out_query += "%s=%s" % (k[0], k[1])

    out_str = path + "?" + out_query
    return out_str
