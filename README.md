# 🌀 Procedural Rotating Planes – Blender Python Animation

A fully procedural 3D animation built in **Blender** using **Python scripting** (`bpy`).  
This project creates a visually striking stack of 100 rotating square planes that move in a rhythmic, alternating pattern — all generated programmatically.

---

## 🎨 Features

- 🧱 **100 stacked planes** generated automatically  
- 🔄 **Alternating clockwise / counterclockwise rotation**  
- 📏 **Gradual scale increase** and **1 m vertical spacing** between planes  
- ⚙️ **Smooth keyframed animation** with phase differences (`π/6`)  
- 🧮 Built entirely with Blender’s Python API (`bpy`)  
- 🌈 Easily customizable parameters: plane count, speed, spacing, colors, and more  

---

## 🖼️ Preview

![Preview Animation](preview.gif)

*(Generated directly in Blender using the included Python script.)*

---

## 🧰 How to Use

1. Open **Blender** and switch to the **Scripting** workspace.  
2. Create a new text block and paste the contents of `rotating_planes.py`.  
3. Press **Alt + P** to execute the script.  
4. Hit **Spacebar** to play the animation.  
5. To render your own preview, go to **Render → Render Animation**.

---

## ⚙️ Parameters

| Parameter | Description | Default |
|------------|--------------|----------|
| `plane_count` | Number of planes | 100 |
| `base_size` | Size of the first plane (in meters) | 1.0 |
| `size_step` | Increment in plane size | 0.2 |
| `z_step` | Spacing along Z-axis | -1.0 |
| `frames` | Total frames in one full rotation | 240 |
| `phase_step` | Phase offset between same-direction planes | π/6 |

---

## 🎬 Example Animation Logic

- Plane 1 → 1 m × 1 m  → Z = 0  → rotates clockwise  
- Plane 2 → 1.2 m × 1.2 m  → Z = –1  → rotates counter-clockwise  
- Plane 3 → 1.4 m × 1.4 m  → Z = –2  → rotates clockwise (phase + π/6)  
- … continues up to Plane 100

---

## 🧠 Concepts Demonstrated

- Procedural modeling with the **Blender Python API**  
- Automated **keyframe animation** generation  
- Mathematical **phase control** for motion synchronization  
- **Parametric design** and motion symmetry

---

## 📦 Files Included


---

## 🪐 License

Released under the **MIT License** — feel free to modify and use for your own creative or educational projects.

---

✨ *Created with Blender, Python, and a bit of math-driven motion design.*


