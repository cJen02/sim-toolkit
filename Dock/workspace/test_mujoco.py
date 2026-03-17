import mujoco # type: ignore
import numpy as np

xml = """
<mujoco>
  <worldbody>
    <light diffuse=".5 .5 .5" pos="0 0 3" dir="0 0 -1"/>
    <geom type="plane" size="1 1 0.1" rgba=".9 .9 .9 1"/>
    <body name="box" pos="0 0 1">
      <joint name="free" type="free"/>
      <geom type="box" size=".1 .1 .1" rgba=".8 .2 .2 1" mass="1"/>
    </body>
  </worldbody>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(xml)
data  = mujoco.MjData(model)

print("Model loaded")
print(f"  Bodies : {model.nbody}")
print(f"  DOFs   : {model.nv}")
print(f"  Box start pos: {data.qpos[:3]}")

for i in range(500):
    mujoco.mj_step(model, data)

print(f"\nAfter 500 steps (box fell under gravity):")
print(f"  Box pos: {data.qpos[:3].round(4)}")
print(f"  Time   : {data.time:.3f}s")
print("\nMuJoCo simulation OK")