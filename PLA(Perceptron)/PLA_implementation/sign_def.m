function sign_self=sign_def(x)
%可以预测多个结果，比如x是一个向量，说明对向量中的每个元素
%标定
s=size(x,1);
sign_self=zeros(s,1);
for i=1:s
   if x(i)>0 
       sign_self(i)=1;
   else if x(i)==0
       sign_self(i)=-1;
   else if x(i)<0
       sign_self(i)=-1;
       end
       end
   end
end