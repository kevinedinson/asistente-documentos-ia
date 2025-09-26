import streamlit as st
from docx import Document
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
        border-radius: 8px;
        border: 2px solid #e0e0e0;
        font-size: 18px;
        padding: 15px;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #1e3c72;
        box-shadow: 0 0 0 0.2rem rgba(30, 60, 114, 0.25);
    }
</style>
""", unsafe_allow_html=True)

def create_certificate_document(nombre_seguro):
    """Crea el certificado con el contenido exacto de la plantilla original"""
    
    # Crear documento
    doc = Document()
    
    # Encabezado principal
    heading = doc.add_heading("CERTIFICADO PACÍFICO SEGUROS", 0)
    heading.alignment = 1  # Centrado
    
    # Párrafo 1: Certificado N° xxxxxxx -- Seguro de [NOMBRE]
    p1 = doc.add_paragraph()
    r1 = p1.add_run("Certificado N° xxxxxxx -- Seguro de ")
    r1.italic = True
    r2 = p1.add_run(nombre_seguro)
    r2.bold = True
    
    # Párrafo 2: Póliza Nº xxxxx - Código de registro xxxxxxx
    p2 = doc.add_paragraph()
    r2_1 = p2.add_run("Póliza Nº xxxxx - Código de registro xxxxxxx")
    r2_1.italic = True
    
    # Agregar línea vacía
    doc.add_paragraph()
    
    # Saludo
    doc.add_paragraph("¡Hola Xxxxxxxxx!")
    doc.add_paragraph()
    doc.add_paragraph("¡Felicidades! Estás asegurado.")
    doc.add_paragraph()
    
    # Confirmación
    p_conf = doc.add_paragraph("Confirmamos que tienes un seguro activo que te protege frente a ")
    r_conf = p_conf.add_run("[completar con el riesgo]")
    r_conf.bold = True
    
    doc.add_paragraph()
    
    # CONTRATANTE
    p_cont = doc.add_paragraph()
    r_cont = p_cont.add_run("CONTRATANTE")
    r_cont.bold = True
    
    doc.add_paragraph()
    doc.add_paragraph("XXXXX, RUC xxxxxxx, Dirección xxxxxxxxx")
    doc.add_paragraph()
    doc.add_paragraph('Distrito xxxxxxx xxxxxxx también llamado sólo "xxxxx".')
    doc.add_paragraph()
    
    # Vigencia
    p_vig = doc.add_paragraph()
    r_vig = p_vig.add_run("Vigencia del Seguro: XXXXXXXXXXX")
    r_vig.bold = True
    
    doc.add_paragraph()
    doc.add_paragraph("Inicio de Vigencia: Desde las XX horas del DD/MM/AAA")
    doc.add_paragraph()
    doc.add_paragraph("Tu seguro se renovará automáticamente.")
    doc.add_paragraph()
    
    # Información de contacto
    p_info = doc.add_paragraph()
    r_info = p_info.add_run("Información de Contacto de Pacífico Seguros")
    r_info.bold = True
    
    doc.add_paragraph()
    doc.add_paragraph("Pacífico Compañía de Seguros y Reaseguros S.A.")
    doc.add_paragraph("RUC N 20332970411 Av. Juan de Arona 830, San Isidro")
    doc.add_paragraph("Teléf.: XXX-XXXX / WhatsApp: +51 XXX-XXXX")
    doc.add_paragraph("Pág. Web.: https://www.pacifico.com.pe/")
    doc.add_paragraph()
    
    # Mensaje importante
    p_msg = doc.add_paragraph()
    r_msg = p_msg.add_run("Si tienes alguna duda sobre tu cobertura o cómo usar tu seguro, contáctanos al número de teléfono indicado o escríbenos por WhatsApp.")
    r_msg.bold = True
    
    doc.add_paragraph()
    doc.add_paragraph("[Índice]")
    doc.add_paragraph()
    
    # Datos del asegurado
    p_aseg = doc.add_paragraph()
    r_aseg = p_aseg.add_run("¿Quién es el ASEGURADO?")
    r_aseg.bold = True
    
    doc.add_paragraph()
    doc.add_paragraph("[Nombre y Apellidos del Asegurado]")
    doc.add_paragraph()
    doc.add_paragraph("¡Tú estás asegurado!")
    doc.add_paragraph()
    doc.add_paragraph("[Tipo Doc]")
    doc.add_paragraph()
    doc.add_paragraph("[Número Doc]")
    doc.add_paragraph()
    doc.add_paragraph("[Domicilio]")
    doc.add_paragraph()
    doc.add_paragraph("[Correo]")
    doc.add_paragraph()
    doc.add_paragraph("[Teléfono]")
    doc.add_paragraph()
    
    # Domicilio contractual
    p_dom = doc.add_paragraph()
    r_dom = p_dom.add_run('Tu domicilio contractual será el correo electrónico que brindaste en la Solicitud de Seguro. Si no lo hiciste, será la dirección física ingresada en los sistemas del [completar con la info del canal. Por ejemplo, para PT es el "Banco"].')
    r_dom.bold = True
    
    doc.add_paragraph()
    doc.add_paragraph("Relación del ASEGURADO con el CONTRATANTE: XXXXXXX")
    doc.add_paragraph()
    
    # Beneficiario
    p_benef = doc.add_paragraph()
    r_benef = p_benef.add_run("Datos del Beneficiario (sólo en caso sea distinto del Asegurado):")
    r_benef.bold = True
    
    doc.add_paragraph()
    doc.add_paragraph("Tipo de Documento: N°:")
    doc.add_paragraph()
    doc.add_paragraph("Apellido Paterno: Apellido Materno:")
    doc.add_paragraph()
    doc.add_paragraph("Nombres: Fecha de nacimiento:")
    doc.add_paragraph()
    doc.add_paragraph("Correo electrónico: Teléfono:")
    doc.add_paragraph()
    
    # Segunda mención de domicilio
    p_dom2 = doc.add_paragraph()
    r_dom2 = p_dom2.add_run("Tu domicilio contractual será el correo electrónico que brindaste en la Solicitud de Seguro.")
    r_dom2.bold = True
    
    doc.add_paragraph()
    
    # Coberturas
    p_cob1 = doc.add_paragraph()
    r_cob1 = p_cob1.add_run("¿En qué situaciones te cubre tu seguro?")
    r_cob1.bold = True
    
    doc.add_paragraph()
    
    p_cob1_resp = doc.add_paragraph()
    r_cob1_resp = p_cob1_resp.add_run("[Aquí debes modificar en función a los inputs]")
    r_cob1_resp.bold = True
    
    doc.add_paragraph()
    
    p_cob2 = doc.add_paragraph()
    r_cob2 = p_cob2.add_run("¿En qué situaciones adicionales te cubre tu seguro?")
    r_cob2.bold = True
    
    doc.add_paragraph()
    
    p_cob2_resp = doc.add_paragraph()
    r_cob2_resp = p_cob2_resp.add_run("xxxxxxxxxxxxxx")
    r_cob2_resp.bold = True
    
    doc.add_paragraph()
    
    # Información importante
    p_info_imp = doc.add_paragraph()
    r_info_imp = p_info_imp.add_run("¿Qué información importante debes considerar?")
    r_info_imp.bold = True
    
    doc.add_paragraph()
    
    p_info_resp = doc.add_paragraph()
    r_info_resp = p_info_resp.add_run("[Completar con las condiciones de asegurabilidad por ejemplo en el caso de PT]")
    r_info_resp.bold = True
    
    doc.add_paragraph()
    
    p_tiempo = doc.add_paragraph()
    r_tiempo = p_tiempo.add_run("Según el tipo de evento que te haya ocurrido hay condiciones de tiempo en los cuales tendrás cobertura:")
    r_tiempo.bold = True
    
    doc.add_paragraph()
    
    # Exclusiones
    p_excl = doc.add_paragraph()
    r_excl = p_excl.add_run("¿En qué situaciones que NO cubre tu seguro?")
    r_excl.bold = True
    
    doc.add_paragraph()
    
    p_excl_resp = doc.add_paragraph()
    r_excl_resp = p_excl_resp.add_run("[Aquí debes modificar en función a los inputs]")
    r_excl_resp.bold = True
    
    doc.add_paragraph()
    
    # Uso de cobertura
    p_uso = doc.add_paragraph()
    r_uso = p_uso.add_run("¿Cómo hago uso de la cobertura?")
    r_uso.bold = True
    
    doc.add_paragraph()
    
    p_uso_intro = doc.add_paragraph()
    r_uso_intro = p_uso_intro.add_run("Si sucediera alguna de las situaciones cubiertas por el seguro que describimos anteriormente:")
    r_uso_intro.bold = True
    
    doc.add_paragraph()
    
    p_uso_resp = doc.add_paragraph()
    r_uso_resp = p_uso_resp.add_run("[Aquí debes modificar en función a los inputs]")
    r_uso_resp.bold = True
    
    doc.add_paragraph()
    
    # Límite de tiempo
    p_limite = doc.add_paragraph()
    r_limite = p_limite.add_run("El límite de tiempo que tienes para presentar tus documentos es de 10 años.")
    r_limite.bold = True
    
    doc.add_paragraph()
    
    # Importante saber
    p_imp_saber = doc.add_paragraph()
    r_imp_saber = p_imp_saber.add_run("Importante saber:")
    r_imp_saber.bold = True
    
    doc.add_paragraph()
    doc.add_paragraph("• Una vez que tengamos todos tus documentos, tenemos 30 días para responderte. Si se aprueba, te pagamos en máximo 30 días. Si no respondemos a tiempo, se considera aprobada.")
    doc.add_paragraph("• Si necesitamos más tiempo para revisar tu caso, te lo solicitaremos solo una vez y por el mismo plazo que el inicial. Si no estás de acuerdo, lo solicitaremos a la Superintendencia de Banca y Seguros.")
    doc.add_paragraph("• Si no entregas los documentos o no haces la prueba poligráfica a tiempo, el proceso se detiene y no podremos hacer el pago.")
    doc.add_paragraph("• Incluso después de pagar, podemos revisar el caso. Si no correspondía, podríamos pedirte el reembolso.")
    doc.add_paragraph()
    
    # Costos
    p_costo = doc.add_paragraph()
    r_costo = p_costo.add_run("¿Cuánto cuesta y cómo se paga el seguro?")
    r_costo.bold = True
    
    doc.add_paragraph()
    
    # Tabla de costos
    table = doc.add_table(rows=5, cols=2)
    table.style = 'Table Grid'
    
    # Llenar tabla con contenido en negrita
    cells_content = [
        ["Moneda", "xxxxxxx"],
        ["Costo Total del Seguro", "xxxx"],
        ["IGV", "xxxx"],
        ["Frecuencia", "xxxx"],
        ["¿Cómo te cobramos el seguro?", "[completar la información del medio de cobro]"]
    ]
    
    for i, (col1_text, col2_text) in enumerate(cells_content):
        cell1 = table.cell(i, 0)
        cell2 = table.cell(i, 1)
        
        # Limpiar párrafos existentes
        cell1.text = ""
        cell2.text = ""
        
        # Agregar texto en negrita
        p1 = cell1.paragraphs[0]
        r1 = p1.add_run(col1_text)
        r1.bold = True
        
        p2 = cell2.paragraphs[0]
        r2 = p2.add_run(col2_text)
        r2.bold = True
    
    doc.add_paragraph()
    
    p_comision = doc.add_paragraph()
    r_comision = p_comision.add_run("El costo total del seguro incluye x% de comisión del [completar con la información del canal].")
    r_comision.bold = True
    
    doc.add_paragraph()
    
    # Duración
    p_duracion = doc.add_paragraph()
    r_duracion = p_duracion.add_run("¿Cuánto dura tu seguro?")
    r_duracion.bold = True
    
    doc.add_paragraph()
    doc.add_paragraph("• Tu seguro puede durar un mes o un año, según el plan que elegiste.")
    doc.add_paragraph("• Se renueva automáticamente cuando termina, salvo que tú o nosotros avisemos con 30 días de anticipación.")
    doc.add_paragraph("• En cada renovación, el pago del seguro será igual al del contrato original, a menos que se acuerde algo distinto por escrito.")
    doc.add_paragraph()
    
    # Inicio y fin
    p_cuando = doc.add_paragraph()
    r_cuando = p_cuando.add_run("¿Cuándo empieza y cuándo termina?")
    r_cuando.bold = True
    
    doc.add_paragraph()
    
    p_inicio = doc.add_paragraph()
    r_inicio = p_inicio.add_run("Inicio: Tu seguro empieza desde que lo contratas, si:")
    r_inicio.bold = True
    
    doc.add_paragraph()
    
    p_req1 = doc.add_paragraph("• ")
    r_req1 = p_req1.add_run("[Completar con los requisitos propios del producto para empiece la vigencia.Por ejemplo para el caso de PT empieza si la tarjeta está activa].")
    r_req1.bold = True
    
    doc.add_paragraph("• Firmaste la solicitud.")
    doc.add_paragraph("• Brindaste información correcta y completa.")
    doc.add_paragraph()
    
    p_fin = doc.add_paragraph()
    r_fin = p_fin.add_run("Fin: Tu seguro terminará si ocurre alguna de estas situaciones:")
    r_fin.bold = True
    
    doc.add_paragraph()
    doc.add_paragraph("• No pagas en los 90 días siguientes a la fecha límite.")
    
    p_req2 = doc.add_paragraph("• ")
    r_req2 = p_req2.add_run('[Completar con los requisitos propios del producto para empiece la vigencia.Por ejemplo para el caso de PT: "Se cancela o vence tu tarjeta, y no la renuevas"].')
    r_req2.bold = True
    
    doc.add_paragraph("• Fallece el asegurado.")
    doc.add_paragraph()
    
    # Arrepentimiento - usar heading nivel 2
    heading_arrep = doc.add_heading("¿Puedo arrepentirme de haber contratado el seguro?", level=2)
    for run in heading_arrep.runs:
        run.bold = True
    
    doc.add_paragraph()
    doc.add_paragraph("Sí. Si cambias de opinión, puedes cancelar el seguro sin dar una razón y sin penalidades dentro de los 15 días calendario desde que recibiste este Certificado.")
    doc.add_paragraph()
    
    p_como = doc.add_paragraph()
    r_como = p_como.add_run("¿Cómo hacerlo?")
    r_como.bold = True
    
    doc.add_paragraph()
    doc.add_paragraph("Puedes usar el mismo canal por el que contrataste el seguro (página web, app, etc.), o escribir al área de Atención al Cliente de Pacífico Seguros. La dirección y canales disponibles están detallados en las Condiciones Particulares de tu póliza o en el Certificado de seguro.")
    doc.add_paragraph()
    
    p_pagaste = doc.add_paragraph()
    r_pagaste = p_pagaste.add_run("¿Y si ya pagaste?")
    r_pagaste.bold = True
    
    doc.add_paragraph()
    doc.add_paragraph("Si ya pagaste el seguro, te devolveremos lo pagado en un máximo de 30 días calendario desde que se reciba tu comunicación.")
    doc.add_paragraph()
    
    p_imp_saber2 = doc.add_paragraph()
    r_imp_saber2 = p_imp_saber2.add_run("Importante saber")
    r_imp_saber2.bold = True
    
    doc.add_paragraph()
    
    p_derecho = doc.add_paragraph()
    r_derecho = p_derecho.add_run("Solo puedes ejercer este derecho si aún no has usado ninguna cobertura ni beneficio del seguro, y si el contrato no ha vencido.")
    r_derecho.bold = True
    
    doc.add_paragraph()
    
    # Sobre certificado
    p_sobre = doc.add_paragraph()
    r_sobre = p_sobre.add_run("Sobre tu certificado de seguro")
    r_sobre.bold = True
    
    doc.add_paragraph()
    doc.add_paragraph("Te lo enviaremos al correo que nos diste. También puedes verlo en nuestra app Mi Espacio Pacífico o en www.pacifico.com.pe.")
    doc.add_paragraph()
    
    # Otros puntos
    p_otros = doc.add_paragraph()
    r_otros = p_otros.add_run("Otros puntos importantes que debes saber:")
    r_otros.bold = True
    
    doc.add_paragraph()
    doc.add_paragraph("• Cuando envíes comunicaciones o pagos al banco, se considerarán como si fueran enviados directamente a nosotros, para el caso de pagos se considerará la fecha en que lo realizaste.")
    doc.add_paragraph("• Somos los únicos responsables de las coberturas que contrataste y asumimos cualquier error u omisión del banco.")
    doc.add_paragraph("• Todos los términos y condiciones de este seguro se encuentran definidos en las Condiciones Particulares, Condiciones Generales de la Póliza.")
    doc.add_paragraph("• Si necesitas la póliza, puedes pedir una copia a Pacífico Seguros o al Banco. Te la entregaremos en máximo en 15 días calendario desde que la solicitas.")
    doc.add_paragraph()
    
    # Fecha y firma
    p_fecha = doc.add_paragraph()
    r_fecha = p_fecha.add_run("Fecha de emisión, Lima, xxde xxxx de xxxx")
    r_fecha.bold = True
    
    doc.add_paragraph()
    
    p_firma = doc.add_paragraph()
    r_firma = p_firma.add_run("Xxxxxxxxxxxxxxxxxxxxxxxxxxx")
    r_firma.bold = True
    
    doc.add_paragraph()
    
    p_rep = doc.add_paragraph()
    r_rep = p_rep.add_run("Representante Pacífico Seguros")
    r_rep.bold = True
    
    return doc

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🛡️ Generador de Certificados Pacífico Seguros</h1>
        <p>Genera certificados con el contenido exacto de la plantilla original</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Ingresa el tipo de seguro")
    
    # Formulario
    nombre_seguro = st.text_input(
        "**Tipo de seguro:**",
        placeholder="Ejemplo: Vida, Vehicular, Hogar, Salud",
        help="Este será el único campo que se personalizará en el certificado"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
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
            with st.spinner("Generando certificado..."):
                try:
                    # Crear documento
                    doc = create_certificate_document(nombre_seguro.strip())
                    
                    # Guardar en memoria
                    doc_buffer = io.BytesIO()
                    doc.save(doc_buffer)
                    doc_buffer.seek(0)
                    
                    # Nombre del archivo
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"Certificado_Pacifico_{nombre_seguro.replace(' ', '_')}_{timestamp}.docx"
                    
                    st.success("✅ Certificado generado exitosamente")
                    
                    # Información
                    st.info(f"""
                    **Certificado generado:**
                    
                    • **Tipo:** Seguro de {nombre_seguro}
                    • **Contenido:** Idéntico a plantilla Pacífico Seguros  
                    • **Estado:** Listo para usar
                    """)
                    
                    # Descarga
                    st.download_button(
                        label="⬇️ DESCARGAR CERTIFICADO",
                        data=doc_buffer.getvalue(),
                        file_name=filename,
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                        use_container_width=True
                    )
                    
                except Exception as e:
                    st.error(f"Error al generar el certificado: {str(e)}")
        else:
            st.error("⚠️ Por favor ingresa el tipo de seguro")
    
    # Información adicional
    if not generar:
        st.markdown("---")
        st.markdown("""
        **Esta herramienta genera certificados con:**
        
        • Contenido idéntico a tu plantilla original de Pacífico Seguros
        • Solo personaliza el nombre del seguro donde corresponde  
        • Mantiene todos los textos, negritas y estructura
        • Formato funcional compatible con Word
        • Fácil edición posterior de campos específicos
        """)

if __name__ == "__main__":
    main()
