import pandas as pd

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        try:
            data = pd.read_excel(self.file_path)
            return data
        except Exception as e:
            print(f"Error al cargar los datos: {e}")
            return None

    def process_data(self, data):
        # Realiza cualquier procesamiento necesario en los datos
        # Asegúrate de no eliminar o transformar datos de manera incorrecta
        return data

