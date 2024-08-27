import tkinter as tk
from tkinter import messagebox, simpledialog


class CuatroEnLinea:
    def __init__(self, root, tamaño):
        self.root = root
        self.tamaño = tamaño
        self.tablero = [[' ' for _ in range(tamaño)] for _ in range(tamaño)]
        self.turno = 'X'
        self.botones = [[None for _ in range(tamaño)] for _ in range(tamaño)]
        self.jugador1_puntaje = 0
        self.jugador2_puntaje = 0
        self.victorias_consecutivas_1 = 0
        self.victorias_consecutivas_2 = 0
        self.crear_tablero()

    def crear_tablero(self):
        for fila in range(self.tamaño):
            for col in range(self.tamaño):
                boton = tk.Button(self.root, text=' ', width=10, height=4,
                                  command=lambda col=col: self.colocar_ficha(col))
                boton.grid(row=fila, column=col)
                self.botones[fila][col] = boton

    def colocar_ficha(self, col):
        for i in range(self.tamaño - 1, -1, -1):
            if self.tablero[i][col] == ' ':
                self.tablero[i][col] = self.turno
                self.botones[i][col].config(text=self.turno, state=tk.DISABLED)
                break
        else:
            return

        if self.es_ganador(self.turno):
            messagebox.showinfo("Fin del Juego", f"¡{self.turno} ha ganado!")
            self.actualizar_puntaje()
            self.reiniciar_tablero()
        elif self.tablero_lleno():
            messagebox.showinfo("Fin del Juego", "¡Empate! El tablero está lleno.")
            self.reiniciar_tablero()
        else:
            self.turno = 'O' if self.turno == 'X' else 'X'

    def es_ganador(self, ficha):

        for fila in range(self.tamaño):
            for col in range(self.tamaño - 3):
                if all(self.tablero[fila][col + i] == ficha for i in range(4)):
                    return True


        for col in range(self.tamaño):
            for fila in range(self.tamaño - 3):
                if all(self.tablero[fila + i][col] == ficha for i in range(4)):
                    return True


        for col in range(self.tamaño - 3):
            for fila in range(3, self.tamaño):
                if all(self.tablero[fila - i][col + i] == ficha for i in range(4)):
                    return True

        for col in range(self.tamaño - 3):
            for fila in range(self.tamaño - 3):
                if all(self.tablero[fila + i][col + i] == ficha for i in range(4)):
                    return True

        return False

    def tablero_lleno(self):
        return all(self.tablero[0][col] != ' ' for col in range(self.tamaño))

    def actualizar_puntaje(self):
        if self.turno == 'X':
            self.jugador1_puntaje += 1 
            self.victorias_consecutivas_1 += 1
            self.victorias_consecutivas_2 = 0
            if self.victorias_consecutivas_1 >= 2:
                self.jugador1_puntaje *= 3
        else:
            self.jugador2_puntaje += 1
            self.victorias_consecutivas_2 += 1
            self.victorias_consecutivas_1 = 0
            if self.victorias_consecutivas_2 >= 2:
                self.jugador2_puntaje *= 3

        self.mostrar_puntaje()

    def mostrar_puntaje(self):
        messagebox.showinfo("Puntaje",
                            f"Jugador 1 (X): {self.jugador1_puntaje}\nJugador 2 (O): {self.jugador2_puntaje}")

    def reiniciar_tablero(self):
        self.tablero = [[' ' for _ in range(self.tamaño)] for _ in range(self.tamaño)]
        for fila in range(self.tamaño):
            for col in range(self.tamaño):
                self.botones[fila][col].config(text=' ', state=tk.NORMAL)
        self.turno = 'X'


def main():
    root = tk.Tk()
    root.title("Cuatro en Línea")

    tamaño = 0
    while tamaño < 4 or tamaño > 6:
        tamaño = simpledialog.askinteger("Tamaño del tablero", "Elige el tamaño del tablero (4-6):")

    juego = CuatroEnLinea(root, tamaño)

    root.mainloop()


if __name__ == "__main__":
    main()

















