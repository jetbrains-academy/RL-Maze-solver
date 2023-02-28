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
    try:
        np.testing.assert_array_equal(not_zero_test, not_zero_actual,
                                  err_msg=f"The resulting Q matrix does not look like we expected. "
                                          f"The positions of Q values greater than 10 differ from "
                                          f"the expected for the test input F matrix \n {F_matrix}")
    except AssertionError as e:
        return str(e)
    try:
        np.testing.assert_array_equal(not_zero_feasibility, not_zero_actual, err_msg="You cannot assign "
                                                                                 "Quality values to "
                                                                                 "intersections of cells, "
                                                                                 "which are not reachable "
                                                                                 "from one another")
    except AssertionError as e:
        return str(e)
