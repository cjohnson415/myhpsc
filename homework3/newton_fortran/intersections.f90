! Main program for finding intersection of g1 and g2

program intersections
	
	use newton, only: solve
	use functions, only: g, gp

	implicit none
    integer :: iters, itest
	integer, parameter :: n_points = 4
    real(kind=8) :: x, x0, fx
    real(kind=8) :: x0vals(n_points)
	logical :: debug         ! set to .true. or .false.

	x0vals = (/-2.15, -1.7,-.9,1.3/)
	debug = .false.

	do itest=1,n_points
		x0 = x0vals(itest)
		print *, ' '  ! blank line
        call solve(g, gp, x0, x, iters, debug)

		print 11, x0
11		format('With inital guess x0 = ', e22.14)
        print 12, x, iters
12      format('solver returns x = ', e22.15, ' after', i3, ' iterations')
		
		enddo
	
end program intersections
