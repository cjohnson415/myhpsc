
program test_quartic

	use newton, only: solve, tol
	use functions, only: f_quartic, fprime_quartic, eps

    implicit none
    real(kind=8) :: x, x0, fx, xstar
    real(kind=8) :: tol_vals(3), eps_vals(3), xstar_vals(3)
    integer :: iters, i_eps, i_tol
	logical :: debug         ! set to .true. or .false.

	! Set params
	x0 = 4.d0
	debug = .false.
	tol_vals = (/1.d-5, 1.d-10, 1.d-14/)
	eps_vals = (/1.d-4, 1.d-8, 1.d-12/)
	xstar_vals = (/1.1d0, 1.01d0, 1.001d0/)

	print *, ' ' ! blank line
	print 11, x0
11  format('Starting with initial guess ', es22.15)
	print *, ' ' ! blank line
	
	print *, '    epsilon        tol    iters          x                 f(x)        x-xstar'

	do i_eps=1,3
		eps = eps_vals(i_eps)
		xstar = xstar_vals(i_eps)
		do i_tol=1,3

			tol = tol_vals(i_tol)
			call solve(f_quartic, fprime_quartic, x0, x, iters, debug)
			fx = f_quartic(x)
		
			print 12, eps, tol, iters, x, fx, x-xstar
12			format(2es13.3, i4, es24.15, 2es13.3)

			enddo
		print *, ' ' ! blank line
		enddo


end program test_quartic
		
