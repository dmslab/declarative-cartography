#!/usr/bin/env python
__author__ = 'kostas'

from cvl.compiler import CvlCompiler
from cvl.framework.query import Query

if __name__ == '__main__':

	QUERY_DICT = {
		'input': 'openflights_airports',
		'output': 'openflights_airports_gen',
		'rank_by': 'num_routes',
		'zoomlevels': 18,
		'fid': 'ogc_fid',
		'geometry': 'wkb_geometry',
		'subject_to': [('visibility', 16), ('proximity', 5)]
	}

	query = Query(**QUERY_DICT)
	compiler = CvlCompiler()
	print compiler.compile(
		query,
		solver='sga',
		target='postgres'
	)

