function[]=pasillo2()

close;

N=50;

fp = fopen('velocity_model.dat','w');

for alpha=0:1:1000,
A=(1+4*alpha)*eye(N);
B=diag(-2*alpha*ones(1,N-1),1);
C=diag(-2*alpha*ones(1,N-1),-1);

T=A+B+C;
T(1,1)=1+3*alpha;
T(N,N)=1+2*alpha;              % alternative v_{i+1}=v_{i}

D=ones(N,1);

V=T\D;

J=mean(V);

fprintf(fp,"%f %f\n",alpha,J);
end

fclose(fp);

%J=alpha*J

return;

M=100;
dmax=1;

D=ones(N,1);

for i=0:M,

  d(i+1)=i*dmax/M;
  
  if d(i+1)<0.5, c=0; 
  else c=d(i+1)-0.5; end

  A=(1+4*c)*eye(N);
  B=diag(-2*c*ones(1,N-1),1);
  C=diag(-2*c*ones(1,N-1),-1);

  T=A+B+C;

  T(1,1)=1+3*c;
  %D(N,1)=1.2*D(N,1);
  D(N,1)=(1+2*c)*D(N,1);     % first  alternative v_{i+1}=v_{d(i+1)}
  %T(N,N)=1+2*c;              % second alternative v_{i+1}=v_{i}
  %T(N,N-1)=-4*c;             % third  alternative v_{i+1}=v_{i-1}

  V=T\D;

  J(i+1)=d(i+1)*sum(V);

end

%[d' J']

plot(d,J)

end
