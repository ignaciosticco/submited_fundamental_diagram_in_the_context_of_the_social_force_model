function[]=pasillo4()

close;

N=10;
c=1000;

fp = fopen('flux_model_revised_1000.dat','w');

for alpha=-0.05:0.001:5.0,
A=(1+4*c*alpha)*eye(N);
B=diag(-2*c*alpha*ones(1,N-1),1);
C=diag(-2*c*alpha*ones(1,N-1),-1);

T=A+B+C;
T(1,1)=1+3*c*alpha;
T(N,N)=1+2*c*alpha;              % alternative v_{i+1}=v_{i}

D=ones(N,1);

V=T\D;

if alpha<0, J=1; 
else J=(1+alpha)*mean(V);
end

fprintf(fp,"%f %f\n",alpha,J);
end

fclose(fp);

return;


