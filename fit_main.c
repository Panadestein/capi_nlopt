
#include "nlopt.h"
#include <stdio.h>
#include <stdlib.h>


double opt_me(int n, const double *x, double *grad, void *func_data)
{
	const double a = x[0];
	const double b = x[1];
	const double v1 = (a*a + b - 11);
	const double v2 = (a + b*b - 7);

	return v1*v1 + v2*v2;
}


int main() {

	int maxeval = 1000;
	double minrms = 0.01;
	double tol = 0.0001;

	double lower[] = {-5., -5.};
	double upper[] = {5., 5.};
	double param_values[] = {0., 0.};
	double minf;

	//nlopt_opt opt = nlopt_create(NLOPT_G_MLSL_LDS, 2);
	nlopt_opt opt = nlopt_create(29, 2);
	nlopt_set_local_optimizer(opt, nlopt_create(NLOPT_LN_BOBYQA, 2));

	nlopt_set_lower_bounds(opt, lower);
	nlopt_set_upper_bounds(opt, upper);

	nlopt_set_min_objective(opt, opt_me, NULL);
	nlopt_set_maxeval(opt, maxeval);
	nlopt_set_stopval(opt, minrms);
	nlopt_set_ftol_abs(opt, tol);

	if (nlopt_optimize(opt, param_values, &minf) < 0)
		printf("NLopt failed!\n");
	else
		printf("Found minimum at f(%g,%g) = %0.10g\n",
		       param_values[0], param_values[1], minf);

	nlopt_destroy(opt);

	return 0;
}

