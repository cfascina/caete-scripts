PROGRAM main
  USE ISO_FORTRAN_ENV, ONLY: REAL32, REAL64, REAL128
  IMPLICIT NONE
  
  REAL(REAL128) :: tol = 0.0000001
  REAL(REAL128) :: x = 0.00000001
  
  if(x .eq. tol) then
      print*, 'x == tol'
  elseif(x .gt. tol) then
      print*, 'x > tol'
  else
      print*, 'x < tol'
  end if

  ! print*, x	
  ! print '(F11.9)', tol
END