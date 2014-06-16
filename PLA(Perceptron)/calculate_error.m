function error_sum=calculate_error(predict,y)
 n=size(predict,1);
 error_sum=0;
 for i=1:n
   if ~isequal(predict(i),y(i))
       error_sum=error_sum+1;
   end
 end
end

