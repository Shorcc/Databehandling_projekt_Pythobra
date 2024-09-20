import sympy as sp
import matplotlib.pyplot as plt

class PythobraBackend:
    def __init__(self):
        pass



    def solve_equation(self, equation, unknown):
        begge_sider = equation.split("=")
        equation1 = sp.Eq(sp.parse_expr(begge_sider[0]),sp.parse_expr(begge_sider[1]))
        løsning = sp.solve(equation1, unknown)
        return str(løsning[0].evalf(4))



    def plot_function(
        self,
        mpl_ax,
        function_name,
        function_expression,
        domain_min,
        domain_max,
        color,
        line_style,
        show_name,
        show_legend,
    ):
        pass
