! $UWHPSC/codes/fortran/newton/functions.f90

module functions

contains

real(kind=8) function f_sqrt(x)
    implicit none
    real(kind=8), intent(in) :: x

    f_sqrt = x**2 - 4.d0

end function f_sqrt


real(kind=8) function fprime_sqrt(x)
    implicit none
    real(kind=8), intent(in) :: x
    
    fprime_sqrt = 2.d0 * x

end function fprime_sqrt


real(kind=8) function g(x)
	implicit none
	real(kind=8), parameter :: pi = ACOS(-1.d0)
	real(kind=8), intent(in) :: x

	g = x*COS(pi*x) - 1.d0 + 0.6*(x**2)

end function g


real(kind=8) function gp(x)
	implicit none
	real(kind=8), parameter :: pi = ACOS(-1.d0)
	real(kind=8), intent(in) :: x

	gp = -pi*x*SIN(pi*x) + COS(pi*x)  +1.2*x

end function gp


end module functions
