import functools
from flask import jsonify, request

def json(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        rv = f(*args, **kwargs)
        status_or_headers = None
        headers = None
        if isinstance(rv, tuple):
            rv, status_or_headers, headers = rv + (None,) * (3 - len(rv))
        if isinstance(status_or_headers, (dict, list)):
            headers, status_or_headers = status_or_headers, None
        if not isinstance(rv, dict):
            rv = rv.to_json()
        rv = jsonify(rv)
        if status_or_headers is not None:
            rv.status_code = status_or_headers
        if headers is not None:
            rv.headers.extend(headers)
        return rv
    return wrapped

def datatables(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        draw = request.args.get('sEcho', 1, type=int)
        start = request.args.get('iDisplayStart', 0, type=int)
        per_page = request.args.get('iDisplayLength', 10, type=int)
        sorting_cols = request.args.get('iSortingCols', 0, type=int)
        
        direction, field = '', ''
        for i in range(sorting_cols):
            colIdx = request.args.get('iSortCol_%s' % i)
            direction = request.args.get('sSortDir_%s' % i)
            field = request.args.get('mDataProp_%s' % colIdx)
            
        sort = '{} {}'.format(field, direction)
        
        query = f(*args, **kwargs)
        page = (start // per_page) + 1
        p = query.order_by(sort).paginate(page, per_page)
        
        json = {
            'draw': draw,
            'recordsTotal': p.total,
            'recordsFiltered': p.total
        }

        json['data'] = [item.to_json() for item in p.items]
        return jsonify(json)
    return wrapped
