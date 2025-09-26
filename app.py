import streamlit as st
from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.shared import OxmlElement, qn
import re
import io
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="Generador de Certificados Pacífico Seguros",
    page_icon="🛡️",
    layout="centered"
)

# CSS personalizado
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .main-header {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .stTextInput > div > div > input {
        border-radius: 5px;
        border: 2px solid #e0e0e0;
        font-size: 18px;
        padding: 12px;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #1e3c72;
        box-shadow: 0 0 0 0.2rem rgba(30, 60, 114, 0.25);
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        border: none;
        border-radius: 5px;
        padding: 12px 24px;
        font-size: 16px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

def create_exact_certificate(nombre_seguro):
    """Crea el certificado exacto preservando el formato original"""
    
    # Crear documento
    doc = Document()
    
    # Configurar márgenes
    section = doc.sections[0]
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    
    # Línea 1: Certificado N° xxxxxxx -- Seguro de [NOMBRE]
    p1 = doc.add_paragraph()
    r1 = p1.add_run("Certificado N° xxxxxxx -- Seguro de ")
    r1.italic = True
    r2 = p1.add_run(nombre_seguro)
    r2.bold = True
    
    # Línea 2: Póliza Nº xxxxx - Código de registro xxxxxxx
    p2 = doc.add_paragraph()
    r3 = p2.add_run("Póliza Nº xxxxx - Código de registro xxxxxxx")
    r3.italic = True
    
    # Saludo
    doc.add_paragraph("¡Hola Xxxxxxxxx!")
    doc.add_paragraph("¡Felicidades! Estás asegurado.")
    
    # Confirmación
    p3 = doc.add_paragraph("Confirmamos que tienes un seguro activo que te protege frente a ")
    r4 = p3.add_run("[completar con el riesgo]")
    r4.bold = True
    
    # CONTRATANTE
    p4 = doc.add_paragraph()
    r5 = p4.add_run("CONTRATANTE")
    r5.bold = True
    
    doc.add_paragraph("XXXXX, RUC xxxxxxx, Dirección xxxxxxxxx")
    doc.add_paragraph("Distrito xxxxxxx xxxxxxx también llamado sólo \"xxxxx\".")
    
    # Vigencia del Seguro
    p5 = doc.add_paragraph()
    r6 = p5.add_run("Vigencia del Seguro: XXXXXXXXXXX")
    r6.bold = True
    
    doc.add_paragraph("Inicio de Vigencia: Desde las XX horas del DD/MM/AAA")
    doc.add_paragraph("Tu seguro se renovará automáticamente.")
    
    # Información de Contacto
    p6 = doc.add_paragraph()
    r7 = p6.add_run("Información de Contacto de Pacífico Seguros")
    r7.bold = True
    
    doc.add_paragraph("Pacífico Compañía de Seguros y Reaseguros S.A.")
    doc.add_paragraph("RUC N 20332970411 Av. Juan de Arona 830, San Isidro")
    doc.add_paragraph("Teléf.: XXX-XXXX / WhatsApp: +51 XXX-XXXX")
    doc.add_paragraph("Pág. Web.: https://www.pacifico.com.pe/")
    
    # Mensaje importante
    p7 = doc.add_paragraph()
    r8 = p7.add_run("Si tienes alguna duda sobre tu cobertura o cómo usar tu seguro, contáctanos al número de teléfono indicado o escríbenos por WhatsApp.")
    r8.bold = True
    
    # [Índice]
    doc.add_paragraph("[Índice]")
    
    # ¿Quién es el ASEGURADO?
    p8 = doc.add_paragraph()
    r9 = p8.add_run("¿Quién es el ASEGURADO?")
    r9.bold = True
    
    doc.add_paragraph("[Nombre y Apellidos del Asegurado]")
    doc.add_paragraph("¡Tú estás asegurado!")
    doc.add_paragraph("[Tipo Doc]")
    doc.add_paragraph("[Número Doc]")
    doc.add_paragraph("[Domicilio]")
    doc.add_paragraph("[Correo]")
    doc.add_paragraph("[Teléfono]")
    
    # Tu domicilio contractual
    p9 = doc.add_paragraph()
    r10 = p9.add_run("Tu domicilio contractual será el correo electrónico que brindaste en la Solicitud de Seguro. Si no lo hiciste, será la dirección física ingresada en los sistemas del [completar con la info del canal. Por ejemplo, para PT es el \"Banco\"].")
    r10.bold = True
    
    doc.add_paragraph("Relación del ASEGURADO con el CONTRATANTE: XXXXXXX")
    
    # Datos del Beneficiario
    p10 = doc.add_paragraph()
    r11 = p10.add_run("Datos del Beneficiario (sólo en caso sea distinto del Asegurado):")
    r11.bold = True
    
    doc.add_paragraph("Tipo de Documento: N°:")
    doc.add_paragraph("Apellido Paterno: Apellido Materno:")
    doc.add_paragraph("Nombres: Fecha de nacimiento:")
    doc.add_paragraph("Correo electrónico: Teléfono:")
    
    # Tu domicilio contractual (repetido)
    p11 = doc.add_paragraph()
    r12 = p11.add_run("Tu domicilio contractual será el correo electrónico que brindaste en la Solicitud de Seguro.")
    r12.bold = True
    
    # ¿En qué situaciones te cubre tu seguro?
    p12 = doc.add_paragraph()
    r13 = p12.add_run("¿En qué situaciones te cubre tu seguro?")
    r13.bold = True
    
    p13 = doc.add_paragraph()
    r14 = p13.add_run("[Aquí debes modificar en función a los inputs]")
    r14.bold = True
    
    # ¿En qué situaciones adicionales te cubre tu seguro?
    p14 = doc.add_paragraph()
    r15 = p14.add_run("¿En qué situaciones adicionales te cubre tu seguro?")
    r15.bold = True
    
    p15 = doc.add_paragraph()
    r16 = p15.add_run("xxxxxxxxxxxxxx")
    r16.bold = True
    
    # ¿Qué información importante debes considerar?
    p16 = doc.add_paragraph()
    r17 = p16.add_run("¿Qué información importante debes considerar?")
    r17.bold = True
    
    p17 = doc.add_paragraph()
    r18 = p17.add_run("[Completar con las condiciones de asegurabilidad por ejemplo en el caso de PT]")
    r18.bold = True
    
    p18 = doc.add_paragraph()
    r19 = p18.add_run("Según el tipo de evento que te haya ocurrido hay condiciones de tiempo en los cuales tendrás cobertura:")
    r19.bold = True
    
    # ¿En qué situaciones que NO cubre tu seguro?
    p19 = doc.add_paragraph()
    r20 = p19.add_run("¿En qué situaciones que NO cubre tu seguro?")
    r20.bold = True
    
    p20 = doc.add_paragraph()
    r21 = p20.add_run("[Aquí debes modificar en función a los inputs]")
    r21.bold = True
    
    # ¿Cómo hago uso de la cobertura?
    p21 = doc.add_paragraph()
    r22 = p21.add_run("¿Cómo hago uso de la cobertura?")
    r22.bold = True
    
    p22 = doc.add_paragraph()
    r23 = p22.add_run("Si sucediera alguna de las situaciones cubiertas por el seguro que describimos anteriormente:")
    r23.bold = True
    
    p23 = doc.add_paragraph()
    r24 = p23.add_run("[Aquí debes modificar en función a los inputs]")
    r24.bold = True
    
    # Cita con sangría (blockquote)
    p24 = doc.add_paragraph()
    r25 = p24.add_run("El límite de tiempo que tienes para presentar tus documentos es de 10 años.")
    r25.bold = True
    p24.paragraph_format.left_indent = Inches(0.5)
    
    # Importante saber:
    p25 = doc.add_paragraph()
    r26 = p25.add_run("Importante saber:")
    r26.bold = True
    
    doc.add_paragraph("• Una vez que tengamos todos tus documentos, tenemos 30 días para responderte. Si se aprueba, te pagamos en máximo 30 días. Si no respondemos a tiempo, se considera aprobada.")
    doc.add_paragraph("• Si necesitamos más tiempo para revisar tu caso, te lo solicitaremos solo una vez y por el mismo plazo que el inicial. Si no estás de acuerdo, lo solicitaremos a la Superintendencia de Banca y Seguros.")
    doc.add_paragraph("• Si no entregas los documentos o no haces la prueba poligráfica a tiempo, el proceso se detiene y no podremos hacer el pago.")
    doc.add_paragraph("• Incluso después de pagar, podemos revisar el caso. Si no correspondía, podríamos pedirte el reembolso.")
    
    # ¿Cuánto cuesta y cómo se paga el seguro?
    p26 = doc.add_paragraph()
    r27 = p26.add_run("¿Cuánto cuesta y cómo se paga el seguro?")
    r27.bold = True
    
    # Tabla
    table = doc.add_table(rows=4, cols=2)
    table.style = 'Table Grid'
    
    # Fila 1
    row1_cells = table.rows[0].cells
    p_cell1 = row1_cells[0].paragraphs[0]
    r_cell1 = p_cell1.add_run("Moneda")
    r_cell1.bold = True
    p_cell2 = row1_cells[1].paragraphs[0]
    r_cell2 = p_cell2.add_run("xxxxxxx")
    r_cell2.bold = True
    
    # Fila 2
    row2_cells = table.rows[1].cells
    p_cell3 = row2_cells[0].paragraphs[0]
    r_cell3 = p_cell3.add_run("Costo Total del Seguro")
    r_cell3.bold = True
    p_cell4 = row2_cells[1].paragraphs[0]
    r_cell4 = p_cell4.add_run("xxxx")
    r_cell4.bold = True
    
    # Fila 3
    row3_cells = table.rows[2].cells
    p_cell5 = row3_cells[0].paragraphs[0]
    r_cell5 = p_cell5.add_run("IGV")
    r_cell5.bold = True
    p_cell6 = row3_cells[1].paragraphs[0]
    r_cell6 = p_cell6.add_run("xxxx")
    r_cell6.bold = True
    
    # Fila 4
    row4_cells = table.rows[3].cells
    p_cell7 = row4_cells[0].paragraphs[0]
    r_cell7 = p_cell7.add_run("Frecuencia")
    r_cell7.bold = True
    p_cell8 = row4_cells[1].paragraphs[0]
    r_cell8 = p_cell8.add_run("xxxx")
    r_cell8.bold = True
    
    # Fila 5 (añadir fila)
    row5 = table.add_row()
    row5_cells = row5.cells
    p_cell9 = row5_cells[0].paragraphs[0]
    r_cell9 = p_cell9.add_run("¿Cómo te cobramos el seguro?")
    r_cell9.bold = True
    p_cell10 = row5_cells[1].paragraphs[0]
    r_cell10 = p_cell10.add_run("[completar la información del medio de cobro]")
    r_cell10.bold = True
    
    # El costo total del seguro incluye
    p27 = doc.add_paragraph()
    r28 = p27.add_run("El costo total del seguro incluye x% de comisión del [completar con la información del canal].")
    r28.bold = True
    
    # ¿Cuánto dura tu seguro?
    p28 = doc.add_paragraph()
    r29 = p28.add_run("¿Cuánto dura tu seguro?")
    r29.bold = True
    
    doc.add_paragraph("• Tu seguro puede durar un mes o un año, según el plan que elegiste.")
    doc.add_paragraph("• Se renueva automáticamente cuando termina, salvo que tú o nosotros avisemos con 30 días de anticipación.")
    doc.add_paragraph("• En cada renovación, el pago del seguro será igual al del contrato original, a menos que se acuerde algo distinto por escrito.")
    
    # ¿Cuándo empieza y cuándo termina?
    p29 = doc.add_paragraph()
    r30 = p29.add_run("¿Cuándo empieza y cuándo termina?")
    r30.bold = True
    
    p30 = doc.add_paragraph()
    r31 = p30.add_run("Inicio: Tu seguro empieza desde que lo contratas, si:")
    r31.bold = True
    
    p31 = doc.add_paragraph("• ")
    r32 = p31.add_run("[Completar con los requisitos propios del producto para empiece la vigencia.Por ejemplo para el caso de PT empieza si la tarjeta está activa].")
    r32.bold = True
    
    doc.add_paragraph("• Firmaste la solicitud.")
    doc.add_paragraph("• Brindaste información correcta y completa.")
    
    p32 = doc.add_paragraph()
    r33 = p32.add_run("Fin: Tu seguro terminará si ocurre alguna de estas situaciones:")
    r33.bold = True
    
    doc.add_paragraph("• No pagas en los 90 días siguientes a la fecha límite.")
    
    p33 = doc.add_paragraph("• ")
    r34 = p33.add_run("[Completar con los requisitos propios del producto para empiece la vigencia.Por ejemplo para el caso de PT: \"Se cancela o vence tu tarjeta, y no la renuevas\"].")
    r34.bold = True
    
    doc.add_paragraph("• Fallece el asegurado.")
    
    # Título con formato de heading
    heading = doc.add_heading("¿Puedo arrepentirme de haber contratado el seguro?", level=2)
    for run in heading.runs:
        run.bold = True
    
    doc.add_paragraph("Sí. Si cambias de opinión, puedes cancelar el seguro sin dar una razón y sin penalidades dentro de los 15 días calendario desde que recibiste este Certificado.")
    
    # ¿Cómo hacerlo?
    p34 = doc.add_paragraph()
    r35 = p34.add_run("¿Cómo hacerlo?")
    r35.bold = True
    
    doc.add_paragraph("Puedes usar el mismo canal por el que contrataste el seguro (página web, app, etc.), o escribir al área de Atención al Cliente de Pacífico Seguros. La dirección y canales disponibles están detallados en las Condiciones Particulares de tu póliza o en el Certificado de seguro.")
    
    # ¿Y si ya pagaste?
    p35 = doc.add_paragraph()
    r36 = p35.add_run("¿Y si ya pagaste?")
    r36.bold = True
    
    doc.add_paragraph("Si ya pagaste el seguro, te devolveremos lo pagado en un máximo de 30 días calendario desde que se reciba tu comunicación.")
    
    # Importante saber
    p36 = doc.add_paragraph()
    r37 = p36.add_run("Importante saber")
    r37.bold = True
    
    p37 = doc.add_paragraph()
    r38 = p37.add_run("Solo puedes ejercer este derecho si aún no has usado ninguna cobertura ni beneficio del seguro, y si el contrato no ha vencido.")
    r38.bold = True
    
    # Sobre tu certificado de seguro
    p38 = doc.add_paragraph()
    r39 = p38.add_run("Sobre tu certificado de seguro")
    r39.bold = True
    
    doc.add_paragraph("Te lo enviaremos al correo que nos diste. También puedes verlo en nuestra app Mi Espacio Pacífico o en www.pacifico.com.pe.")
    
    # Otros puntos importantes que debes saber:
    p39 = doc.add_paragraph()
    r40 = p39.add_run("Otros puntos importantes que debes saber:")
    r40.bold = True
    
    doc.add_paragraph("• Cuando envíes comunicaciones o pagos al banco, se considerarán como si fueran enviados directamente a nosotros, para el caso de pagos se considerará la fecha en que lo realizaste.")
    doc.add_paragraph("• Somos los únicos responsables de las coberturas que contrataste y asumimos cualquier error u omisión del banco.")
    doc.add_paragraph("• Todos los términos y condiciones de este seguro se encuentran definidos en las Condiciones Particulares, Condiciones Generales de la Póliza.")
    doc.add_paragraph("• Si necesitas la póliza, puedes pedir una copia a Pacífico Seguros o al Banco. Te la entregaremos en máximo en 15 días calendario desde que la solicitas.")
    
    # Fecha de emisión
    p40 = doc.add_paragraph()
    r41 = p40.add_run("Fecha de emisión, Lima, xxde xxxx de xxxx")
    r41.bold = True
    
    # Firma
    p41 = doc.add_paragraph()
    r42 = p41.add_run("Xxxxxxxxxxxxxxxxxxxxxxxxxxx")
    r42.bold = True
    
    p42 = doc.add_paragraph()
    r43 = p42.add_run("Representante Pacífico Seguros")
    r43.bold = True
    
    return doc

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🛡️ Generador de Certificados Pacífico Seguros</h1>
        <p>Genera certificados con el formato exacto original</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Completa la información del seguro")
    
    # Formulario más claro
    with st.container():
        nombre_seguro = st.text_input(
            "**¿Cuál es el tipo de seguro?**",
            placeholder="Ejemplo: Vida, Vehicular, Hogar, Salud, etc.",
            help="Especifica el tipo de seguro para el certificado",
            key="seguro_input"
        )
        
        # Espacio
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Botón más visible
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            generar = st.button(
                "📄 GENERAR CERTIFICADO",
                use_container_width=True,
                type="primary"
            )
    
    # Procesamiento
    if generar:
        if nombre_seguro and nombre_seguro.strip():
            with st.spinner("Generando certificado con formato original..."):
                try:
                    # Generar documento exacto
                    doc = create_exact_certificate(nombre_seguro.strip())
                    
                    # Guardar en memoria
                    doc_buffer = io.BytesIO()
                    doc.save(doc_buffer)
                    doc_buffer.seek(0)
                    
                    # Nombre del archivo
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"Certificado_Pacifico_{nombre_seguro.replace(' ', '_')}_{timestamp}.docx"
                    
                    st.success("✅ Certificado generado con formato original preservado")
                    
                    # Información
                    st.info(f"""
                    **📋 Certificado generado:**
                    • Tipo de seguro: {nombre_seguro}
                    • Formato: Original de Pacífico Seguros
                    • Estado: Listo para personalizar
                    """)
                    
                    # Descarga
                    st.download_button(
                        label="⬇️ DESCARGAR CERTIFICADO",
                        data=doc_buffer.getvalue(),
                        file_name=filename,
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                        use_container_width=True
                    )
                    
                    st.warning("""
                    **📝 Nota:** El documento mantiene el formato exacto original. 
                    Todos los campos aparecen como en la plantilla original para que puedas editarlos manualmente.
                    """)
                    
                except Exception as e:
                    st.error(f"Error al generar el certificado: {str(e)}")
        else:
            st.error("⚠️ Por favor ingresa el tipo de seguro")
    
    # Información adicional
    if not generar:
        st.markdown("---")
        st.markdown("""
        **💡 ¿Cómo funciona?**
        
        1. Escribe el tipo de seguro (Ej: "Vida", "Vehicular", "Hogar")
        2. Haz clic en generar
        3. Descarga el certificado con formato original
        4. Edita el documento Word para personalizar los demás campos
        
        **✅ El documento mantiene:**
        • Formato exacto del original
        • Todas las negritas y cursivas
        • Estructura y espaciado original
        • Solo cambia el nombre del seguro
        """)

if __name__ == "__main__":
    main()
