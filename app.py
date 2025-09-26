import streamlit as st
from docx import Document
import re
import io
from datetime import datetime
import base64

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

def create_base_template():
    """Crea la plantilla base exacta del documento original"""
    doc = Document()
    
    # Eliminar el párrafo por defecto
    doc._body.clear_content()
    
    # Recrear exactamente el contenido del documento original
    
    # Párrafo 1: Certificado N° xxxxxxx -- Seguro de {{completar con el nombre del seguro}}
    p1 = doc.add_paragraph()
    r1 = p1.add_run("Certificado N° xxxxxxx -- Seguro de ")
    r1.italic = True
    r2 = p1.add_run("{{completar con el nombre del seguro}}")
    r2.bold = True
    
    # Párrafo 2: Póliza Nº xxxxx - Código de registro xxxxxxx
    p2 = doc.add_paragraph()
    r2_1 = p2.add_run("Póliza Nº xxxxx - Código de registro xxxxxxx")
    r2_1.italic = True
    
    # Párrafo 3: ¡Hola Xxxxxxxxx!
    doc.add_paragraph("¡Hola Xxxxxxxxx!")
    
    # Párrafo 4: ¡Felicidades! Estás asegurado.
    doc.add_paragraph("¡Felicidades! Estás asegurado.")
    
    # Párrafo 5: Confirmamos que tienes un seguro activo...
    p5 = doc.add_paragraph("Confirmamos que tienes un seguro activo que te protege frente a ")
    r5 = p5.add_run("[completar con el riesgo]")
    r5.bold = True
    
    # Párrafo 6: CONTRATANTE
    p6 = doc.add_paragraph()
    r6 = p6.add_run("CONTRATANTE")
    r6.bold = True
    
    # Párrafo 7: XXXXX, RUC xxxxxxx...
    doc.add_paragraph("XXXXX, RUC xxxxxxx, Dirección xxxxxxxxx")
    
    # Párrafo 8: Distrito xxxxxxx...
    doc.add_paragraph("Distrito xxxxxxx xxxxxxx también llamado sólo \"xxxxx\".")
    
    # Párrafo 9: Vigencia del Seguro
    p9 = doc.add_paragraph()
    r9 = p9.add_run("Vigencia del Seguro: XXXXXXXXXXX")
    r9.bold = True
    
    # Párrafo 10: Inicio de Vigencia
    doc.add_paragraph("Inicio de Vigencia: Desde las XX horas del DD/MM/AAA")
    
    # Párrafo 11: Tu seguro se renovará
    doc.add_paragraph("Tu seguro se renovará automáticamente.")
    
    # Párrafo 12: Información de Contacto
    p12 = doc.add_paragraph()
    r12 = p12.add_run("Información de Contacto de Pacífico Seguros")
    r12.bold = True
    
    # Párrafos de contacto
    doc.add_paragraph("Pacífico Compañía de Seguros y Reaseguros S.A.")
    doc.add_paragraph("RUC N 20332970411 Av. Juan de Arona 830, San Isidro")
    doc.add_paragraph("Teléf.: XXX-XXXX / WhatsApp: +51 XXX-XXXX")
    doc.add_paragraph("Pág. Web.: https://www.pacifico.com.pe/")
    
    # Mensaje importante en negrita
    p_msg = doc.add_paragraph()
    r_msg = p_msg.add_run("Si tienes alguna duda sobre tu cobertura o cómo usar tu seguro, contáctanos al número de teléfono indicado o escríbenos por WhatsApp.")
    r_msg.bold = True
    
    # [Índice]
    doc.add_paragraph("[Índice]")
    
    # ¿Quién es el ASEGURADO?
    p_aseg = doc.add_paragraph()
    r_aseg = p_aseg.add_run("¿Quién es el ASEGURADO?")
    r_aseg.bold = True
    
    # Datos del asegurado
    doc.add_paragraph("[Nombre y Apellidos del Asegurado]")
    doc.add_paragraph("¡Tú estás asegurado!")
    doc.add_paragraph("[Tipo Doc]")
    doc.add_paragraph("[Número Doc]")
    doc.add_paragraph("[Domicilio]")
    doc.add_paragraph("[Correo]")
    doc.add_paragraph("[Teléfono]")
    
    # Domicilio contractual
    p_dom = doc.add_paragraph()
    r_dom = p_dom.add_run("Tu domicilio contractual será el correo electrónico que brindaste en la Solicitud de Seguro. Si no lo hiciste, será la dirección física ingresada en los sistemas del [completar con la info del canal. Por ejemplo, para PT es el \"Banco\"].")
    r_dom.bold = True
    
    # Relación
    doc.add_paragraph("Relación del ASEGURADO con el CONTRATANTE: XXXXXXX")
    
    # Datos del Beneficiario
    p_benef = doc.add_paragraph()
    r_benef = p_benef.add_run("Datos del Beneficiario (sólo en caso sea distinto del Asegurado):")
    r_benef.bold = True
    
    doc.add_paragraph("Tipo de Documento: N°:")
    doc.add_paragraph("Apellido Paterno: Apellido Materno:")
    doc.add_paragraph("Nombres: Fecha de nacimiento:")
    doc.add_paragraph("Correo electrónico: Teléfono:")
    
    # Tu domicilio contractual (segunda vez)
    p_dom2 = doc.add_paragraph()
    r_dom2 = p_dom2.add_run("Tu domicilio contractual será el correo electrónico que brindaste en la Solicitud de Seguro.")
    r_dom2.bold = True
    
    # ¿En qué situaciones te cubre tu seguro?
    p_cubre = doc.add_paragraph()
    r_cubre = p_cubre.add_run("¿En qué situaciones te cubre tu seguro?")
    r_cubre.bold = True
    
    p_cubre_resp = doc.add_paragraph()
    r_cubre_resp = p_cubre_resp.add_run("[Aquí debes modificar en función a los inputs]")
    r_cubre_resp.bold = True
    
    # ¿En qué situaciones adicionales te cubre tu seguro?
    p_adic = doc.add_paragraph()
    r_adic = p_adic.add_run("¿En qué situaciones adicionales te cubre tu seguro?")
    r_adic.bold = True
    
    p_adic_resp = doc.add_paragraph()
    r_adic_resp = p_adic_resp.add_run("xxxxxxxxxxxxxx")
    r_adic_resp.bold = True
    
    # ¿Qué información importante debes considerar?
    p_info = doc.add_paragraph()
    r_info = p_info.add_run("¿Qué información importante debes considerar?")
    r_info.bold = True
    
    p_info_resp = doc.add_paragraph()
    r_info_resp = p_info_resp.add_run("[Completar con las condiciones de asegurabilidad por ejemplo en el caso de PT]")
    r_info_resp.bold = True
    
    p_tiempo = doc.add_paragraph()
    r_tiempo = p_tiempo.add_run("Según el tipo de evento que te haya ocurrido hay condiciones de tiempo en los cuales tendrás cobertura:")
    r_tiempo.bold = True
    
    # ¿En qué situaciones que NO cubre tu seguro?
    p_no_cubre = doc.add_paragraph()
    r_no_cubre = p_no_cubre.add_run("¿En qué situaciones que NO cubre tu seguro?")
    r_no_cubre.bold = True
    
    p_no_cubre_resp = doc.add_paragraph()
    r_no_cubre_resp = p_no_cubre_resp.add_run("[Aquí debes modificar en función a los inputs]")
    r_no_cubre_resp.bold = True
    
    # ¿Cómo hago uso de la cobertura?
    p_uso = doc.add_paragraph()
    r_uso = p_uso.add_run("¿Cómo hago uso de la cobertura?")
    r_uso.bold = True
    
    p_uso_intro = doc.add_paragraph()
    r_uso_intro = p_uso_intro.add_run("Si sucediera alguna de las situaciones cubiertas por el seguro que describimos anteriormente:")
    r_uso_intro.bold = True
    
    p_uso_resp = doc.add_paragraph()
    r_uso_resp = p_uso_resp.add_run("[Aquí debes modificar en función a los inputs]")
    r_uso_resp.bold = True
    
    # Blockquote: El límite de tiempo...
    p_limite = doc.add_paragraph()
    r_limite = p_limite.add_run("El límite de tiempo que tienes para presentar tus documentos es de 10 años.")
    r_limite.bold = True
    # Simular blockquote con sangría
    p_limite.paragraph_format.left_indent = 720000  # En EMUs (English Metric Units)
    
    # Importante saber:
    p_imp = doc.add_paragraph()
    r_imp = p_imp.add_run("Importante saber:")
    r_imp.bold = True
    
    # Lista de puntos importantes
    doc.add_paragraph("• Una vez que tengamos todos tus documentos, tenemos 30 días para responderte. Si se aprueba, te pagamos en máximo 30 días. Si no respondemos a tiempo, se considera aprobada.")
    doc.add_paragraph("• Si necesitamos más tiempo para revisar tu caso, te lo solicitaremos solo una vez y por el mismo plazo que el inicial. Si no estás de acuerdo, lo solicitaremos a la Superintendencia de Banca y Seguros.")
    doc.add_paragraph("• Si no entregas los documentos o no haces la prueba poligráfica a tiempo, el proceso se detiene y no podremos hacer el pago.")
    doc.add_paragraph("• Incluso después de pagar, podemos revisar el caso. Si no correspondía, podríamos pedirte el reembolso.")
    
    # ¿Cuánto cuesta y cómo se paga el seguro?
    p_costo = doc.add_paragraph()
    r_costo = p_costo.add_run("¿Cuánto cuesta y cómo se paga el seguro?")
    r_costo.bold = True
    
    # Tabla exacta
    table = doc.add_table(rows=5, cols=2)
    table.style = 'Table Grid'
    
    # Fila 1: Moneda
    cell_1_1 = table.cell(0, 0)
    p_cell_1_1 = cell_1_1.paragraphs[0]
    r_cell_1_1 = p_cell_1_1.add_run("Moneda")
    r_cell_1_1.bold = True
    
    cell_1_2 = table.cell(0, 1)
    p_cell_1_2 = cell_1_2.paragraphs[0]
    r_cell_1_2 = p_cell_1_2.add_run("xxxxxxx")
    r_cell_1_2.bold = True
    
    # Fila 2: Costo Total del Seguro
    cell_2_1 = table.cell(1, 0)
    p_cell_2_1 = cell_2_1.paragraphs[0]
    r_cell_2_1 = p_cell_2_1.add_run("Costo Total del Seguro")
    r_cell_2_1.bold = True
    
    cell_2_2 = table.cell(1, 1)
    p_cell_2_2 = cell_2_2.paragraphs[0]
    r_cell_2_2 = p_cell_2_2.add_run("xxxx")
    r_cell_2_2.bold = True
    
    # Fila 3: IGV
    cell_3_1 = table.cell(2, 0)
    p_cell_3_1 = cell_3_1.paragraphs[0]
    r_cell_3_1 = p_cell_3_1.add_run("IGV")
    r_cell_3_1.bold = True
    
    cell_3_2 = table.cell(2, 1)
    p_cell_3_2 = cell_3_2.paragraphs[0]
    r_cell_3_2 = p_cell_3_2.add_run("xxxx")
    r_cell_3_2.bold = True
    
    # Fila 4: Frecuencia
    cell_4_1 = table.cell(3, 0)
    p_cell_4_1 = cell_4_1.paragraphs[0]
    r_cell_4_1 = p_cell_4_1.add_run("Frecuencia")
    r_cell_4_1.bold = True
    
    cell_4_2 = table.cell(3, 1)
    p_cell_4_2 = cell_4_2.paragraphs[0]
    r_cell_4_2 = p_cell_4_2.add_run("xxxx")
    r_cell_4_2.bold = True
    
    # Fila 5: ¿Cómo te cobramos el seguro?
    cell_5_1 = table.cell(4, 0)
    p_cell_5_1 = cell_5_1.paragraphs[0]
    r_cell_5_1 = p_cell_5_1.add_run("¿Cómo te cobramos el seguro?")
    r_cell_5_1.bold = True
    
    cell_5_2 = table.cell(4, 1)
    p_cell_5_2 = cell_5_2.paragraphs[0]
    r_cell_5_2 = p_cell_5_2.add_run("[completar la información del medio de cobro]")
    r_cell_5_2.bold = True
    
    # El costo total del seguro incluye x% de comisión
    p_comision = doc.add_paragraph()
    r_comision = p_comision.add_run("El costo total del seguro incluye x% de comisión del [completar con la información del canal].")
    r_comision.bold = True
    
    # ¿Cuánto dura tu seguro?
    p_duracion = doc.add_paragraph()
    r_duracion = p_duracion.add_run("¿Cuánto dura tu seguro?")
    r_duracion.bold = True
    
    doc.add_paragraph("• Tu seguro puede durar un mes o un año, según el plan que elegiste.")
    doc.add_paragraph("• Se renueva automáticamente cuando termina, salvo que tú o nosotros avisemos con 30 días de anticipación.")
    doc.add_paragraph("• En cada renovación, el pago del seguro será igual al del contrato original, a menos que se acuerde algo distinto por escrito.")
    
    # ¿Cuándo empieza y cuándo termina?
    p_cuando = doc.add_paragraph()
    r_cuando = p_cuando.add_run("¿Cuándo empieza y cuándo termina?")
    r_cuando.bold = True
    
    # Inicio:
    p_inicio = doc.add_paragraph()
    r_inicio = p_inicio.add_run("Inicio: Tu seguro empieza desde que lo contratas, si:")
    r_inicio.bold = True
    
    # Lista de inicio
    p_req1 = doc.add_paragraph("• ")
    r_req1 = p_req1.add_run("[Completar con los requisitos propios del producto para empiece la vigencia.Por ejemplo para el caso de PT empieza si la tarjeta está activa].")
    r_req1.bold = True
    
    doc.add_paragraph("• Firmaste la solicitud.")
    doc.add_paragraph("• Brindaste información correcta y completa.")
    
    # Fin:
    p_fin = doc.add_paragraph()
    r_fin = p_fin.add_run("Fin: Tu seguro terminará si ocurre alguna de estas situaciones:")
    r_fin.bold = True
    
    doc.add_paragraph("• No pagas en los 90 días siguientes a la fecha límite.")
    
    p_req2 = doc.add_paragraph("• ")
    r_req2 = p_req2.add_run("[Completar con los requisitos propios del producto para empiece la vigencia.Por ejemplo para el caso de PT: \"Se cancela o vence tu tarjeta, y no la renuevas\"].")
    r_req2.bold = True
    
    doc.add_paragraph("• Fallece el asegurado.")
    
    # Heading: ¿Puedo arrepentirme de haber contratado el seguro?
    heading = doc.add_heading("¿Puedo arrepentirme de haber contratado el seguro?", level=2)
    for run in heading.runs:
        run.bold = True
    
    doc.add_paragraph("Sí. Si cambias de opinión, puedes cancelar el seguro sin dar una razón y sin penalidades dentro de los 15 días calendario desde que recibiste este Certificado.")
    
    # ¿Cómo hacerlo?
    p_como = doc.add_paragraph()
    r_como = p_como.add_run("¿Cómo hacerlo?")
    r_como.bold = True
    
    doc.add_paragraph("Puedes usar el mismo canal por el que contrataste el seguro (página web, app, etc.), o escribir al área de Atención al Cliente de Pacífico Seguros. La dirección y canales disponibles están detallados en las Condiciones Particulares de tu póliza o en el Certificado de seguro.")
    
    # ¿Y si ya pagaste?
    p_pagaste = doc.add_paragraph()
    r_pagaste = p_pagaste.add_run("¿Y si ya pagaste?")
    r_pagaste.bold = True
    
    doc.add_paragraph("Si ya pagaste el seguro, te devolveremos lo pagado en un máximo de 30 días calendario desde que se reciba tu comunicación.")
    
    # Importante saber
    p_imp_saber = doc.add_paragraph()
    r_imp_saber = p_imp_saber.add_run("Importante saber")
    r_imp_saber.bold = True
    
    p_derecho = doc.add_paragraph()
    r_derecho = p_derecho.add_run("Solo puedes ejercer este derecho si aún no has usado ninguna cobertura ni beneficio del seguro, y si el contrato no ha vencido.")
    r_derecho.bold = True
    
    # Sobre tu certificado de seguro
    p_sobre = doc.add_paragraph()
    r_sobre = p_sobre.add_run("Sobre tu certificado de seguro")
    r_sobre.bold = True
    
    doc.add_paragraph("Te lo enviaremos al correo que nos diste. También puedes verlo en nuestra app Mi Espacio Pacífico o en www.pacifico.com.pe.")
    
    # Otros puntos importantes que debes saber:
    p_otros = doc.add_paragraph()
    r_otros = p_otros.add_run("Otros puntos importantes que debes saber:")
    r_otros.bold = True
    
    doc.add_paragraph("• Cuando envíes comunicaciones o pagos al banco, se considerarán como si fueran enviados directamente a nosotros, para el caso de pagos se considerará la fecha en que lo realizaste.")
    doc.add_paragraph("• Somos los únicos responsables de las coberturas que contrataste y asumimos cualquier error u omisión del banco.")
    doc.add_paragraph("• Todos los términos y condiciones de este seguro se encuentran definidos en las Condiciones Particulares, Condiciones Generales de la Póliza.")
    doc.add_paragraph("• Si necesitas la póliza, puedes pedir una copia a Pacífico Seguros o al Banco. Te la entregaremos en máximo en 15 días calendario desde que la solicitas.")
    
    # Fecha de emisión
    p_fecha = doc.add_paragraph()
    r_fecha = p_fecha.add_run("Fecha de emisión, Lima, xxde xxxx de xxxx")
    r_fecha.bold = True
    
    # Firma
    p_firma = doc.add_paragraph()
    r_firma = p_firma.add_run("Xxxxxxxxxxxxxxxxxxxxxxxxxxx")
    r_firma.bold = True
    
    p_rep = doc.add_paragraph()
    r_rep = p_rep.add_run("Representante Pacífico Seguros")
    r_rep.bold = True
    
    return doc

def replace_insurance_name(doc, nombre_seguro):
    """Reemplaza únicamente el nombre del seguro en el documento"""
    
    # Buscar y reemplazar en todos los párrafos
    for paragraph in doc.paragraphs:
        if "{{completar con el nombre del seguro}}" in paragraph.text:
            # Buscar el run específico que contiene la variable
            for run in paragraph.runs:
                if "{{completar con el nombre del seguro}}" in run.text:
                    run.text = run.text.replace("{{completar con el nombre del seguro}}", nombre_seguro)
                    break
    
    # También buscar en tablas por si acaso
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    if "{{completar con el nombre del seguro}}" in paragraph.text:
                        for run in paragraph.runs:
                            if "{{completar con el nombre del seguro}}" in run.text:
                                run.text = run.text.replace("{{completar con el nombre del seguro}}", nombre_seguro)
                                break
    
    return doc

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🛡️ Generador de Certificados Pacífico Seguros</h1>
        <p>Formato exacto preservado - Solo cambia el nombre del seguro</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Ingresa el tipo de seguro")
    
    # Formulario más claro
    with st.container():
        nombre_seguro = st.text_input(
            "**Tipo de seguro:**",
            placeholder="Ejemplo: Vida, Vehicular, Hogar, Salud, etc.",
            help="Este nombre aparecerá en: 'Certificado N° xxxxxxx -- Seguro de [TU RESPUESTA]'",
            key="seguro_input"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Botón centrado
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
            with st.spinner("Generando certificado con formato original exacto..."):
                try:
                    # Crear plantilla base exacta
                    doc = create_base_template()
                    
                    # Reemplazar solo el nombre del seguro
                    doc = replace_insurance_name(doc, nombre_seguro.strip())
                    
                    # Guardar en memoria
                    doc_buffer = io.BytesIO()
                    doc.save(doc_buffer)
                    doc_buffer.seek(0)
                    
                    # Nombre del archivo
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"Certificado_Pacifico_{nombre_seguro.replace(' ', '_')}_{timestamp}.docx"
                    
                    st.success("✅ Certificado generado preservando formato original")
                    
                    # Información
                    st.info(f"""
                    **Certificado generado:**
                    
                    • **Tipo:** Seguro de {nombre_seguro}
                    • **Formato:** Exacto al original de Pacífico Seguros  
                    • **Cambios:** Solo el nombre del seguro
                    • **Estado:** Listo para editar campos restantes
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
                    **📝 Instrucciones:**
                    
                    El documento mantiene el formato exacto original. Todos los demás campos 
                    (como xxxxxxx, [completar], etc.) aparecen tal como están en la plantilla 
                    para que los edites manualmente según cada caso específico.
                    """)
                    
                except Exception as e:
                    st.error(f"Error al generar el certificado: {str(e)}")
        else:
            st.error("⚠️ Por favor ingresa el tipo de seguro")
    
    # Información adicional
    if not generar:
        st.markdown("---")
        st.markdown("""
        **🎯 Lo que hace esta herramienta:**
        
        • Toma la plantilla exacta de Pacífico Seguros
        • Solo reemplaza "{{completar con el nombre del seguro}}" con tu respuesta  
        • Mantiene TODO el formato original: negritas, cursivas, espaciado, tabla
        • Todos los demás campos quedan como placeholders para edición manual
        
        **📋 Resultado esperado:**
        
        "Certificado N° xxxxxxx -- Seguro de **[TU TIPO DE SEGURO]**"
        
        Todo lo demás permanece exactamente igual al formato original.
        """)

if __name__ == "__main__":
    main()
