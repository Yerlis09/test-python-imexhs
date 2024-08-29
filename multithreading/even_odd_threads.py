import threading
import time

class EvenOddPrinter:
    """
    Clase que maneja la impresión de números pares e impares usando hilos.
    """
    def __init__(self, max_number):
        self.max_number = max_number

    def print_even_numbers(self):
        """
        Método para imprimir números pares hasta el máximo definido.
        """
        for i in range(2, self.max_number + 1, 2):
            print(f"Even: {i}")
            time.sleep(0.5)

    def print_odd_numbers(self):
        """
        Método para imprimir números impares hasta el máximo definido.
        """
        for i in range(1, self.max_number + 1, 2):
            print(f"Odd: {i}")
            time.sleep(0.5)

    def start_threads(self):
        """
        Método para iniciar los hilos de impresión de números pares e impares.
        """
        even_thread = threading.Thread(target=self.print_even_numbers)
        odd_thread = threading.Thread(target=self.print_odd_numbers)

        even_thread.start()
        odd_thread.start()

        even_thread.join()
        odd_thread.join()

        print("Both threads have finished.")
