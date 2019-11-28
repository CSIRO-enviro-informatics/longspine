import requests
import rdflib

ngs = {
    # 'rdf':	        'http://www.w3.org/1999/02/22-rdf-syntax-ns',
    # 'rdfs':	        'http://www.w3.org/2000/01/rdf-schema',
    # 'owl':          'http://www.w3.org/2002/07/owl',
    # 'time':	        'http://www.w3.org/2006/time',
    # 'dcat':    	    'http://www.w3.org/ns/dcat',
    # 'void':	        'http://rdfs.org/ns/void',
    # 'loci':	        'http://linked.data.gov.au/def/loci',
    # 'skos':	        'http://www.w3.org/2004/02/skos/core',
    # 'org':	        'http://www.w3.org/ns/org',
    #
    # 'long':	        'http://test.linked.data.gov.au/def/longspine',
    # 'aao':	        'http://test.linked.data.gov.au/def/aao',
    # 'agor':	        'http://test.linked.data.gov.au/def/agor',
    # 'crs':	        'http://test.linked.data.gov.au/def/crs',
    # 'pbs':	        'http://test.linked.data.gov.au/def/pbs',
    # 'rda':	        'http://test.linked.data.gov.au/def/rda',

    'agift':    	'https://data.naa.gov.au/def/agift/export/def/agift.rdf',
    'cofog':	    'http://test.linked.data.gov.au/def/cofog',
    'cofoga':	    'http://test.linked.data.gov.au/def/cofog-a',
    'crsth':	    'http://test.linked.data.gov.au/def/crs-th',
    'gpc':	        'http://test.linked.data.gov.au/def/gpc',
    'lgpc':	        'http://test.linked.data.gov.au/def/lgpc',
    'rdavoc':	    'http://test.linked.data.gov.au/def/rdavoc',

    # 'aaodata':	    'http://test.linked.data.gov.au/dataset/aao',
    # 'agordata': 	'http://test.linked.data.gov.au/dataset/agor',
    # 'crsdata':	    'http://test.linked.data.gov.au/dataset/crs',
    # 'pbsdata':	    'http://test.linked.data.gov.au/dataset/pbs',

    'agiftcrsth':	'http://test.linked.data.gov.au/dataset/agiftcrsth',
    'agiftcofoga':	'http://test.linked.data.gov.au/dataset/agiftcofoga',
    'cofogcofoga':	'http://test.linked.data.gov.au/dataset/cofogcofoga',
    'lgpccofog':	'http://test.linked.data.gov.au/dataset/lgpccofog',
    'gpclgpc':	    'http://test.linked.data.gov.au/dataset/gpclgpc'
}

for k, v in ngs.items():
    print('getting {}'.format(k))
    if k in ['dcat', 'rdfs', 'org', 'time']:
        r = requests.get(v + '.ttl')
        with open(k + '.ttl', 'w') as f:
            f.write(r.text)
    elif k in ['skos', 'agift']:
        r = requests.get(v)  # this gets an rdf/xml file
        g = rdflib.Graph().parse(data=r.text, format='xml')
        with open(k + '.ttl', 'w') as f:
            f.write(g.serialize(format='turtle').decode('utf-8'))
    else:
        r = requests.get(v, headers={'Accept': 'text/turtle'})
        with open(k + '.ttl', 'w') as f:
            f.write(r.text)

# small tidy-ups
# removes problematic empty URI in VoID
with open('void.ttl', 'r') as f:
    lines = f.readlines()
with open('void.ttl', 'w') as f:
    for line in lines:
        if line.strip('\n') != '    dcterms:FileFormat <>;':
            f.write(line)
