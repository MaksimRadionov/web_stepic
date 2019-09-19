def application(env, start_response):
    a = env['QUERY_STRING'].split('&')
    sta_r =""
    for i in a:
        sta_r = sta_r + str(i) + '\n'
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [bytes(sta_r,encoding='utf8')]
