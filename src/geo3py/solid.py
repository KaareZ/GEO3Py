# class Surface3D:
#     def __init__(self, name, r, dom_1, dom_2, dom_3):
#         self.name = name
#         self.r = r
#         self.dom_1 = dom_1
#         self.dom_2 = dom_2
#         self.dom_3 = dom_3
        
#     def __str__(self):
#         return f"{self.name} = {latex(r)}"

#     def getJacobi(self):
#         symbol_1 = self.dom_1[0]
#         symbol_2 = self.dom_2[0]
#         symbol_3 = self.dom_3[0]
#         jacobi = diff(self.r, symbol_1).cross(diff(self.r, symbol_2)).dot(diff(self.r, symbol_3))
#         return jacobi

#     def getVolume(self, dom_1=None, dom_2=None, dom_3=None):
#         if dom_1 is None: dom_1 = self.dom_1
#         if dom_2 is None: dom_2 = self.dom_2
#         if dom_3 is None: dom_3 = self.dom_3
#         jacobi = self.getJacobi()

#         vol_int = simplify(Integral(jacobi, dom_1, dom_2, dom_3))
#         vol = vol_int.doit()
#         return vol
