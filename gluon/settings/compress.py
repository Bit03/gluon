
COMPRESS_ENABLED = True
COMPRESS_PRECOMPILERS = (
    # ('text/coffeescript', 'coffee --compile --stdio'),
    ('text/less', '/usr/local/bin/lessc {infile} {outfile}'),
    # ('text/x-sass', 'sass {infile} {outfile}'),
    # ('text/x-scss', 'sass --scss {infile} {outfile}'),
)

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.rCSSMinFilter',
]
COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'

COMPRESS_OUTPUT_DIR = 'release'
COMPRESS_OFFLINE = True