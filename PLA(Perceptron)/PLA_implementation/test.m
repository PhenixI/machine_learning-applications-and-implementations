input=load('data.txt');
si=size(input,2);
X=input(:,1:si-1);
y=input(:,si);
number=0;
input=load('test.txt');
si=size(input,2);
n=size(input,1);
X_test=input(:,1:si-1);
y_test=input(:,si);
error1 =0.0;
for i=1:2000
[weights,w0,number_change]=PerceptronLearningAlgorithm_two(X,y);

predict=sign_def(X_test*weights+w0);
error = calculate_error(predict,y_test);
error1 = error1+(error/n);

end

error1 = error/2000;
disp(num2str(error1));

