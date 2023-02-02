import numpy as np
import wrapt_timeout_decorator

timeoutlimit = 20


@wrapt_timeout_decorator.timeout(timeoutlimit)
def test_function(agent, test_agent, F_matrix, max_epochs):
    agent.train(F_matrix, max_epochs)
    test_agent.train(F_matrix, max_epochs)
    not_zero_actual = np.where(test_agent.Q >= 10)
    not_zero_test = np.where(agent.Q >= 10)
    not_zero_feasibility = np.where(F_matrix != 0)
    np.testing.assert_array_equal(not_zero_test, not_zero_actual,
                                  err_msg="The resulting Q matrix does not look like we expected.")
    np.testing.assert_array_equal(not_zero_feasibility, not_zero_actual, err_msg="You cannot assign "
                                                                                 "Quality values to "
                                                                                 "intersections of cells, "
                                                                                 "which are not reachable "
                                                                                 "from one another")
