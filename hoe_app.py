import streamlit as st
import pandas as pd

# Datos base
data = {
    'Equipo': [
        'Laptop', 'Laptop', 'Laptop',
        'CPU', 'CPU', 'CPU',
        'Celular', 'Celular',
        'Tableta', 'Tableta',
        'Monitor', 'Monitor',
        'Pantalla LCD', 'Pantalla LCD',
        'Servidor', 'Servidor', 'Servidor',
        'Switch', 'Switch'
    ],
    'Operación': [
        'Desarmar carcasa', 'Extraer batería', 'Extraer disco duro',
        'Remover carcasa', 'Retirar RAM', 'Retirar disco duro',
        'Remover pantalla', 'Retirar batería',
        'Remover pantalla', 'Retirar batería',
        'Separar carcasa', 'Retirar panel LCD',
        'Separar carcasa', 'Retirar panel LCD grande',
        'Remover tapas', 'Extraer fuentes de poder', 'Retirar discos duros',
        'Retirar tapas', 'Desconectar puertos'
    ],
    'Tiempo (min)': [
        5, 2, 3,
        6, 4, 5,
        4, 3,
        4, 3,
        5, 6,
        7, 8,
        5, 7, 6,
        4, 3
    ]
}

df = pd.DataFrame(data)

st.title("Generador de HOE - Reciclaje Electrónico")

# Entradas del usuario
equipo = st.selectbox("Selecciona el tipo de equipo:", df['Equipo'].unique())
costo_hora = st.number_input("Costo de mano de obra ($/hora):", value=60)

if st.button("Generar HOE"):
    operaciones = df[df['Equipo'] == equipo]
    tiempo_total = operaciones['Tiempo (min)'].sum()
    costo_estimado = (tiempo_total / 60) * costo_hora

    st.subheader("Operaciones sugeridas:")
    for idx, row in operaciones.iterrows():
        st.write(f"- {row['Operación']} ({row['Tiempo (min)']} min)")

    st.markdown("---")
    st.write(f"**Tiempo Total:** {tiempo_total} minutos")
    st.write(f"**Costo Estimado:** ${costo_estimado:.2f}")
df = pd.read_excel('operaciones_hoe.xlsx')
    
