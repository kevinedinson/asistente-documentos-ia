import streamlit as st
from docx import Document
import re
import io
from datetime import datetime
import random

# ====== CONFIGURACIÓN DE LA PÁGINA ======
st.set_page_config(
    page_title="🤖 Asistente IA para Documentos Word",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ====== CSS PERSONALIZADO ======
st.markdown("""
<style>
    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Estilo del chat */
    .chat-container {
        max-height: 400px;
        overflow-y: auto;
        padding: 1rem;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        background-color: #fafafa;
    }
    
    /* Estilo para las variables encontradas */
    .variable-tag {
        background-color: #e3f2fd;
        padding: 2px 8px;
        border-radius: 4px;
        margin: 2px;
        display: inline-block;
        font-family: monospace;
    }
    
    /* Estilo del progreso */
    .progress-text {
        text-align: center;
        font-weight: bold;
        color: #1976d2;
    }
    
    /* Botones principales */
    .main-button {
        background: linear-gradient(45deg, #1976d2, #42a5f5);
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 8px;
        font-weight: bold;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# ====== CLASE PRINCIPAL DEL ASISTENTE ======
class DocumentAIAssistant:
    def __init__(self):
        self.questions_db = {
            # Preguntas para contratos
            'contrato': {
                'nombre': "¿Cuál es el nombre completo de la persona que firmará el contrato?",
                'empresa': "¿Cuál es el nombre de la empresa?",
                'fecha': "¿Cuál es la fecha del contrato?",
                'monto': "¿Cuál es el monto total del contrato?",
                'servicio': "¿Qué servicio se está contratando?",
                'plazo': "¿Cuál es la duración del contrato?"
            },
            # Preguntas para cartas
            'carta': {
                'destinatario': "¿A quién va dirigida la carta?",
                'fecha': "¿Qué fecha debe aparecer en la carta?",
                'asunto': "¿Cuál es el asunto de la carta?",
                'mensaje': "¿Cuál es el mensaje principal?",
                'remitente': "¿Quién envía la carta?"
            },
            # Preguntas para facturas
            'factura': {
                'numero': "¿Cuál es el número de factura?",
                'cliente': "¿Cuál es el nombre del cliente?",
                'fecha': "¿Cuál es la fecha de emisión?",
                'producto': "¿Qué producto o servicio se factura?",
                'cantidad': "¿Cuántas unidades?",
                'precio': "¿Cuál es el precio total?"
            }
        }
    
    def detect_document_type(self, text):
        """Detecta el tipo de documento automáticamente"""
        text_lower = text.lower()
        
        if any(word in text_lower for word in ['contrato', 'acuerdo', 'convenio', 'términos']):
            return 'contrato', '📄 Contrato Comercial'
        elif any(word in text_lower for word in ['factura', 'invoice', 'cobro', 'total', 'subtotal']):
            return 'factura', '🧾 Factura'
        elif any(word in text_lower for word in ['carta', 'estimado', 'querido', 'saludo']):
            return 'carta', '✉️ Carta'
        elif any(word in text_lower for word in ['propuesta', 'cotización', 'presupuesto']):
            return 'contrato', '💼 Propuesta Comercial'
        elif any(word in text_lower for word in ['certificado', 'diploma', 'reconocimiento']):
            return 'carta', '🏆 Certificado'
        else:
            return 'general', '📋 Documento General'
    
    def generate_smart_question(self, variable, doc_type):
        """Genera preguntas inteligentes basadas en la variable"""
        var_lower = variable.lower()
        
        # Buscar en la base de datos de preguntas
        questions = self.questions_db.get(doc_type, {})
        
        # Detectar tipo de variable
        for key, question in questions.items():
            if key in var_lower:
                return question
        
        # Preguntas genéricas inteligentes
        if any(word in var_lower for word in ['nombre', 'client', 'person']):
            return f"¿Cuál es el nombre completo para '{variable.replace('_', ' ')}'?"
        elif any(word in var_lower for word in ['fecha', 'date']):
            return f"¿Qué fecha necesitas para '{variable.replace('_', ' ')}'?"
        elif any(word in var_lower for word in ['monto', 'precio', 'valor', 'total']):
            return f"¿Cuál es el monto para '{variable.replace('_', ' ')}'?"
        elif any(word in var_lower for word in ['email', 'correo']):
            return "¿Cuál es la dirección de email?"
        elif any(word in var_lower for word in ['telefono', 'phone']):
            return "¿Cuál es el número de teléfono?"
        else:
            return f"Por favor proporciona el valor para '{variable.replace('_', ' ').title()}'"
    
    def get_input_type(self, variable):
        """Determina el tipo de input apropiado"""
        var_lower = variable.lower()
        
        if any(word in var_lower for word in ['fecha', 'date']):
            return 'date'
        elif any(word in var_lower for word in ['monto', 'precio', 'valor', 'total', 'cantidad']):
            return 'number'
        elif any(word in var_lower for word in ['email', 'correo']):
            return 'email'
        else:
            return 'text'
    
    def validate_response(self, response, input_type):
        """Valida las respuestas del usuario"""
        if not response or str(response).strip() == "":
            return False, "Por favor proporciona una respuesta válida"
        
        if input_type == 'email':
            if '@' not in str(response) or '.' not in str(response):
                return False, "Por favor ingresa un email válido (ejemplo@correo.com)"
        
        return True, ""
    
    def generate_confirmation(self, variable, response):
        """Genera confirmaciones variadas"""
        confirmations = [
            f"✅ Perfecto, guardé '{response}'",
            f"📝 Excelente, tengo '{response}' anotado",
            f"👍 Muy bien, '{response}' registrado",
            f"✨ Entendido, '{response}' para {variable.replace('_', ' ')}"
        ]
        return random.choice(confirmations)

# ====== FUNCIÓN PRINCIPAL ======
def main():
    # Inicializar el asistente
    if "assistant" not in st.session_state:
        st.session_state.assistant = DocumentAIAssistant()
        st.session_state.step = "welcome"
        st.session_state.variables = []
        st.session_state.responses = {}
        st.session_state.current_question = 0
        st.session_state.chat_history = []
        st.session_state.document = None
        st.session_state.doc_type = None
        st.session_state.doc_type_display = None
    
    assistant = st.session_state.assistant
    
    # ====== HEADER ======
    st.title("🤖 Asistente IA para Documentos Word")
    st.markdown("*Tu asistente personal para generar documentos personalizados*")
    
    # ====== NAVEGACIÓN POR PASOS ======
    if st.session_state.step == "welcome":
        show_welcome_screen()
    elif st.session_state.step == "chat":
        show_chat_interface()
    elif st.session_state.step == "download":
        show_download_screen()

def show_welcome_screen():
    """Pantalla de bienvenida y carga de documento"""
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 👋 ¡Hola! Bienvenido a tu asistente de documentos
        
        Te ayudo a personalizar tus documentos Word de forma conversacional:
        
        1. **Sube tu plantilla** Word con variables como {{nombre}}, {{fecha}}
        2. **Responde mis preguntas** de forma natural
        3. **Descarga tu documento** personalizado
        
        ¡Es así de simple!
        """)
        
        # Upload del documento
        uploaded_file = st.file_uploader(
            "📎 Selecciona tu plantilla Word (.docx)",
            type=['docx'],
            help="Tu documento debe contener variables en formato {{nombre_variable}}"
        )
        
        if uploaded_file:
            process_uploaded_document(uploaded_file)
    
    with col2:
        st.info("""
        💡 **Ejemplo de variables:**
        
        - `{{nombre_cliente}}`
        - `{{fecha_contrato}}`
        - `{{monto_total}}`
        - `{{empresa}}`
        - `{{email}}`
        """)
        
        st.markdown("""
        ### 📊 Ejemplos de uso:
        - Contratos comerciales
        - Cartas oficiales  
        - Facturas
        - Propuestas
        - Certificados
        """)

def process_uploaded_document(uploaded_file):
    """Procesa el documento subido"""
    try:
        # Leer el documento
        doc = Document(uploaded_file)
        
        # Extraer todo el texto
        all_text = extract_all_text(doc)
        
        # Encontrar variables
        variables = extract_variables(all_text)
        
        if variables:
            # Detectar tipo de documento
            doc_type, doc_type_display = st.session_state.assistant.detect_document_type(all_text)
            
            # Guardar en session state
            st.session_state.variables = variables
            st.session_state.document = uploaded_file
            st.session_state.doc_type = doc_type
            st.session_state.doc_type_display = doc_type_display
            
            # Mostrar análisis
            st.success(f"✅ ¡Documento analizado exitosamente!")
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"""
                **Tipo detectado:** {doc_type_display}
                
                **Variables encontradas:** {len(variables)}
                """)
                
                # Mostrar variables en formato bonito
                st.markdown("**Variables a completar:**")
                variables_html = ""
                for var in variables:
                    variables_html += f'<span class="variable-tag">{{{{ {var} }}}}</span> '
                st.markdown(variables_html, unsafe_allow_html=True)
            
            with col2:
                st.metric(
                    label="Variables detectadas",
                    value=len(variables),
                    delta="Listo para personalizar"
                )
            
            # Inicializar chat
            st.session_state.chat_history = [{
                "role": "assistant",
                "content": f"¡Perfecto! He analizado tu {doc_type_display.lower()} y encontré {len(variables)} campos para personalizar. Te haré algunas preguntas rápidas. ¿Empezamos? 🚀"
            }]
            
            if st.button("🚀 Comenzar conversación", use_container_width=True):
                st.session_state.step = "chat"
                st.rerun()
        
        else:
            st.error("❌ No encontré variables en formato {{variable}} en tu documento")
            show_help_section()
    
    except Exception as e:
        st.error(f"❌ Error al procesar el documento: {str(e)}")
        st.info("Por favor asegúrate de que el archivo sea un documento Word válido (.docx)")

def show_help_section():
    """Muestra ayuda sobre cómo crear variables"""
    with st.expander("💡 ¿Cómo crear variables en mi documento?", expanded=True):
        st.markdown("""
        Para que el asistente pueda personalizar tu documento, necesitas marcar las partes variables:
        
        **❌ Incorrecto:**
        - NOMBRE DEL CLIENTE
        - [FECHA]
        - <MONTO>
        
        **✅ Correcto:**
        - {{nombre_cliente}}
        - {{fecha_contrato}}
        - {{monto_total}}
        
        **Ejemplo de documento:**
        Contrato entre {{empresa_contratante}} y {{cliente}}.
    
    Fecha: {{fecha_inicio}}
    Monto: {{monto_total}}
    """)

def extract_all_text(doc):
    """Extrae todo el texto del documento Word"""
    text = ""
    
    # Texto de párrafos
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    
    # Texto de tablas
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    text += paragraph.text + "\n"
    
    # Texto de encabezados y pies de página
    for section in doc.sections:
        if section.header:
            for paragraph in section.header.paragraphs:
                text += paragraph.text + "\n"
        if section.footer:
            for paragraph in section.footer.paragraphs:
                text += paragraph.text + "\n"
    
    return text

def extract_variables(text):
    """Extrae variables del texto"""
    variables = list(set(re.findall(r'\{\{([^}]+)\}\}', text)))
    return sorted(variables)

def show_chat_interface():
    """Interfaz de chat conversacional"""
    
    st.header("💬 Conversación con tu asistente")
    
    # Sidebar con progreso
    with st.sidebar:
        st.header("📊 Progreso")
        
        if st.session_state.variables:
            total_vars = len(st.session_state.variables)
            completed = len(st.session_state.responses)
            progress = completed / total_vars if total_vars > 0 else 0
            
            st.progress(progress)
            st.write(f"**Completado:** {completed}/{total_vars}")
            
            # Mostrar variables completadas
            if st.session_state.responses:
                st.subheader("✅ Datos guardados:")
                for var, response in st.session_state.responses.items():
                    st.write(f"**{var.replace('_', ' ').title()}:** {response}")
        
        # Botón para reiniciar
        if st.button("🔄 Empezar de nuevo"):
            st.session_state.clear()
            st.rerun()
    
    # Contenedor del chat
    chat_container = st.container()
    
    with chat_container:
        # Mostrar historial de chat
        for message in st.session_state.chat_history:
            if message["role"] == "assistant":
                st.chat_message("assistant", avatar="🤖").write(message["content"])
            else:
                st.chat_message("user", avatar="👤").write(message["content"])
    
    # Lógica de preguntas
    handle_chat_logic()

def handle_chat_logic():
    """Maneja la lógica del chat"""
    variables = st.session_state.variables
    current_q = st.session_state.current_question
    assistant = st.session_state.assistant
    
    if current_q < len(variables):
        current_var = variables[current_q]
        
        # Generar pregunta si no está en el historial
        if not st.session_state.chat_history or "?" not in st.session_state.chat_history[-1]["content"]:
            question = assistant.generate_smart_question(current_var, st.session_state.doc_type)
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": question
            })
            st.chat_message("assistant", avatar="🤖").write(question)
        
        # Campo de entrada
        show_input_field(current_var, current_q)
    
    else:
        # Todas las preguntas completadas
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": "🎉 ¡Excelente! Ya tengo toda la información necesaria. Tu documento personalizado está listo para generar."
        })
        st.session_state.step = "download"
        st.rerun()

def show_input_field(current_var, current_q):
    """Muestra el campo de entrada apropiado"""
    assistant = st.session_state.assistant
    input_type = assistant.get_input_type(current_var)
    
    col1, col2 = st.columns([4, 1])
    
    with col1:
        if input_type == 'date':
            user_input = st.date_input(
                "Selecciona la fecha:",
                key=f"input_{current_q}",
                help="Elige la fecha del calendario"
            )
            user_input = user_input.strftime("%d/%m/%Y")
        
        elif input_type == 'number':
            user_input = st.number_input(
                "Ingresa el monto:",
                min_value=0.0,
                step=0.01,
                key=f"input_{current_q}",
                help="Ingresa solo números"
            )
        
        elif input_type == 'email':
            user_input = st.text_input(
                "Escribe el email:",
                placeholder="ejemplo@correo.com",
                key=f"input_{current_q}",
                help="Formato: usuario@dominio.com"
            )
        
        else:
            user_input = st.text_input(
                "Tu respuesta:",
                key=f"input_{current_q}",
                help="Escribe tu respuesta aquí"
            )
    
    with col2:
        if st.button("Enviar", key=f"send_{current_q}"):
            handle_user_response(user_input, current_var, input_type)

def handle_user_response(user_input, current_var, input_type):
    """Procesa la respuesta del usuario"""
    assistant = st.session_state.assistant
    
    # Validar respuesta
    is_valid, error_msg = assistant.validate_response(user_input, input_type)
    
    if not is_valid:
        st.error(error_msg)
        return
    
    # Formatear respuesta
    formatted_response = format_response(user_input, input_type)
    
    # Agregar al chat
    st.session_state.chat_history.append({
        "role": "user",
        "content": str(formatted_response)
    })
    
    # Guardar respuesta
    st.session_state.responses[current_var] = formatted_response
    
    # Confirmación del asistente
    confirmation = assistant.generate_confirmation(current_var, formatted_response)
    st.session_state.chat_history.append({
        "role": "assistant",
        "content": confirmation
    })
    
    # Avanzar pregunta
    st.session_state.current_question += 1
    
    st.rerun()

def format_response(response, input_type):
    """Formatea la respuesta según el tipo"""
    if input_type == 'number':
        return f"${float(response):,.2f}"
    else:
        return str(response).strip()

def show_download_screen():
    """Pantalla de descarga del documento"""
    
    st.header("🎉 ¡Tu documento está listo!")
    
    # Mostrar últimos mensajes del chat
    for message in st.session_state.chat_history[-2:]:
        if message["role"] == "assistant":
            st.chat_message("assistant", avatar="🤖").write(message["content"])
    
    # Resumen de datos
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📋 Datos recopilados:")
        
        for var, response in st.session_state.responses.items():
            st.markdown(f"**{var.replace('_', ' ').title()}:** {response}")
    
    with col2:
        st.metric(
            label="Variables completadas",
            value=len(st.session_state.responses),
            delta="100% completo"
        )
        
        st.info(f"""
        📄 **Tipo:** {st.session_state.doc_type_display}
        
        ⏱️ **Tiempo:** {datetime.now().strftime('%H:%M')}
        
        ✅ **Estado:** Listo para descargar
        """)
    
    # Generar y descargar documento
    if st.button("📄 Generar y Descargar Documento", use_container_width=True):
        download_document()
    
    # Opciones adicionales
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔄 Crear otro documento", use_container_width=True):
            st.session_state.clear()
            st.rerun()
    
    with col2:
        if st.button("✏️ Modificar respuestas", use_container_width=True):
            st.session_state.step = "chat"
            st.session_state.current_question = 0
            st.session_state.responses = {}
            # Mantener solo mensaje inicial
            st.session_state.chat_history = st.session_state.chat_history[:1]
            st.rerun()

def download_document():
    """Genera y permite descargar el documento"""
    
    with st.spinner("🤖 Generando tu documento personalizado..."):
        try:
            # Cargar documento original
            doc = Document(st.session_state.document)
            
            # Reemplazar variables en todo el documento
            replace_variables_in_document(doc, st.session_state.responses)
            
            # Guardar en memoria
            doc_buffer = io.BytesIO()
            doc.save(doc_buffer)
            doc_buffer.seek(0)
            
            # Generar nombre de archivo
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            doc_type = st.session_state.doc_type
            filename = f"{doc_type}_personalizado_{timestamp}.docx"
            
            st.success("✅ ¡Documento generado exitosamente!")
            
            # Botón de descarga
            st.download_button(
                label="⬇️ Descargar Documento Word",
                data=doc_buffer.getvalue(),
                file_name=filename,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                use_container_width=True
            )
            
            # Mensaje final
            st.chat_message("assistant", avatar="🤖").write(
                "🎉 ¡Perfecto! Tu documento personalizado está listo. "
                "Todas las variables han sido reemplazadas correctamente. "
                "¡Gracias por usar el asistente!"
            )
            
        except Exception as e:
            st.error(f"❌ Error al generar el documento: {str(e)}")

def replace_variables_in_document(doc, responses):
    """Reemplaza las variables en todo el documento"""
    
    # Función auxiliar para reemplazar en párrafos
    def replace_in_paragraph(paragraph, replacements):
        for var, value in replacements.items():
            placeholder = f"{{{{{var}}}}}"
            if placeholder in paragraph.text:
                paragraph.text = paragraph.text.replace(placeholder, str(value))
    
    # Reemplazar en párrafos principales
    for paragraph in doc.paragraphs:
        replace_in_paragraph(paragraph, responses)
    
    # Reemplazar en tablas
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    replace_in_paragraph(paragraph, responses)
    
    # Reemplazar en encabezados y pies de página
    for section in doc.sections:
        if section.header:
            for paragraph in section.header.paragraphs:
                replace_in_paragraph(paragraph, responses)
        if section.footer:
            for paragraph in section.footer.paragraphs:
                replace_in_paragraph(paragraph, responses)

# ====== EJECUTAR APLICACIÓN ======
if __name__ == "__main__":
    main()
