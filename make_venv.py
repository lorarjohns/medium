from venv import EnvBuilder
from types import SimpleNamespace
import os, sys
from typing import BinaryIO
from urllib.parse import urlparse
from urllib.request import urlretrieve
from threading import Thread
from subprocess import Popen, PIPE
import os.path 

class NewVenv(EnvBuilder):
    '''
    This builder installs setuptools and pip so that you can pip
    install other packages into the newly created virtual environment.

    @param nodist: If True, setuptools and pip are not installed.
    @param nopip: If True, pip is not installed.
    @param progress: If pip and setuptools are installed, the progress 
        of installation can be monitored by passing a progress callable.

    '''
    def __init__(self, *args, **kwargs) -> None:
        self.nodist = kwargs.pop('nodist', False)
        self.nopip = kwargs.pop('nopip', False)
        self.progress = kwargs.pop('progress', None)
        self.verbose = kwargs.pop('verbose', False)
        super().__init__(*args, **kwargs)

    def post_setup(self, context: SimpleNamespace) -> None:
        '''
        Set up packages that need to be preinstalled into the
            virtual environment.

        @param context: The information for the virtual environment
            creation request being processed.
        '''
        os.environ['VIRTUAL_ENV'] = context.env_dir
        if not self.nodist:
            self.install_setuptools(context)
        if not self.nopip and not self.nodist:
            self.install_pip(context)

    def reader(self, stream: BinaryIO, context: SimpleNamespace) -> None:
        '''
        Read lines from subprocess output stream and write the information
            to a specified callable or to sys.stderr.
        
        @param stream: Popen.stdout readable byte stream object as returned 
            by open() 
        @param context: The information for the virtual environment
            creation request being processed.
        '''
        progress = self.progress
        while True:
            s = stream.readline()
            if not s:
                break
            if progress is not None:
                progress(s, context)
            else:
                if not self.verbose:
                    sys.stderr.write('.')
                else:
                    sys.stderr.write(s.decode('utf-8'))
                sys.stderr.flush()
        stream.close()

    def install_script(self, context: SimpleNamespace, name: str, url: str) -> None:
        '''
        Install a package into the virtual environment from a script.

        @param context: The information for the virtual environment
            creation request being processed.
        
        @param name: The name of the package being installed.

        @param url: The url of the file containing the install script.
        '''
        
        # Parse the url to create path names
        _, _, path, _, _, _ = urlparse(url)
        fn = os.path.split(path)[-1]
        binpath = context.bin_path
        distpath = os.path.join(binpath, fn)

        # Download script into venv binaries folder
        urlretrieve(url, distpath)
        progress = self.progress

        if self.verbose:
            term = '\n'
        else:
            term = ''

        if progress is not None:
            progress(f'Installing {name} ... {term}', 'main')
        else:
            sys.stderr.write(f'Installing {name} ... {term}')
            sys.stderr.flush()

        # Install script into the venv
        args = [context.env_exe, fn]
        p = Popen(args, stdout=PIPE, stderr=PIPE, cwd=binpath)
        t1 = Thread(target=self.reader, args=(p.stdout, 'stdout'))
        t1.start()
        t2 = Thread(target=self.reader, args=(p.stderr, 'stderr'))
        t2.start()
        p.wait()
        t1.join()
        t2.join()
        if progress is not None:
            progress('done.', 'main')
        else:
            sys.stderr.write('done.\n')

        # Clean up
        os.unlink(distpath)

    def install_setuptools(self, context: SimpleNamespace) -> None:
        '''
        Install setuptools in the virtual environment.

         @param context: The information for the virtual environment
            creation request being processed.
        '''
        url = 'https://bitbucket.org/pypa/setuptools/downloads/ez_setup.py'
        self.install_script(context, 'setuptools', url)
        # clear up the setuptools archive which gets downloaded
        pred = lambda o: o.startswith('setuptools-') and o.endswith('.tar.gz')
        files = filter(pred, os.listdir(context.bin_path))
        for f in files:
            f = os.path.join(context.bin_path, f)
            os.unlink(f)

    def install_pip(self, context: SimpleNamespace) -> None:
        '''
        Install pip in the virtual environment.

        @param context: The information for the virtual environment
                        creation request being processed.
        '''
        url = 'https://bootstrap.pypa.io/get-pip.py'
        self.install_script(context, 'pip', url)

def main(args=None):

    compatible = True
    
    if sys.version_info < (3, 3):
        compatible = False
    elif not hasattr(sys, 'base_prefix'):
        compatible = False
    if not compatible:
        raise ValueError('This script only works with Python 3.3 or greater.')
    else:
        import argparse

        parser = argparse.ArgumentParser(prog=__name__,
                                         description='Creates virtual Python '
                                                     'environments in one or '
                                                     'more target '
                                                     'directories.')
        parser.add_argument('dirs', metavar='ENV_DIR', nargs='+',
                            help='A directory in which to create the'
                                 'virtual environment.')
        parser.add_argument('--no-setuptools', default=False,
                            action='store_true', dest='nodist',
                            help="Don't install setuptools or pip in the "
                                 "virtual environment.")
        parser.add_argument('--no-pip', default=False,
                            action='store_true', dest='nopip',
                            help="Don't install pip in the virtual "
                                 "environment.")
        parser.add_argument('--system-site-packages', default=False,
                            action='store_true', dest='system_site',
                            help='Give the virtual environment access to the '
                                 'system site-packages dir.')
        if os.name == 'nt':
            use_symlinks = False
        else:
            use_symlinks = True
        parser.add_argument('--symlinks', default=use_symlinks,
                            action='store_true', dest='symlinks',
                            help='Try to use symlinks rather than copies, '
                                 'when symlinks are not the default for '
                                 'the platform.')
        parser.add_argument('--clear', default=False, action='store_true',
                            dest='clear', help='Delete the contents of the '
                                               'virtual environment '
                                               'directory if it already '
                                               'exists, before virtual '
                                               'environment creation.')
        parser.add_argument('--upgrade', default=False, action='store_true',
                            dest='upgrade', help='Upgrade the virtual '
                                                 'environment directory to '
                                                 'use this version of '
                                                 'Python, assuming Python '
                                                 'has been upgraded '
                                                 'in-place.')
        parser.add_argument('--verbose', default=False, action='store_true',
                            dest='verbose', help='Display the output '
                                               'from the scripts which '
                                               'install setuptools and pip.')
        options = parser.parse_args(args)
        if options.upgrade and options.clear:
            raise ValueError('you cannot supply --upgrade and --clear together.')
        builder = NewVenv(system_site_packages=options.system_site,
                                       clear=options.clear,
                                       symlinks=options.symlinks,
                                       upgrade=options.upgrade,
                                       nodist=options.nodist,
                                       nopip=options.nopip,
                                       verbose=options.verbose)
        for d in options.dirs:
            builder.create(d)

if __name__ == '__main__':
    rc = 1
    try:
        main()
        rc = 0
    except Exception as e:
        print('Error: %s' % e, file=sys.stderr)
    sys.exit(rc)