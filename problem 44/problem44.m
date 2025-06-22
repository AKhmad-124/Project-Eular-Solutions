clc;clearvars;

function x = pent_gen(n)
x = n.*(3.*n-1)./2;
end

function x = pent_check(number)
n=(sqrt(24*number +1)+1)/6;
if mod(n,1)== 0
    x=1;
else
    x=0;
end
end

% for i = 1:90
% pent_check(pent_gen(i)+1)
% end

for j = 1:10000
    j
for k = 1:10000
pj = pent_gen(j);
pk = pent_gen(k);

if pent_check(pj+pk) == 1
    if pj-pk >= 0 
      if pent_check(pj-pk) == 1
           z = [j k pj pk pk-pj]
      end
   end
end

end
end
z

