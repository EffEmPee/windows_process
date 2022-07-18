from email import charset
from multiprocessing import Process
import os, signal

def info(name):
    pid = os.getpid()
    ppid = os.getppid()

    with open(name + '.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n\n----------------child process: {pid}----------------\n')
        file.write(f'\n\n----------------child of: {ppid}----------------\n')

        aux = 1
        while(aux < 6):
            file.write(f'\nexecution n°{aux}')
            aux += 1
        
        file.write(f'\n\nkilling process {pid}...')
        file.close()

    os.kill(pid, signal.SIGTERM)


def create_file(name):
    with open(name + '.txt', 'w', encoding='utf-8') as file:
        file.write(f'module name: {__name__}')
        file.write(f'\nprocess id: {os.getpid()}')
        file.write(f'\nparent process: {os.getppid()}')
        file.close()

    info_p = Process(target=info, args=(name, ))
    info_p.start()
    info_p.join()


if __name__ == '__main__':
    p = Process(target=create_file, args=('test',))
    p.start()
    p.join()
