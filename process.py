from ast import arg
from multiprocessing import parent_process
import os
import sys

def valid_args():
  process_id = -1
  try:
    process_id = int(sys.argv[1])
    if (process_id > 0):
      return process_id
    else:
      print("El número de proceso no puede ser negativo.")
      return -1
  except:
    print("El valor de id de proceso no corresponde a un numero válido.")
    return -1

def main():
  args_size =len(sys.argv)
  if (args_size == 2):
    process_id = valid_args()
    if (process_id != -1):
      # generar calulos:
      process_name_request = "ps -p {} -o comm=".format(process_id)
      print("El nombre del proceso con el id ", process_id, " es: ")
      os.system(process_name_request)
      print("El ID del proceso es:")
      print(process_id)
      parent_process_request = "ps -o ppid= -p {}".format(process_id)
      print("El id del proceso padre es:")
      os.system(parent_process_request)
      process_owner_request = "ps -p {} -o user=".format(process_id)
      print("El propietario del proceso es:")
      os.system(process_owner_request)
      cpu_use_request = "ps -p {} -o %cpu".format(process_id)
      print("El porcentaje de uso del proceso es:")
      os.system(cpu_use_request)
      memory_consume_request = "ps -p {} -o %mem".format(process_id)
      print("El consumo de memoria del proceso es:")
      os.system(memory_consume_request)
      status_request = "ps -p {} -o stat".format(process_id)
      print("El estado del proceso es:")
      os.system(status_request)
      executable_path_request = "readlink -f /proc/{}/exe".format(process_id)
      print("El path del ejecutable del proceso es:")
      os.system(executable_path_request)
  elif (args_size == 1):
    print("Digite el número del proceso como argumento.")
  else:
    print("Digitó más argumentos de los nenesarios.")

if __name__ == "__main__":
    main()
