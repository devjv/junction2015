import os
from flask import current_app
from flask.ext.assets import Environment, Bundle

assets = Environment()

# assets.load_path = [
#     os.path.join(os.path.dirname(__file__), 'bower_components'),
# ]

assets.register(
    'js_all',
    Bundle(
        '**.js',
        output='js_all.js'
    )
)
