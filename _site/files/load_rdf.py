import requests
import json


# get all the server files for import
files_for_importing = []
r = requests.get(
    'http://db.longspine.cat/rest/data/import/server/main',
    headers={'Accept': 'application/json'},
    auth=('admin', '????')
)

if r.ok:
    for f in r.json():
        files_for_importing.append(f['name'])

# print('Files for Importing:')
# print('\n'.join(files_for_importing))

# files -> Names Graphs
ngs = {
    'rdf':	        'http://www.w3.org/1999/02/22-rdf-syntax-ns',
    'rdfs':	        'http://www.w3.org/2000/01/rdf-schema',
    'owl':          'http://www.w3.org/2002/07/owl',
    'time':	        'http://www.w3.org/2006/time',
    'dcat':    	    'http://www.w3.org/ns/dcat',
    'void':	        'http://rdfs.org/ns/void',
    'loci':	        'http://linked.data.gov.au/def/loci',
    'skos':	        'http://www.w3.org/2004/02/skos/core',
    'org':	        'http://www.w3.org/ns/org',

    'long':	        'http://test.linked.data.gov.au/def/longspine',
    'aao':	        'http://test.linked.data.gov.au/def/aao',
    'agor':	        'http://test.linked.data.gov.au/def/agor',
    'crs':	        'http://test.linked.data.gov.au/def/crs',
    'pbs':	        'http://test.linked.data.gov.au/def/pbs',
    'rda':	        'http://test.linked.data.gov.au/def/rda',

    'agift':    	'https://data.naa.gov.au/def/agift/export/def/agift.rdf',
    'cofog':	    'http://test.linked.data.gov.au/def/cofog',
    'cofoga':	    'http://test.linked.data.gov.au/def/cofog-a',
    'crsth':	    'http://test.linked.data.gov.au/def/crs-th',
    'gpc':	        'http://test.linked.data.gov.au/def/gpc',
    'lgpc':	        'http://test.linked.data.gov.au/def/lgpc',
    'rdavoc':	    'http://test.linked.data.gov.au/def/rdavoc',

    # 'aaodata':	    'http://test.linked.data.gov.au/dataset/aao',
    # 'agordata': 	    'http://test.linked.data.gov.au/dataset/agor',
    # 'crsdata':	    'http://test.linked.data.gov.au/dataset/crs',
    # 'pbsdata':	    'http://test.linked.data.gov.au/dataset/pbs',

    'agiftcrsth':	'http://test.linked.data.gov.au/dataset/agiftcrsth',
    'agiftcofoga':	'http://test.linked.data.gov.au/dataset/agiftcofoga',
    'cofogcofoga':	'http://test.linked.data.gov.au/dataset/cofogcofoga',
    'lgpccofog':	'http://test.linked.data.gov.au/dataset/lgpccofog',
    'gpclgpc':	    'http://test.linked.data.gov.au/dataset/gpclgpc'
}

# print('Files -> Named Graphs:')
# for k, v in ngs.items():
#     print('{}.ttl:\t\t{}'.format(k, v))


print('Checking that all files for NGs are present for import:')
all_present = True
for k in ngs.keys():
    if k + '.ttl' not in files_for_importing:
        print(k + '.ttl is missing')
        all_present = False

if all_present:
    print('All files present')

# exit()

# load all available files

for k, v in ngs.items():
    f = k + '.ttl'

    '''
    Equivalent CURL command (no pwd):
    curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"fileNames": ["lgpc.ttl"],"importSettings": {"baseURI": "string","context": "http://linked.data.gov.au/def/lgpc","data": "lgpc.ttl","forceSerial": true,"format": "string","message": "string","name": "string","parserSettings": {"failOnUnknownDataTypes": true,"failOnUnknownLanguageTags": true,"normalizeDataTypeValues": true,"normalizeLanguageTags": true,"preserveBNodeIds": true,"stopOnError": true,"verifyDataTypeValues": true,"verifyLanguageTags": true,"verifyRelativeURIs": true,"verifyURISyntax": true},"replaceGraphs": ["http://linked.data.gov.au/def/lgpc"],"status": "PENDING","timestamp": 0,"type": "string","xRequestIdHeaders": "string"}}' 'http://admin:?????@db.longspine.cat/rest/data/import/server/main'
    '''

    post_body_template = {
      'fileNames': [
        f
      ],
      'importSettings': {
        'baseURI': 'string',
        'context': v,
        'data': f,
        'forceSerial': True,
        'format': 'turtle',
        'message': '',
        'name': 'LGPC',
        'parserSettings': {
          'failOnUnknownDataTypes': True,
          'failOnUnknownLanguageTags': True,
          'normalizeDataTypeValues': True,
          'normalizeLanguageTags': True,
          'preserveBNodeIds': True,
          'stopOnError': True,
          'verifyDataTypeValues': True,
          'verifyLanguageTags': True,
          'verifyRelativeURIs': True,
          'verifyURISyntax': True
        },
        'replaceGraphs': [
          v
        ],
        'status': 'PENDING',
        'timestamp': 0,
        'type': '',
        'xRequestIdHeaders': ''
      }
    }

    r = requests.post(
        'http://db.longspine.cat/rest/data/import/server/main',
        data=json.dumps(post_body_template),
        headers={
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
        auth=('admin', '????')
    )
    if r.ok:
        print(f + ' ok')
    else:
        print(r.status_code)
        print(r.text)
