# Copyright (C) 2018 AGUILAR-MENA Jimmy and PANADES-BARRUETA Ramon L.
# This file is part of capi_nlopt <https://github.com/Panadestein/capi_nlopt.git> 
#
# capi_nlopt is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# capi_nlopt is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with capi_nlopt.  If not, see <http://www.gnu.org/licenses/>.
#!/usr/bin/env python3

import numpy as np
import wnlopt

# We'll optimize Himmelblau's function
def opt_me(x, grad):
    a, b = x[0], x[1]
    return (a**2 + b - 11)**2 + (a + b**2 - 7)**2

# Set variables
maxeval = 1000
minrms = 0.01
tol = 0.0001
param_values = np.array([0, 0], dtype=np.float64)

print(wnlopt.NLOPT_G_MLSL_LDS, wnlopt.NLOPT_LN_BOBYQA)

# C API wrapper
opt = wnlopt.PyNlopt(wnlopt.NLOPT_G_MLSL_LDS, 2)
opt.set_local_optimizer(wnlopt.PyNlopt(wnlopt.NLOPT_LN_BOBYQA, 2))

opt.set_lower_bounds(np.array([-5, -5], dtype=np.float64))
opt.set_upper_bounds(np.array([5, 5], dtype=np.float64))

opt.set_callback(opt_me)
opt.set_maxeval(maxeval)
opt.set_stopval(minrms)
opt.set_ftol_abs(tol)
minf = opt.optimize(param_values, 0.0)
print("minimum: f(%lf, %lf) = %lf" %
      (param_values[0], param_values[1], minf))
