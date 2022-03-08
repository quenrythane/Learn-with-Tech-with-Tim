import my_package
import my_package.package_file_2

if __name__ == '__main__':
    print(__name__)

    my_package.function_file_1()  # dzięki temu że w pliku __init__ zaimportowałem package_file_1 to tutaj mogę podać że
                # że chce użyć pakietu i od razu użyć nazwy funkcji

    my_package.package_file_2.function_file_2()  # tego nie dodałem w __init__ więc muszę się męczyć: nazwa_paczki.nazwa_pliku.nazwa_funkcji()



