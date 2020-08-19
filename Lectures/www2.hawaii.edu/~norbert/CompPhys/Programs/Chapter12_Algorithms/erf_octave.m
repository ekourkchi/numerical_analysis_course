function y=erf_octave(x)

%Abramovitz&Stegun 7.1.28

a1=0.0705230784;  a2=0.0422820123;
a3=0.0092705272;  a4=0.0001520143;
a5=0.0002765672;  a6=0.0000430638;

y= 1.-1./(1+x.*(a1+x.*(a2+x.*(a3+x.*(a4+x.*(a5+x.*a6)))))).^16;

%12+4+2 flops
%error <=3.e-7