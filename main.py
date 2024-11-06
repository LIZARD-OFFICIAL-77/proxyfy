from server import Waitress,request

import curlify
import re

app = Waitress(__name__)

@app.route('/', defaults={'path': ''},methods=["DELETE","POST","GET","OPTIONS","PUT","PATCH"])
@app.route('/<path:path>',methods=["DELETE","POST","GET","OPTIONS","PUT","PATCH"])
def catch(path):
    """
        request.args: the key/value pairs in the URL query string
        request.form: the key/value pairs in the body, from a HTML post form, or JavaScript request that isn't JSON encoded
        request.files: the files in the body, which Flask keeps separate from form. HTML forms must use enctype=multipart/form-data or files will not be uploaded.
        request.values: combined args and form, preferring args if keys overlap
        request.json: parsed JSON data. The request must have the application/json content type, or use request.get_json(force=True) to ignore the content type.
    """
    
    request.body = request.data
    
    curlified = curlify.to_curl(request)
    curlified = re.sub("http(.*)\"","%%REQUEST_URL%%\"",curlified)
    curlified = re.sub("http://(.*)","%%REQUEST_URL%%",curlified)
    curlified = re.sub("https://(.*)","%%REQUEST_URL%%",curlified)
    
    return curlified,200


app.waitress_serve(port=8000)