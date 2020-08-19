! ****************************************************************
!   NAME:                Ehsan Kourkchi
! 
!   HOMEWORK:            8
! 
!   CLASS:               Scientific Computation (IfA)
! 
!   INSTRUCTOR:          Norbert Schorghofer
! 
!   DATE:                November 04, 2015           
! 
!   FILE:                hw08.f90
! 
!   DESCRIPTION:
!   
!   How to compile: $ ifort -O hw08.py
! 
! ****************************************************************
!
!
!  
! This is the non-optimized code ...
! for N=40,000, it takes ~15 sec on node31 at IfA
! The array 'r' is useless and takes so much time to allocate, refrenced and deallocate
!

program hw08
implicit none

   integer, parameter :: N = 40000
   real(8), dimension(:,:), allocatable :: r
   real, dimension(N) ::  x,y
   real m
   integer :: i,j
   
   allocate( r(N,N) )
   r(1:N,1:N) = 1D0
! ... x and y have been assigned values earlier ...
   m=1E38
   do i=1,N
       do j=1,N
         if (i==j) cycle ! skips to next iteration
         r(i,j) = sqrt((x(i)-x(j))**2. + (y(i)-y(j))**2.)
         if (r(i,j)<m) m=r(i,j)
       enddo
   enddo
! m is minimum distance

   deallocate(r)

end



!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!
!   This is the optimized code
!   We don't need to really allocate an extra 2d matrix "r"
!   The process of allocation really takes long time
!   and we do Not really use that matrix
!
!   Using the following tricks, the running-time reduces to 0.003 sec on node31
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


program hw08_optimized
implicit none

   integer, parameter :: N = 40000

! We don't use "r" any more
!    real(8), dimension(:,:), allocatable :: r
   real, dimension(N) ::  x,y
   real m,distance
   integer :: i,j
   
!    allocate( r(N,N) )
!    r(1:N,1:N) = 1D0
! ... x and y have been assigned values earlier ...
   m=1E38
   
   
   ! We don't need to cross check each pair twice
   do i=1,N-1
       do j=i+1,N
       
           ! we don't nedd this, we take care of this situation when setting up the llop-variables
!          if (i==j) cycle ! skips to next iteration
         
         ! instead of r(i,j), we use the single variable 'distance'
         ! The following arrangment may help a little bit
         ! to calculate the independent subtractions all at once
         !
         !  a = x(i)-x(j)
         !  b = y(i)-y(j)
         !  distance = sqrt(a*a + b*b) 
         !
         !  Sometiems, for simple cases it's better to use direrct multiplication
         !  instead of using the power function
         !
         ! I guess, ifort takes care of these kind of simple situations 
         !
         distance = sqrt((x(i)-x(j))**2. + (y(i)-y(j))**2.)
         if (distance<m) m=distance
       enddo
   enddo
! m is minimum distance

! no "r", no allocation and deallocation
!    deallocate(r)

end
