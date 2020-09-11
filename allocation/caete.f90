program caete
    use ISO_FORTRAN_ENV, only: REAL32, REAL64, REAL128
    use allocation
    implicit none

    real(REAL64) :: delta_leaf
    real(REAL64) :: delta_root
    real(REAL64) :: delta_sapwood

    ! call show_consts()
    
    call leaf_carbon(delta_leaf)
    print*, 'CARBON ON LEAF =', delta_leaf

    call root_carbon(delta_leaf, delta_root)
    print*, 'CARBON ON ROOT =', delta_root
    
    call sapwood_carbon(delta_leaf, delta_root, delta_sapwood)
    print*, 'CARBON ON SAPWOOD =', delta_sapwood
end program caete