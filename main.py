import logging
import os
import sys
from collections import namedtuple


def files_dirs_info(path: str):
    tree = os.walk(os.path.join(path))
    logger = logging.getLogger(__name__)
    format = '{asctime:<5} - {levelname:<5} - {msg}'
    logging.basicConfig(filename='walk_dir_log.log', filemode='a', encoding='UTF-8',
                        level=logging.INFO, style='{', format=format)

    FileInfo = namedtuple('FileInfo', ['name', 'expansion', 'parent_dir'])
    DirInfo = namedtuple('DirInfo', ['name', 'parent_dir'])
    for i in tree:
        if i[2]:
            for j in i[2]:
                if '.' in j:
                    fInfo = FileInfo(j.split('.')[0], "." + j.split('.')[1], i[0])
                    logger.info(msg=f'Файл "{fInfo.name}" с расширением '
                                    f'"{fInfo.expansion}" находится в директории '
                                    f'"{fInfo.parent_dir}"')
                else:
                    fInfo = FileInfo(j.split('.')[0], 'не указанным', i[0])
                    logger.info(msg=f'Файл "{fInfo.name}" с {fInfo.expansion} расширением '
                                    f'находится в директории '
                                    f'"{fInfo.parent_dir}"')
        if i[1]:
            for j in i[1]:
                dInfo = DirInfo(j, i[0])
                logger.info(msg=f'Папка "{dInfo.name}" находится в директории '
                                f'"{dInfo.parent_dir}"')


if __name__ == '__main__':
    files_dirs_info(sys.argv[1])
