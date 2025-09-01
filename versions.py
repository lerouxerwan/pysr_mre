
from pysr.julia_import import Pkg, jl, jl_version

from importlib.metadata import version

print(version('pysr'))

print(jl, type(jl))
print(Pkg, type(Pkg))
print(jl.VERSION, type(jl.VERSION))
print(jl_version)