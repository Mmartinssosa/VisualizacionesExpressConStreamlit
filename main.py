import streamlit as st
from data_processing import DataProcessor
from visualization import DataVisualizer

def main():
    st.image('Unab.png', caption='Universidad Nacional de Almirante Brown')
    st.title("Usando Streamlit para analizar intereses de Programadores del mundo")

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
            st.markdown("""
            *Materia Programación Avanzada, Trabajo Integrador Ariana Barrios y Martín Sosa*

            Presentamos un ejemplo de uso de la biblioteca Streamlit de Python, un framework diseñado para crear rápidamente aplicaciones web enfocadas en la visualización de datos. Ideal para prototipos rápidos de aplicaciones web con un fuerte enfoque en la visualización de datos.

            Desarrollamos una aplicación web interactiva para visualizar y analizar un conjunto de datos de interés general llamado 'Análisis de Encuesta de Programadores', obtenido de Kaggle. Este conjunto de datos contiene los resultados de una encuesta mundial de desarrolladores realizada en 2023, diseñada para explorar intereses generales y tendencias en la comunidad de programadores.
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
