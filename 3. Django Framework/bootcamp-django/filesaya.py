# minimum manage.py

import os
import sys
# import configsaya

if __name__ == '__main__':
    try:
        from django.core.management import execute_from_command_line
        print("Mengimport Django.", "BERHASIL")
    except ImportError as exc:
        print("Mengimport Django.", "GAGAL")
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configsaya')
    execute_from_command_line(sys.argv)