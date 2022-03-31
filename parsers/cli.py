import argparse


class Parser():
    @staticmethod
    def get_args():
        """Get arguments from the command line"""
        parser = argparse.ArgumentParser(
            description='A handy file organizer for your messiest file systems')
        parser.add_argument('-p', dest='dir_path',
                            help='Path to the Directory you want to organize')
        parser.add_argument(
            '-rd', help='Remove any duplicates that may be found')
        parser.add_argument(
            '-size', help='Returns the total size of the directory')

        return parser.parse_args()
