import numpy as np
import plotly.graph_objs as go

# Crear datos iniciales
theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, np.pi, 100)
theta, phi = np.meshgrid(theta, phi)

# Coordenadas esféricas para crear un efecto de expansión y contracción
r = 1  # Radio inicial
x = r * np.sin(phi) * np.cos(theta)
y = r * np.sin(phi) * np.sin(theta)
z = r * np.cos(phi)

# Crear los frames para la animación
frames = []
for i in range(1, 100):
    scale_factor = np.sin(i * 0.1) + 1.5  # Factor de escala dinámico
    x_frame = scale_factor * np.sin(phi) * np.cos(theta)
    y_frame = scale_factor * np.sin(phi) * np.sin(theta)
    z_frame = scale_factor * np.cos(phi)
    
    frames.append(go.Frame(data=[go.Scatter3d(
        x=x_frame.flatten(), 
        y=y_frame.flatten(), 
        z=z_frame.flatten(),
        mode='markers',
        marker=dict(size=4, color=z_frame.flatten(), colorscale='Rainbow', opacity=0.8)
    )]))

# Crear la traza inicial
scatter = go.Scatter3d(
    x=x.flatten(), 
    y=y.flatten(), 
    z=z.flatten(), 
    mode='markers',
    marker=dict(size=4, color=z.flatten(), colorscale='Rainbow', opacity=0.8)
)

# Crear la figura y configurar la animación
fig = go.Figure(
    data=[scatter],
    layout=go.Layout(
        title="Expansión y Contracción de Puntos 3D",
        scene=dict(
            xaxis=dict(range=[-3, 3], autorange=False, backgroundcolor="rgb(230, 230, 255)"),
            yaxis=dict(range=[-3, 3], autorange=False, backgroundcolor="rgb(230, 255, 230)"),
            zaxis=dict(range=[-3, 3], autorange=False, backgroundcolor="rgb(255, 230, 230)"),
        ),
        margin=dict(l=0, r=0, b=0, t=40),
        updatemenus=[dict(type="buttons", showactive=False, buttons=[dict(label="Play", method="animate", args=[None, {"frame": {"duration": 100, "redraw": True}, "fromcurrent": True, "transition": {"duration": 0}}])])],
    ),
    frames=frames
)

# Iniciar animación automáticamente
fig.update_layout(
    updatemenus=[dict(type="buttons", showactive=False, buttons=[dict(label="",
        method="animate", args=[None, {"frame": {"duration": 100, "redraw": True}, "fromcurrent": True, "transition": {"duration": 0}}])])],
    sliders=[{
        "steps": [{"args": [[f.name], {"frame": {"duration": 100, "redraw": True}, "mode": "immediate", "transition": {"duration": 0}}], "label": f"Step {k}", "method": "animate"} for k, f in enumerate(frames)],
        "currentvalue": {"prefix": "Frame: "},
        "pad": {"b": 10},
        "len": 0.9
    }]
)

# Mostrar la gráfica
fig.show()





