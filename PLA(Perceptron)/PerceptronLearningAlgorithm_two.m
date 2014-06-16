function [weights,w0,number_change]=PerceptronLearningAlgorithm_two(X,y)
%Perceptron Learning Algorithm (PLA)
%the number of training features

m=size(X,1);
n=size(X,2);

weights = zeros(n,1);
w0=0;
No_mistake=false;
number_change=0;
while (~No_mistake)
    No_mistake=true;
    for i=1:m
        %预测结果，用于比较是否分类错误
        prediction = sign_def (X(i,:) * weights+w0);
        if ~isequal(prediction,y(i))%当分类错误的时候
            No_mistake=false;
            number_change =number_change+1;
            disp(num2str(number_change));
            weights = weights + y(i) * X(i,:)';%更新权重,该方法属于感知机的原始形式
            w0=w0+y(i);%更新w0
        end
    end
end

end