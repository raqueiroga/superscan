import argparse
import socket
from typing import Iterable


def scan_port(host: str, port: int) -> None:
    """Check if a given port on a host is open."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"🔓 Porta {port} aberta em {host}.")
        else:
            print(f"🔒 Porta {port} fechada em {host}.")


def scan_ports(host: str, ports: Iterable[int]) -> None:
    """Scan multiple ports on a given host."""
    for port in ports:
        scan_port(host, port)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="SuperScan - verificador simples de portas"
    )
    parser.add_argument(
        "host",
        nargs="?",
        default="example.com",
        help="Host a ser verificado",
    )
    parser.add_argument(
        "--ports",
        "-p",
        nargs="+",
        type=int,
        default=[80],
        help="Lista de portas a serem checadas",
    )
    args = parser.parse_args()

    print("✅ SuperScan conectado com sucesso!")
    scan_ports(args.host, args.ports)


if __name__ == "__main__":
    main()
