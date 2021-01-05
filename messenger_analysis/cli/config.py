'''App configuration'''


from typing import Any, Set


class _Config:
    '''App configuration'''
    datasource: str = './data'
    include_names: Set[str] = set()
    exclude_groups: bool = False
    exclude_archived: bool = False
    validate: bool = False

    def update(self, args: Any):
        self.datasource = args.datasource
        self.include_names = set(args.includeNames.split(',')) if args.includeNames else set()
        self.exclude_groups = args.excludeGroups
        self.exclude_archived = args.excludeArchived
        self.validate = args.validate

    def __repr__(self):
        return ' '.join((
            f'<Config datasource:{self.datasource}',
            f'include_names:{self.include_names}',
            f'exclude_groups:{self.exclude_groups} exclude_archived:{self.exclude_archived}',
            f'validate:{self.validate}>'
        ))

CONFIG = _Config()