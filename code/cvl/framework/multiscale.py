__author__ = 'kostas'
"""
Algorithmic framework
"""


class LadderFramework(object):
    def get_code(self, zoomlevels, code_generator):

        code_generator.Initialize()  # output table, index on output table, analyze!

        for z in reversed(range(zoomlevels)):
            code_generator.InitializeLevel(z)
            code_generator.FindConflicts(z)  # find conflicts
            code_generator.ResolveConflicts(z)  # find records to delete
            code_generator.FinalizeLevel(z)

        code_generator.Finalize()
        return code_generator.get_code()
