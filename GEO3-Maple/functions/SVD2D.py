# GEO3, Python port
# SVD2D
# functions/SVD2D.py


# Description:
# SVD baseret 4-faktor split af given 2x2-matrix med søjle vektorer a og b.
# Out: Original SVD
#
# Globals:  Sigma, Sigma1, Sigma2, U, Vt, F, Energy
# Locals:  SingValDec, Uraw, Vtraw, detAA, A, AA
# Parameters: a::list, b::list
def SVD2D(a, b):
	##################################
	########## CONVERTED #############
	##################################
	
	
	####################
	
	####################
	
	####################
	
	
	AA:= evalf(Matrix([
	[a[1],b[1]],
	[a[2], b[2]]
	]))
	
	
	
	detAA:= Determinant(AA)
	
	if detAA < 0 :
		F:= Matrix([[0,1.], [1.,0]])
		A:= evalf(AA.F);
	else:
		A:= evalf(AA);
		
		F:= Matrix([[1,0], [0,1]])
	
	
	
	
	
	SingValDec:= [SingularValues(A, output=['U', 'S', 'Vt'])]
	
	Uraw:= SingValDec[1]
	
	Sigma:= DiagonalMatrix(SingValDec[2])
	
	Sigma1:= DiagonalMatrix([Sigma[1,1], 1])
	Sigma2:= DiagonalMatrix([1, Sigma[2,2]])
	
	Energy:= (1-Sigma[1,1])^2 + (1-Sigma[2,2])^2
	
	Vtraw:= SingValDec[3]
	
	# Guarantee that the 'first' rotation is chosen positively
	# oriented obtain by changing sign on first Vt row and then
	# corresondingly change sign on first U column:
	
	if Determinant(Vtraw) < 0 :
		Vt:= RowOperation(Vtraw, 1, -1)
	else:
		Vt:= Vtraw
	
	
	
	if Determinant(Vtraw) < 0 :
		U:= ColumnOperation(Uraw, 1, -1)
	else:
		U:= Uraw
	
	
	
	
	####################
	
##################################
########## ORIGINAL ##############
##################################
	
	
	####################
	
	####################
	
	####################
	      
	
	AA:= evalf(Matrix([
	[a[1],b[1]],
	[a[2], b[2]]
	]));
	
	
	
	detAA:= Determinant(AA);
	
	if detAA < 0 then 
	F:= Matrix([[0,1.], [1.,0]]);
	A:= evalf(AA.F); else
	A:= evalf(AA); 
	F:= Matrix([[1,0], [0,1]]);
	end if;
	
	
	
	
	SingValDec:= [SingularValues(A, output=['U', 'S', 'Vt'])];
	
	Uraw:= SingValDec[1];
	
	Sigma:= DiagonalMatrix(SingValDec[2]);
	
	Sigma1:= DiagonalMatrix([Sigma[1,1], 1]);
	Sigma2:= DiagonalMatrix([1, Sigma[2,2]]);
	
	Energy:= (1-Sigma[1,1])^2 + (1-Sigma[2,2])^2;
	
	Vtraw:= SingValDec[3];
	
	# Guarantee that the 'first' rotation is chosen positively 
	# oriented obtain by changing sign on first Vt row and then
	# corresondingly change sign on first U column:
	
	if Determinant(Vtraw) < 0 then 
	Vt:= RowOperation(Vtraw, 1, -1);
	else
	Vt:= Vtraw;
	end if;
	
	
	if Determinant(Vtraw) < 0 then 
	U:= ColumnOperation(Uraw, 1, -1);
	else
	U:= Uraw;
	end if;
	
	
	
	####################
	
