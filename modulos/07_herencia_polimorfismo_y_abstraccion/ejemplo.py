from abc import ABC, abstractmethod


class Notificador(ABC):
    @abstractmethod
    def enviar(self, texto):
        """Recibe str y devuelve una confirmación str; ejemplo local sin red."""


class NotificadorPantalla(Notificador):
    def enviar(self, texto):
        return "Pantalla: " + texto


class NotificadorSimulado(Notificador):
    def enviar(self, texto):
        return "Simulado: " + texto


def avisar(notificador, texto):
    return notificador.enviar(texto)


if __name__ == "__main__":
    for medio in [NotificadorPantalla(), NotificadorSimulado()]:
        print(avisar(medio, "Devolver L1"))
