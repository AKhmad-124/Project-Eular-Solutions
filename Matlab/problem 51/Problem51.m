clc;clearvars;
function answer = is_prime(number)
i=3;
    if number <2
        answer = 0;
        return 
    end
while i <= round(sqrt(number))
    if mod(number,i) == 0
        answer = 0;
        return 
    end
    i = i+2;
end
answer=1;
end

function amount = divide_and_replace(number,indexvec,max_tries)
number_vec = num2str(number) -'0';

y = zeros(size(number_vec));
y(indexvec) = 1;
y = str2double(sprintf('%d',y));

x = zeros(size(indexvec))+9;

for i = 0:9
    
    number_vec(indexvec) = x;
    x = x-1;
    new_number = str2double(sprintf('%d',number_vec))
    mod(new_number,y)
end

end
divide_and_replace(13,[1],1)


function all_indexvec = generateindex(size)%size as in 1111 --> size = 4
for z = 0:size-2
    z
for i=1:size
for j=i+z:size 
j
end
end
end
end
generateindex(4)
%remember:
% x=num2str(56993-56003) -'0'
% y= (56993-56113)
%  56993-56333
%  56993-56443
%  56993-56663
%  56993-56773
%  56993-56993
% x
% b = str2double(sprintf('%d',x))
