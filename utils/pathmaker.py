from config_files import config


class Pathmaker:
    def __init__(self, path: list):
        self.path = path

    def __str__(self):
        path = ''
        for dir in self.path:
            path += f'/{dir}'
        return path

    def resolve(self) -> str:
        return str(self)


def create_path(*paths: str) -> Pathmaker:
    # Strip end and start /
    final_path = []
    for path in paths:
        path = path.strip('/')
        path = path.split('/')
        final_path += list(filter(None, path))
    return Pathmaker(final_path)


def create_priority_path(priority_path: str, backup_path: str, path: str) -> Pathmaker:
    if config.ROOT in priority_path.split('/'):
        return create_path(priority_path, path)
    else:
        return create_path(backup_path, priority_path, path)