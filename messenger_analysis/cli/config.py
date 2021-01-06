'''App configuration'''


from typing import Any, Set


class _Config:
    '''App configuration'''
    datasource: str
    include_names: Set[str]
    exclude_groups: bool
    exclude_archived: bool
    validate: bool

    def update(self, args: Any):
        '''Update config with ArgumentParser'''
        self.datasource = args.datasource if args.datasource else './data'
        self.include_names = set(args.includeNames[0].split(',')) if args.includeNames else set()
        self.exclude_groups = args.excludeGroups or False
        self.exclude_archived = args.excludeArchived or False
        self.validate = args.validate or False

    def __repr__(self):
        return ' '.join((
            f'<Config datasource:{self.datasource}',
            f'include_names:{self.include_names}',
            f'exclude_groups:{self.exclude_groups} exclude_archived:{self.exclude_archived}',
            f'validate:{self.validate}>'
        ))

CONFIG = _Config()
