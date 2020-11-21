import os
import sys

if __name__ == '__main__':
    try:
        from django.core.management import execute_from_command_line

        print("Importing Django.", "SUCCESS")
    except ImportError as exc:
        print("Importing Django.", "FAILED")

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tools.configs')
    execute_from_command_line(sys.argv)
