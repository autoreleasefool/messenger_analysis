'''App configuration'''


import os
from typing import Any, Set


class _Config:
    '''App configuration'''
    datasource: str
    output: str
    stopwords: str

    plotTimestamps: int
    plotTopWords: int

    include_names: Set[str]
    exclude_groups: bool
    exclude_archived: bool
    include_words: Set[str]
    exclude_words: Set[str]

    validate: bool

    def update(self, args: Any):
        '''Update config with ArgumentParser'''
        self.datasource = args.datasource
        self.output = args.output
        self.stopwords = args.stopwords
        self.plotTimestamps = args.plotTimestamps
        self.plotTopWords = args.plotTopWords
        self.include_names = set(args.includeNames[0].split(',')) if args.includeNames else set()
        self.exclude_groups = args.excludeGroups or False
        self.exclude_archived = args.excludeArchived or False
        self.include_words = set(args.includeWords[0].split(',')) if args.includeWords else set()
        self.exclude_words = set(args.excludeWords[0].split(',')) if args.excludeWords else set()
        self.validate = args.validate or False

    def __repr__(self):
        return ' '.join((
            f'<Config datasource:{self.datasource} stopwords:{self.stopwords} output:{self.output}',
            f'include_names:{self.include_names}',
            f'exclude_groups:{self.exclude_groups} exclude_archived:{self.exclude_archived}',
            f'validate:{self.validate}>'
        ))

    def get_output_filename(self, name: str) -> str:
        return os.path.join(self.output, name)


CONFIG = _Config()
