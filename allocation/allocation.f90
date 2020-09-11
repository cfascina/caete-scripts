module allocation
    use ISO_FORTRAN_ENV, only: REAL32, REAL64, REAL128
    implicit none

    !==============================!
    != Constants
    !==============================!
    real(REAL64), parameter :: klatosa = 6000.0
    real(REAL64), parameter :: dw = 200.0
    real(REAL64), parameter :: ltor = 0.77302587552347657
    real(REAL64), parameter :: k_allom2 = 36.0
    real(REAL64), parameter :: k_allom3 = 0.22
    real(REAL64), parameter :: spec_leaf = 15.365607091853349 
    real(REAL64), parameter :: bminc = 0.0
    real(REAL64), parameter :: tol = 0.0000001
    real(REAL64), parameter :: pi = 3.1415926536

    !==============================!

    real(REAL64) :: H = 3 !SOMENTE PARA TESTES
    real(REAL64) :: L = 4 !SOMENTE PARA TESTES
    real(REAL64) :: SS = 2 !SOMENTE PARA TESTES
    real(REAL64) :: R = 4 !SOMENTE PARA TESTES
    real(REAL64) :: SW = 5 !SOMENTE PARA TESTES
    
    contains

    !==============================!
	!= Subrotines
	!==============================!
    ! Just to test comparisons with "tol" value
    ! It can be deleted later
    ! subroutine show_consts()
    !     implicit none
    !     real(REAL128) :: x = 0.0000001
        
    !     print*, 'show_consts()'
    !     print '(F11.9)', tol

    !     if(x .eq. tol) then
    !         print*, 'eq'
    !     elseif(x .gt. tol) then
    !         print*, 'gt'
    !     else
    !         print*, 'lt'
    !     end if

    ! end subroutine show_consts

    ! Use the bisection method to solve the leaf mass increment
    subroutine leaf_carbon(delta_leaf)
        real(REAL64) :: delta_leaf

        delta_leaf = bisection_method(0.0, 10.0)
        
        return
    end subroutine leaf_carbon

	! Once we have the leaf mass increment we can cant get 
    ! root mass increment based on the LTOR constant
    subroutine root_carbon(delta_leaf, delta_root)
        real(REAL64) :: delta_leaf
        real(REAL64) :: delta_root
        
        delta_root = (delta_leaf + L) / ltor - R
        
        return
    end subroutine root_carbon

    ! Finally using the cmass_increment mass conservation we can calculate sapwood increment
    subroutine sapwood_carbon(delta_leaf, delta_root, delta_sapwood)
        real(REAL64) :: delta_leaf
        real(REAL64) :: delta_root
        real(REAL64) :: delta_sapwood
        
        delta_sapwood = bminc - delta_leaf - delta_root
        
        return
    end subroutine sapwood_carbon

	!==============================!
	!= Functions
	!==============================!
    function bisection_method(a, b) result(midpoint)
        implicit none
        real(REAL32) :: a, b
        real(REAL64) :: aux_a, aux_b
        real(REAL64) :: midpoint
        
        aux_a = a
        aux_b = b

        if((f(aux_a) * f(aux_b)) .gt. 0) then
            midpoint = -2.0
            return
        endif
        
        do while((aux_b - aux_a) / 2.0 .gt. tol)
            midpoint = (aux_a + aux_b) / 2
            
            if(f(midpoint) .eq. 0.0) then
                exit            
            elseif(f(aux_a) * f(midpoint) .lt. 0) then
                aux_b = midpoint
            else
                aux_a = midpoint
            endif
        end do
    end function bisection_method

    function f(x) result(searched_x)
        implicit none
        real(REAL64) :: x
        real(REAL64) :: searched_x
        
        searched_x = & 
            calc_tau1() * &
            (SS - x - x / ltor + H) - &
            ( &
                (SS - x - x / ltor) / &
                (L + x) * calc_tau3() &
            ) ** calc_tau2()
    end function f

    function calc_tau1() result(tau1)
        implicit none
        real(REAL64) :: tau1
        
        tau1 = k_allom2 ** (2.0 / k_allom3) * 4.0 / 3.14159 / dw
    end function calc_tau1

    function calc_tau2() result(tau2)
        implicit none
        real(REAL64) :: tau2 
        
        tau2 = 1.0 + 2.0 / k_allom3
    end function calc_tau2

    function calc_tau3() result(tau3)
        implicit none
        real(REAL64) :: tau3
        
        tau3 = klatosa / dw / spec_leaf
    end function calc_tau3

    ! function sapwood (ltor, R, SW, L, bminc) result (SS)
    !     implicit none
    !     real :: ltor
    !     real :: R
    !     real :: SW
    !     real :: L
    !     real :: bminc
    !     real :: SS
        
    !     SS = SW + bminc - L / ltor + R
    ! end function sapwood
end module allocation
