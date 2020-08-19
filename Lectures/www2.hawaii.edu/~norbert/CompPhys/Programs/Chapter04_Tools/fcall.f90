! program which test whether initialization in
! a subroutine is done only the first time the
! subroutine is called

program fcall
implicit none
call hehe
call hehe
end program fcall




subroutine hehe
implicit none
integer :: b=-1
print *,b
b=7
end subroutine hehe
