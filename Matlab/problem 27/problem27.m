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


is_prime(2)

biggest = 0;
for a = -5000:5000
    for b = -5000:5000

        counter = 0;
        n = 0;
        while n < 6000
            number = n^2 + a*n +b;
            if is_prime(number) == 1
                counter = counter + 1;
                n = n+1;
            else
             
                break
            end

        end
        if counter> biggest
        biggest = counter;
        [biggest a b]
        end
    end
end
