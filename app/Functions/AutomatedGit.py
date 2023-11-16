import subprocess




def git_add_commit_push(commit_message):
    try:
        # Agregar todos los archivos modificados
        subprocess.check_call(['git', 'add', '.'])

        # Hacer commit con un mensaje proporcionado
        subprocess.check_call(['git', 'commit', '-m', commit_message])

        # Hacer push a la rama main
        subprocess.check_call(['git', 'push', 'origin', 'main'])

        print("Cambios añadidos, commit y push realizados correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Ocurrió un error: {e}")


