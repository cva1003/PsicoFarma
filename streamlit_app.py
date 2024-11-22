import streamlit as st
from fpdf import FPDF
from io import BytesIO

# Función para generar el PDF con el logo
def generar_pdf(nombre, edad, sexo, fecha_nac, ejercicio, alcohol, fumador, gen, medicamento, alelo, recomendacion):
    pdf = FPDF()
    pdf.add_page()
    
    # Insertar logo
    pdf.image("logo.png", x=10, y=8, w=30)  # Ajusta posición y tamaño
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(0, 40, "Recomendaciones Farmacogenéticas", ln=True, align="C")
    pdf.ln(10)

    # Línea separadora
    pdf.set_draw_color(0, 123, 255)  # Azul
    pdf.set_line_width(0.5)
    pdf.line(10, 40, 200, 40)
    pdf.ln(10)

    # Contenido del PDF
    pdf.set_font("Arial", size=12)
    pdf.set_text_color(0, 0, 0)

    pdf.cell(0, 10, "Información Personal:", ln=True, align="L")
    pdf.cell(0, 10, f"Nombre: {nombre}", ln=True)
    pdf.cell(0, 10, f"Edad: {edad} años", ln=True)
    pdf.cell(0, 10, f"Sexo: {sexo}", ln=True)
    pdf.cell(0, 10, f"Fecha de nacimiento: {fecha_nac}", ln=True)
    pdf.ln(5)

    pdf.cell(0, 10, "Estilo de Vida:", ln=True, align="L")
    pdf.cell(0, 10, f"Ejercicio regular: {'Sí' if ejercicio == 'Sí' else 'No'}", ln=True)
    pdf.cell(0, 10, f"Consumo de alcohol: {'Sí' if alcohol == 'Sí' else 'No'}", ln=True)
    pdf.cell(0, 10, f"Fuma o ha fumado: {'Sí' if fumador == 'Sí' else 'No'}", ln=True)
    pdf.ln(5)

    pdf.cell(0, 10, "Información Genética y Médica:", ln=True, align="L")
    pdf.cell(0, 10, f"Gen seleccionado: {gen}", ln=True)
    pdf.cell(0, 10, f"Medicamento seleccionado: {medicamento}", ln=True)
    pdf.cell(0, 10, f"Alelo seleccionado: {alelo}", ln=True)
    pdf.ln(5)

    pdf.set_text_color(220, 53, 69)
    pdf.cell(0, 10, "Recomendación:", ln=True, align="L")
    pdf.set_text_color(0, 0, 0)
    pdf.multi_cell(0, 10, recomendacion, align="L")
    pdf.ln(5)

    pdf_output = BytesIO()
    pdf_output.write(pdf.output(dest="S").encode("latin1"))
    pdf_output.seek(0)
    return pdf_output

# Mostrar logo en la página web
st.image("logo.png", width=150)

st.title("Recomendaciones Farmacogenéticas")
st.write("Esta aplicación proporciona recomendaciones basadas en genes y medicamentos.")

# Formulario de entrada
nombre = st.text_input("Nombre y apellidos", "Pablo Fuentes")
edad = st.number_input("Edad", value=20)
sexo = st.selectbox("Sexo", ["Hombre", "Mujer"])
fecha_nac = st.date_input("Fecha de nacimiento")
ejercicio = st.radio("¿Realizas ejercicio regularmente?", ["Sí", "No"])
alcohol = st.radio("¿Consumes alcohol regularmente?", ["Sí", "No"])
fumador = st.radio("¿Fumas o has fumado alguna vez?", ["Sí", "No"])
gen = st.selectbox("Selecciona un gen", ["CYP2D6"])
medicamento = st.selectbox("Selecciona un medicamento", ["Venlafaxina"])
alelo = st.selectbox("Selecciona un alelo", ["*1/*10", "*1/*2", "*2/*2"])
recomendacion = "Tratamiento con dosis normal"  # Este valor puedes calcularlo dinámicamente

# Mostrar resumen y generar PDF
if st.button("Generar resumen"):
    st.subheader("Resumen")
    st.write(f"**Nombre:** {nombre}")
    st.write(f"**Edad:** {edad}")
    st.write(f"**Sexo:** {sexo}")
    st.write(f"**Fecha de nacimiento:** {fecha_nac}")
    st.write(f"**Ejercicio regular:** {ejercicio}")
    st.write(f"**Consumo de alcohol:** {alcohol}")
    st.write(f"**Fuma o ha fumado:** {fumador}")
    st.write(f"**Gen seleccionado:** {gen}")
    st.write(f"**Medicamento seleccionado:** {medicamento}")
    st.write(f"**Alelo seleccionado:** {alelo}")
    st.write(f"**Recomendación:** {recomendacion}")

    pdf_data = generar_pdf(nombre, edad, sexo, fecha_nac, ejercicio, alcohol, fumador, gen, medicamento, alelo, recomendacion)
    st.download_button(
        label="Descargar PDF",
        data=pdf_data,
        file_name="recomendaciones_farmacogeneticas.pdf",
        mime="application/pdf"
    )
