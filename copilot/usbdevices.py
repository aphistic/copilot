import os.path
from subprocess import check_output

def _read_file(path):
    with open(path) as f:
        return f.read()

def _blk_parse(blk_line):
    blk_info = {}
    for i, c in enumerate(blk_line):
        if c == ':':
            blk_line = blk_line[i+2:]
            break

    name_start, name_end, val_start, val_end = (0, 0, 0, 0)
    in_val = False
    i = 0
    while i < len(blk_line):
        c = blk_line[i]
        if c == '=' and not in_val:
            name_end = i
            val_start = i+2
            i += 2
            in_val = True
        if c == '"' and in_val:
            val_end = i
            blk_info[blk_line[name_start:name_end].lower()] = blk_line[val_start:val_end]
            name_start = i+2
            in_val = False
        i += 1

    return blk_info

def usb_drives():
    drives = []

    with open('/proc/partitions') as parts_file:
        lines = parts_file.readlines()[2:]
        for line in lines:
            words = [x.strip() for x in line.split()]
            minor_number = int(words[1])
            dev_name = words[3]
            if minor_number % 16 == 0:
                block_path = '/sys/class/block/{}'.format(dev_name)
                if os.path.islink(block_path):
                    if os.path.realpath(block_path).find('/usb') > 0:
                        drives.append(UsbDrive('/dev/{}'.format(dev_name), block_path))

    return drives

class UsbDrive(object):
    def __init__(self, dev_path, info_path):
        self._dev_path = dev_path
        self._info_path = info_path

        self._info = self._discover_info()
        self._partitions = self._discover_parts()

    def __str__(self):
        return self.name()

    def _discover_info(self):
        return {
            'vendor': _read_file(os.path.join(self._info_path, 'device/vendor')).strip(),
            'model': _read_file(os.path.join(self._info_path, 'device/model')).strip(),
            'size': int(_read_file(os.path.join(self._info_path, 'size'))) << 9
        }

        return info

    def _discover_parts(self):
        parts = []
        output = [x.strip().decode(encoding='UTF-8') for x in check_output(['blkid']).split(b'\n')]
        for part in output:
            if part.startswith(self._dev_path):
                part_path = part.split(':')[0]
                parts.append(DrivePartition(part_path, _blk_parse(part)))
        return parts

    def name(self):
        return '{} {} ({}GB)'.format(self.vendor(), self.model(), self.size('g')).strip()

    def path(self):
        return self._dev_path

    def vendor(self):
        return self._info['vendor']

    def model(self):
        return self._info['model']

    def size(self, units='b'):
        units = units.lower()
        if units == 'b':
            new_size = self._info['size']
        elif units == 'k':
            new_size = self._info['size'] / 1024
        elif units == 'm':
            new_size = (self._info['size'] / 1024) / 1024
        elif units == 'g':
            new_size = ((self._info['size'] / 1024) / 1024) / 1024

        return round(new_size, 1)

    def partitions(self):
        return self._partitions


class DrivePartition(object):
    def __init__(self, partition_path, blk_info):
        self._part_path = partition_path
        self._info = blk_info

    def path(self):
        return self._part_path

    def type(self):
        return self._info['type']
