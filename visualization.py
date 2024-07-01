import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

class DataVisualizer:
    def __init__(self, data):
        self.data = data

    def plot_country(self):
        if 'Pais' in self.data.columns:
            country_counts = self.data['Pais'].value_counts().sort_values(ascending=False)
            country_counts_df = country_counts.reset_index()
            country_counts_df.columns = ['Pais', 'Cantidad']
            st.table(country_counts_df.head(20))
        else:
            st.warning("'Pais' no encontrada en los datos.")

    def plot_education(self):
        if 'Nivel educativo' in self.data.columns:
            education_counts = self.data['Nivel educativo'].value_counts()
            sorted_counts = education_counts.sort_values(ascending=False)
            total_count = sorted_counts.sum()
            
            # Calcular el porcentaje y agregarlo como una nueva columna
            sorted_counts_df = pd.DataFrame(sorted_counts).reset_index()
            sorted_counts_df.columns = ['Nivel educativo', 'Cantidad']
            sorted_counts_df['Porcentaje (%)'] = (sorted_counts_df['Cantidad'] / total_count) * 100
            
            st.table(sorted_counts_df)
        else:
            st.warning("'Nivel educativo' no encontrada en los datos.")

    def plot_age(self):
        st.image('Edad.png', caption='Distribución por Edad')

    def plot_occupation(self):
        if 'Employment/Ocupación BD aparte' in self.data.columns:
            occupation_counts = self.data['Employment/Ocupación BD aparte'].value_counts().sort_values(ascending=False)
            st.bar_chart(occupation_counts)
        else:
            st.warning("'Employment/Ocupación BD aparte' no encontrada en los datos.")

    def plot_work_mode(self):
        if 'Modalidad de trabajo' in self.data.columns:
            work_mode_counts = self.data['Modalidad de trabajo'].value_counts()
            fig, ax = plt.subplots()
            ax.pie(work_mode_counts, labels=work_mode_counts.index, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            st.pyplot(fig)
        else:
            st.warning("'Modalidad de trabajo' no encontrada en los datos.")

    def plot_main_branch(self):
        if 'Rama principal' in self.data.columns:
            main_branch_counts = self.data['Rama principal'].value_counts().sort_values(ascending=False)
            st.bar_chart(main_branch_counts)
        else:
            st.warning("'Rama principal' no encontrada en los datos.")

    def plot_coding_reason(self):
        if 'CodingActivities/Motivo de desarrollar BD aparte' in self.data.columns:
            coding_reason_counts = self.data['CodingActivities/Motivo de desarrollar BD aparte'].value_counts().sort_values(ascending=False)
            st.bar_chart(coding_reason_counts)
        else:
            st.warning("'CodingActivities/Motivo de desarrollar BD aparte' no encontrada en los datos.")

    def plot_learning_method(self):
        if 'LearnCode' in self.data.columns:
            learning_method_counts = self.data['LearnCode'].value_counts().sort_values(ascending=False)
            st.bar_chart(learning_method_counts)
        else:
            st.warning("'LearnCode' no encontrada en los datos.")

    def plot_development_area(self):
        if 'Tipo de desarrollo' in self.data.columns:
            development_area_counts = self.data['Tipo de desarrollo'].value_counts().sort_values(ascending=False)
            st.bar_chart(development_area_counts)
        else:
            st.warning("'Tipo de desarrollo' no encontrada en los datos.")

    def plot_years_programming(self):
        st.image('lineas.png', caption='¿Cuantos Años lleva programando?')

    def plot_top_languages_used(self):
        data = pd.read_excel('BD apart LanguageHaveWorkedWith.xlsx')
        language_counts = data['LanguageHaveWorkedWith'].str.split(';').explode().value_counts().head(10)
        st.bar_chart(language_counts)
        fig, ax = plt.subplots()
        ax.pie(language_counts, labels=language_counts.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

    def plot_top_languages_desired(self):
        data = pd.read_excel('BD apart LanguageWantToWorkWith.xlsx')
        language_counts = data['LanguageWantToWorkWith'].str.split(';').explode().value_counts().head(10)
        st.bar_chart(language_counts)
        fig, ax = plt.subplots()
        ax.pie(language_counts, labels=language_counts.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

    def plot_top_databases_used(self):
        data = pd.read_excel('BD apart DatabaseHaveWorkedWith.xlsx')
        db_counts = data['DatabaseHaveWorkedWith'].value_counts().head(10)
        st.bar_chart(db_counts)
        fig, ax = plt.subplots()
        ax.pie(db_counts, labels=db_counts.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

    def plot_top_databases_desired(self):
        data = pd.read_excel('BD apart DatabaseWantToWorkWith.xlsx')
        db_counts = data['DatabaseWantToWorkWith'].value_counts().head(10)
        st.bar_chart(db_counts)
        fig, ax = plt.subplots()
        ax.pie(db_counts, labels=db_counts.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

    def plot_top_webframeworks_used(self):
        data = pd.read_excel('BD apart WebframeHaveWorkedWith.xlsx')
        webframework_counts = data['WebframeHaveWorkedWith'].value_counts().head(10)
        st.bar_chart(webframework_counts)
        fig, ax = plt.subplots()
        ax.pie(webframework_counts, labels=webframework_counts.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

    def plot_top_webframeworks_desired(self):
        data = pd.read_excel('BD apart WebframeWantToWorkWith.xlsx')
        webframework_counts = data['WebframeWantToWorkWith'].value_counts().head(10)
        st.bar_chart(webframework_counts)
        fig, ax = plt.subplots()
        ax.pie(webframework_counts, labels=webframework_counts.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

# main.py
import streamlit as st
from data_processing import DataProcessor
from visualization import DataVisualizer

def main():
    st.title("Análisis de Encuesta de Programadores")

    # Crear una instancia de DataProcessor
    data_processor = DataProcessor('BDparaTp.xlsx')

    # Cargar y procesar los datos
    data = data_processor.load_data()

    if data is not None:
        # Sidebar para la navegación
        st.sidebar.title("Navegación")
        selection = st.sidebar.radio("Ir a", ["Introducción", "Conociendo a los encuestados", "Herramientas Utilizadas vs Deseadas"])

        # Introducción
        if selection == "Introducción":
            st.header("Introducción")
            st.write("""
            El conjunto de datos analizado son los resultados de la 'Encuesta de desarrolladores de Stack Overflow 2023'. La encuesta se envió del 8 de mayo de 2023 al 19 de mayo de 2023. La mediana del tiempo dedicado a la encuesta para respuestas calificadas fue de 17 minutos.

            Los encuestados fueron reclutados principalmente a través de canales propiedad de Stack Overflow. Las 5 principales fuentes de encuestados fueron mensajes en el sitio, publicaciones de blog, listas de correo electrónico, publicaciones meta.stackoverflow, anuncios publicitarios y publicaciones en redes sociales. Dado que los encuestados fueron reclutados de esta manera, los usuarios altamente comprometidos en Stack Overflow tenían más probabilidades de notar los enlaces para la encuesta y hacer clic para comenzarla.
            """)

            # Mostrar cantidad total de encuestados
            st.subheader("Cantidad total de encuestados")
            total_encuestados = len(data)
            st.markdown(f"*Total de encuestados:* {total_encuestados}")

            # Mostrar muestra de datos cargados
            st.subheader("Muestra de datos cargados")
            st.write(data.head())

        # Conociendo a los encuestados
        elif selection == "Conociendo a los encuestados":
            st.header("Conociendo a los encuestados")
            data_visualizer = DataVisualizer(data)

            # Mostrar gráficos de cada sección
            st.subheader("País")
            data_visualizer.plot_country()

            st.subheader("Educación")
            data_visualizer.plot_education()

            st.subheader("Edad")
            data_visualizer.plot_age()

            st.subheader("Ocupación")
            data_visualizer.plot_occupation()

            st.subheader("Modalidad de trabajo")
            data_visualizer.plot_work_mode()

            st.subheader("Rama principal")
            data_visualizer.plot_main_branch()

            st.subheader("Razón de programar")
            data_visualizer.plot_coding_reason()

            st.subheader("Como aprendió a programar")
            data_visualizer.plot_learning_method()

            st.subheader("Área de desarrollo")
            data_visualizer.plot_development_area()

            st.subheader("Años programando en total")
            data_visualizer.plot_years_programming()

        # Herramientas Utilizadas vs Deseadas
        elif selection == "Herramientas Utilizadas vs Deseadas":
            st.header("Herramientas Utilizadas vs Deseadas")
            data_visualizer = DataVisualizer(data)

            # Mostrar gráficos de cada sección
            st.subheader("10 lenguajes más utilizados")
            data_visualizer.plot_top_languages_used()

            st.subheader("10 lenguajes más deseados")
            data_visualizer.plot_top_languages_desired()

            st.subheader("Las 10 bases de datos más utilizadas")
            data_visualizer.plot_top_databases_used()

            st.subheader("Las 10 bases de datos más deseadas")
            data_visualizer.plot_top_databases_desired()

            st.subheader("Los 10 marcos web y tecnologías más utilizadas")
            data_visualizer.plot_top_webframeworks_used()

            st.subheader("Los 10 marcos web y tecnologías más deseadas")
            data_visualizer.plot_top_webframeworks_desired()

    else:
        st.error("No se pudo cargar el archivo de datos.")

if __name__ == "__main__":
    main()
