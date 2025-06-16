function biggest =  biggestLU2RD(x)
s= size(x);
bunch_size = 4;
biggest = 0;
for i = 1:s(1) - (bunch_size-1)
    for j = 1:s(1) - (bunch_size-1)
        product  = 1;
        for w = 0:bunch_size-1
            product = product *x(i+w,j+w);
            if product > biggest
                biggest = product;
            end
        end
    end
end
