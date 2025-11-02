import argparse 

parser = argparse.ArgumentParser()


parser.add_argument('-host','--host',help="Digite o nome do host")
parser.add_argument('-user','--user',help="Digite o nome do usuário")


args = parser.parse_args()


opts = f"{args.host} {args.user}"

print("Host/user: ",opts)