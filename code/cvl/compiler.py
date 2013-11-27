"""
The compiler uses algorithms in framework.algorithms together with engine specific code generators
"""

import sys

import cvl.framework.multiscale as multiscale
import cvl.engines


class CvlCompiler(object):
	"""Compiler that turns CVL into transaction code"""
	def __init__(self):
		super(CvlCompiler, self).__init__()

	def compile(self, query, solver='heuristic', target='postgres', algorithmic_framework='ladder', **options):
		solver = solver.lower()
		target = target.lower()
		algorithmic_framework = algorithmic_framework.lower()

		if target == 'postgres':
			code_generator = cvl.engines.postgres.CodeGenerator(query, solver, **options)
		else:
			raise NotImplementedError("target not implemented: %s" % str(target))

		if algorithmic_framework == 'ladder':
			return multiscale.LadderFramework().get_code(query.zoomlevels, code_generator)
		else:
			raise NotImplementedError("algorithmic framework not implemented: %s" % str(algorithmic_framework))


if __name__ == '__main__':
	print 'try 7k_pt_cells_bound.py in the root directory'





