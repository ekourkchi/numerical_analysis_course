      program intpow
      implicit none
      integer j
      real x

      do j=1,1000000000
c         x=3.**7     ! takes 0.9 seconds
         x=3.**6.9    ! takes 2.1 seconds
      enddo
      print *,x

      end
