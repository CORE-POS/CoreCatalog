from flask import send_from_directory, request, redirect, url_for, abort
from CoreCatalog import app
from CoreCatalog.database import db_session
from CoreCatalog.models import Items
from CoreCatalog.json_out import json_as_configured
from sqlalchemy import or_

@app.route('/')
def index():
	return send_from_directory(app.static_folder,'api.html')

@app.route('/item/<upc>')
def show_item(upc):
    item = Items.query.get(upc.zfill(13))
    if item == None:
        return json_as_configured({'ErrorCode':404,'ErrorMsg':'Item not found'})
    else:
        return json_as_configured(item.serialize())

@app.route('/all/')
def show_all_items():
    items = Items.query

    return json_as_configured([i.serialize() for i in items]);

@app.route('/item/', methods=['POST'])
def write_item():
    # upc and apikey are required fields
    if not(request.json) or not 'upc' in request.json or not 'apikey' in request.json:
        abort(400)
    # apikey is not valid
    if not(ApiKey.query.filter_by(ApiKey.apikey == request.json['apikey'])):
        abort(403)

    item = Items(upc=request.json['upc'].zfill(13),
                 short_description=request.json.get('short_description', ''), 
                 long_description=request.json.get('long_description', ''), 
                 brand=request.json.get('brand', ''), 
                 unit_size=request.json.get('unit_size', '') )
    db_session.add(item)

    return json_as_configured(item.serialize())
